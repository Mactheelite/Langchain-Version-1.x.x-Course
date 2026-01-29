
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0
)


# Define a reusable prompt template
# - "system" sets the assistant's behavior
# - "human" is the user input
# - {topic} is a variable that will be filled in at runtime
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Give me the most recent answers. Make it short."),
    ("human", "Tell me a joke about {topic}.")
])


formatted_prompt = prompt_template.invoke({
    "topic": "computers"
})


# Send the formatted prompt to the LLM
response = llm.invoke(formatted_prompt)
print(response.content)
