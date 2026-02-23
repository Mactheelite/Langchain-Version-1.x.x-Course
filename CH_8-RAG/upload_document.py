from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from config import CHROMA_TENANT, CHROMA_DATABASE, CHROMA_API_KEY, COLLECTION_NAME, EMBEDDING_MODEL

import tempfile

def upload_document_from_bytes(filename: str, file_bytes: bytes):

    # 1️ Save the PDF temporarily
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
        tmp_file.write(file_bytes)
        tmp_path = tmp_file.name

    # 2️ Load PDF
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    # 3️ Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    # 4️ Add metadata
    for chunk in chunks:
        chunk.metadata["source"] = filename

    # 5️ Embeddings
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    # 6️ Chroma Cloud vector store
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        chroma_cloud_api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE
    )

    # 7 Upload chunks
    vectorstore.add_documents(chunks)

    print(f"✅ {filename} uploaded successfully to Chroma Cloud.")


def delete_document_by_filename(filename: str):
    """
    Delete all document chunks from Chroma Cloud that have the specified filename in metadata.
    """
    # 1️ Embeddings
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    # 2️ Chroma Cloud vector store
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        chroma_cloud_api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE
    )

    # 3️ Get all documents with this filename
    results = vectorstore.get(where={"source": filename})
    
    if not results['ids']:
        return {"status": "not_found", "message": f"No documents found with filename: {filename}"}
    
    # 4️ Delete the documents
    vectorstore.delete(ids=results['ids'])
    
    return {"status": "success", "message": f"Deleted {len(results['ids'])} chunks from {filename}"}