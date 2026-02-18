from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

prompt_template = PromptTemplate.from_template(
    "Tell me a joke about {topic}."
)

formated_prompt = prompt_template.invoke({"topic": "computers"})


response = llm.invoke(formated_prompt)

print(response.content)