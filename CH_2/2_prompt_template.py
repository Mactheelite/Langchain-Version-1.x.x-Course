from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")


llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

prompt_template = PromptTemplate.from_template(
    "Tell me a joke about {topic}."
)

formated_prompt = prompt_template.invoke({"topic": "computers"})


response = llm.invoke(formated_prompt)

print(response.content)