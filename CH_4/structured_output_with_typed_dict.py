from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict

load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

class JokeResponse(TypedDict):
    joke: str
    length: int

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
llm_with_typed_dict = llm.with_structured_output(JokeResponse)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Give me the most recent answers. Make it short."),
    ("human", "Tell me a joke about {topic}.")
    ])

formated_prompt = prompt_template.invoke({"topic": "computers"})


response = llm_with_typed_dict.invoke(formated_prompt)

print(response)
print(response.get("joke"))
print(response.get("length"))