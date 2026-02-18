# Make sure to install pydantic before running this example:
# pip install pydantic or uv add pydantic

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

load_dotenv()

class JokeResponse(BaseModel):
    joke: str
    length: int

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
llm_with_pydantic = llm.with_structured_output(JokeResponse)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Your answer should be in just one sentence."),
    ("human", "Tell me a joke about {topic}.")
    ])

formated_prompt = prompt_template.invoke({"topic": "computers"})


response = llm_with_pydantic.invoke(formated_prompt)

print(response)
print("-"*100)
print(response.joke)
print(response.length)