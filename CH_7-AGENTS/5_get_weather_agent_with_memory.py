from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.tools import tool, ToolRuntime
import requests
from langgraph.checkpoint.memory import InMemorySaver
from dataclasses import dataclass

load_dotenv()

@dataclass
class Context:
    user_id: str

@dataclass
class ResponseFormat:
    summary: str
    temperature: float
    temperature_fahrenheit: float
    humidity: float

@tool("get_weather",description="Return weather information for a given city.", return_direct=False)
def get_weather(city: str) -> str:
    """Get the weather for a city.
    
    Args:
        city: The name of the city.
    """
    response = requests.get(f"http://wttr.in/{city}?format=j1") # This is a free weather endpoint that returns weather information in JSON format. You can replace this with any other weather API of your choice.
    if response.status_code == 200:
        return response.json()
    else:
        return f"Could not retrieve weather information for {city}."
    
@tool("locate_user", description="Look up user's city based on the context")
def locate_user(runtime: ToolRuntime[Context]):
    match runtime.context.user_id:
        case "user_123":
            return "Lagos, Nigeria"
        case "user_456":
            return "Abuja, Nigeria"
        case _:
            return "Unknown location"
        
model = init_chat_model("gpt-4.1-mini" , temperature=0.4)

tools = [get_weather, locate_user]
checkpointer = InMemorySaver()
    
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""You are a helpful weather assistant who always cracks jokes and is humorous while remaining helpful""",
    context_schema=Context,
    response_format=ResponseFormat,
    checkpointer=checkpointer
)

config = {"configurable": {"thread_id": 1}}

ai_response = agent.invoke(
    {
        "messages": [
                   {"role": "user", "content": "What is the weather in my location?"}
                 ] ,
       
        }, 
        config=config,
        context=Context(user_id="user_456") # Change the user_id to "user_123" or "user_456" to get weather information for Lagos or Abuja respectively. For any other user_id, it will return "Unknown location".
        )


print(ai_response["structured_response"].summary) # This will print the summary of the weather information based on the user_id.


# I can ask a follow up question and the AI will remember that i am refering to the city with the same id above

ai_response = agent.invoke(
    {
        "messages": [
                   {"role": "user", "content": "And is that usual?"}
                 ] ,
       
        }, 
        config=config,
        context=Context(user_id="user_456") # Change the user_id to "user_123" or "user_456" to get weather information for Lagos or Abuja respectively. For any other user_id, it will return "Unknown location".
        )

print("\n=== All Messages ===")
print(ai_response["structured_response"].summary)