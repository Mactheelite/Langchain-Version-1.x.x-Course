# make sure to install tavily before running this example:
# pip install tavily-python or uv add tavily-python
# Generate api key from https://tavily.com and set it in your .env file as TAVILY_API_KEY

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.tools import tool
from tavily import TavilyClient
import os
from typing import Literal

load_dotenv()

llm = init_chat_model(model="gpt-4o", temperature=0)

if os.environ.get("TAVILY_API_KEY") is None:
    raise ValueError("TAVILY_API_KEY environment variable not set.")

tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY")) # make sure to set TAVILY_API_KEY in your .env file

# Defining a basic tool using the @tool decorator
@tool(description="A tool to perform internet search for a given query.")
def internet_search(
    query:str,
    max_results: int = 3,
    topic: Literal["general", "news"] = "news",
    include_raw_content: bool = False
    ):
    """General purpose internet search tool. Always use this tool when you need to search something on the internet.
    
    Args:
        query: The search query.
        max_results: The maximum number of results to return.
        topic: The topic of the search, either 'general' or 'news'.
        include_raw_content: Whether to include the raw content of the search results."""
    results = tavily_client.search(
        query=query,
        max_results=max_results,
        topic=topic,
        include_raw_content=include_raw_content,
        include_answer=True
    )
    return results


def beautify_and_display_best(search_results: dict) -> str:
    """Extracts the answer from Tavily search results and provide the exact answer verbatim.
    
    Args:
        search_results: Dictionary containing Tavily API search results
    
    Returns:
        The answer field from Tavily API response
    """
    answer = search_results.get('answer')
    
    if not answer:
        return "No answer found."
    
    return answer


tools = [internet_search]

llm_with_tools = llm.bind_tools(tools, tool_choice="internet_search")

question = [{"role": "user", "content": "What is the capital of France?"}]

response = llm_with_tools.invoke(question)


if response.tool_calls:
    for tool_call in response.tool_calls:
        print(f"Tool used: {tool_call['name']}")
        print(f"With arguments: {tool_call['args']}\n")
        
        result = internet_search.invoke(tool_call['args'])
        
        answer = beautify_and_display_best(result)
        print(f"Answer:\n{'-'*70}\n{answer}\n{'-'*70}")
else:
    print(response.content) # If the model doesn't use any tool, it will return a general response.