from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from config import (
    CHROMA_TENANT,
    CHROMA_DATABASE,
    CHROMA_API_KEY,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    LLM_MODEL,
)


def build_rag_chain():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        chroma_cloud_api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE,
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr", search_kwargs={"k": 4, "fetch_k": 20}
    )

    llm = ChatOpenAI(model=LLM_MODEL, temperature=0)

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful assistant.
Use ONLY the context below to answer.
If the answer is not in context, say "I don't know."

Context:
{context}

Question:
{question}
"""
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain