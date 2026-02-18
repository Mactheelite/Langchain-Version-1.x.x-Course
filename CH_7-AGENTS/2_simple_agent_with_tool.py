# from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool

# Normally an agent would have tools to call, but for this simple example we will create an agent without any tools to demonstrate the basic setup.
load_dotenv()

# llm = init_chat_model(model="gpt-5-nano", temperature=0)

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

@tool
def get_weather(city: str) -> str:
    """Get the weather for a city.
    
    Args:
        city: The name of the city.
    """
    
    return f"The weather in {city} is shady"



agent = create_agent(
    model="gpt-5-nano",
    tools=[addition_calculator, multiplication_calculator, get_weather],
    system_prompt="""You are a helpful assistant. Answer the user's question to the best of your ability. 
    Use tools where necessary to provide accurate and complete answers. If the user asks for a calculation, use the appropriate calculator tool. 
    If the user asks for weather information, use the get_weather tool.""",
)

response = agent.invoke(
    {"messages": [
                   {"role": "user", "content": "What is the weather in Lagos, Nigeria?"}
                 ]
        })

print(response["messages"][-1].content) # The response is a list of messages, and we print the content of the last message which is the agent's response.