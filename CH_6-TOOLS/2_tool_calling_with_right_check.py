# Basic tool definition

# The simplest way to create a tool is with the @tool decorator. 
# By default, the function’s docstring becomes the tool’s description that helps the model understand when to use it.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
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

message = [{"role": "user", "content": "What is the capital of France?"}]

response = llm_with_tools.invoke(message)


if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call["name"] == "multiplication_calculator":
            name = tool_call["name"]
            args = tool_call["args"]
            
            result = multiplication_calculator.invoke(args)
            print(f"Tool used: {name}, Result: {result}")
        elif tool_call["name"] == "addition_calculator":
             name = tool_call["name"]
             args = tool_call["args"]

             result = addition_calculator.invoke(args)
             print(f"Tool used: {name}, Result: {result}")
        else:
            print("No recognized tool was used.")
else:
    print(response.content)