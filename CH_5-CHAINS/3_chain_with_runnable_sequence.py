from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Your answer should be in just one sentence."),
    ("human", "Tell me a joke about {topic}.")
    ])

parser = StrOutputParser() 

chain = RunnableSequence(prompt_template, llm, parser) # This is another way to create a chain in series.


response = chain.invoke({"topic": "computers"})

print(response)