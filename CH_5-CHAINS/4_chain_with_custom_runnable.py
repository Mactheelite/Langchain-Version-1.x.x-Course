from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Make all your answers to be short and concise."),
    ("human", "{input}.")
    ])

parser = StrOutputParser() 



# Custom dictionary maker. The function just helps to convert the output text to dictionary with key 'text'.
def dictionary_maker(text:str) -> dict:
    """This fuction converts text to dictionary with key 'text'.""" # Docstring is very important to describe the function
    return {"text": text}

custom_dict_maker = RunnableLambda(dictionary_maker)

word = "Computers" # You can change this word to test with other words.

# This line is optional. It's just to show the converted dictionary output. {'text': '...'}
chain = RunnableSequence(prompt_template, llm, parser,custom_dict_maker)
print(chain.invoke({"input": word}))

instagram_post = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Instagram post generator. Make it short and engaging."),
    ("human", "Create short and engaging Instagram posts on the word: {text}.")
    ])

final_chain = RunnableSequence(
    prompt_template,
    llm,
    parser,
    custom_dict_maker,
    instagram_post,
    llm,
    parser
    )


response = final_chain.stream({"input" : word}) # Streaming response is good. it generates output in chunks just like ChatGPT.

for chunk in response:
    print(chunk, end="", flush=True)