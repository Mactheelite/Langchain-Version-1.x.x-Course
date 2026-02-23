from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from config import (CHROMA_TENANT, CHROMA_DATABASE, CHROMA_API_KEY, COLLECTION_NAME, EMBEDDING_MODEL)

def ingest_documents(file_path: str):
    # Load the document
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Create embeddings for the chunks
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    embeddings = embedding_model.embed_documents([chunk.page_content for chunk in chunks])


    # Cloud vector store connection
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        chroma_cloud_api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE
    )

    vectorstore.add_documents(chunks)
    print("✅ Documents uploaded to Chroma Cloud.")

if __name__ == "__main__":
    ingest_documents("data/sample.txt")
