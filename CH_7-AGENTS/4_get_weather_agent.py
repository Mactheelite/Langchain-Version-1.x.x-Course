from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.tools import tool
import requests

load_dotenv()

@tool("get_weather",description="Return weather information for a given city.", return_direct=False)
def get_weather(city: str) -> str:
    """Get the weather for a city.
    
    Args:
        city: The name of the city.
    """
    response = requests.get(f"http://wttr.in/{city}?format=j1") # This is a free weather API that returns weather information in JSON format. You can replace this with any other weather API of your choice.
    if response.status_code == 200:
        data = response.json()
        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']
        temp_f = current_condition['temp_F']
        return f"The weather in {city} is {weather_desc} with a temperature of {temp_c}°C ({temp_f}°F)."
    else:
        return f"Could not retrieve weather information for {city}."
    

agent = create_agent(
    model="gpt-4.1-mini",
    tools=[get_weather],
    system_prompt="""You are a helpful weather assistant who always cracks jokes and is humorous while remaining helpful""",
)


response = agent.invoke(
    {"messages": [
                   {"role": "user", "content": "What is the weather in Lagos, Nigeria?"}
                 ]
        })

print(response)
print("\n", "=" *110 , "\n")
print(response["messages"][-1].content) # This will print the actual and real-time weather information for Lagos Nigeria.