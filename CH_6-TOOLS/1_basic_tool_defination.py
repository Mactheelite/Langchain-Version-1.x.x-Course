# Basic tool definition

# The simplest way to create a tool is with the @tool decorator. 
# By default, the function’s docstring becomes the tool’s description that helps the model understand when to use it.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# Defining a basic tool using the @tool decorator
@tool
def addition_calculator(a: int, b: int) -> str:
    """Adds two numbers and returns the result as a string. Use this tool only when you need to perform addition.
    
    Args:
        a: The first number.
        b: The second number.
    """
    return f"The sum of {a} and {b} is {a + b}."

@tool
def multiplication_calculator(a: int, b: int) -> str:
    """Multiplies two numbers and returns the result as a string. Use this tool only when you need to perform multiplication.
    
    Args:
        a: The first number.
        b: The second number.
    """
    return f"The product of {a} and {b} is {a * b}."


tools = [addition_calculator, multiplication_calculator]

llm_with_tools = llm.bind_tools(tools=tools)

response = llm_with_tools.invoke("What is the product of 5 and 10?")

print(response) # If you print just the response, You will see the whole details, 
# It will include the content as well as tool usage information. 
# Some times, the content will be an empty list another time the tool_calls will be empty.
print("-"*100)
print(response.content) 
print("-"*100)
print(response.tool_calls) 