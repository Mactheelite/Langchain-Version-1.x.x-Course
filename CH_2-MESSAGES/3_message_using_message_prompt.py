
# Message prompts
# Alternatively, you can pass in a list of messages to the model by 
# providing a list of message objects.

# Use message prompts when:
# ~ Managing multi-turn conversations
# ~ Working with multimodal content (images, audio, files)
# ~ Including system instructions

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage

load_dotenv()


llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# Message must alway be in a list

# Using message objects
messages_1 = [
    SystemMessage(content="You are a poetry expert"),
    HumanMessage(content="Write a short poetry about 'orange' in 25 words."),
    AIMessage("Cherry blossoms bloom...") # This is optional
]

# Using dictionaries
messages_2 = [
    {"role": "system", "content": "You are a poetry expert"}, 
    {"role": "user", "content": "Write a haiku about spring"}, # It's either you use "user", or "human" for the role
    {"role": "assistant", "content": "Cherry blossoms bloom..."} # This is optional
]

response = llm.invoke(messages_2) # Returns AIMessage

print(response.content)



#Notes

## System message
# A SystemMessage represent an initial set of instructions that primes the model’s behavior. 
# You can use a system message to set the tone, define the model’s role, and establish guidelines for responses.

# Human message
# A HumanMessage represents user input and interactions. 
# They can contain text, images, audio, files, and any other amount of multimodal content.

# AI message
# An AIMessage represents the output of a model invocation. 
# They can include multimodal data, tool calls, and provider-specific metadata that you can later access.