from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableLambda, RunnableParallel


load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")



llm = ChatOpenAI(model="gpt-5-nano", temperature=0,streaming=True)

# This prompt is to search about any topic on the internet and summarize the findings in brief.
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Make a search about {input} on the internet and summarize the findings in brief."),
    ("human", "{input}.")
    ])

parser = StrOutputParser() 


def dictionary_maker(text: str) -> dict:
    """This fuction converts text to dictionary with key 'text'.""" 
    return {"text": text}

custom_dict_maker = RunnableLambda(dictionary_maker)

instagram_post = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Instagram post generator. just one."),
    ("human", "Create short and engaging Instagram posts on the word: {text}.")
    ])

instagram_chain = RunnableSequence(
    instagram_post,
    llm,
    parser
    )

def twitter_post_maker(text: dict):
    """This function is to make an twitter post from 'text'."""
    twitter_text = text['text']
    twitter_post = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful twitter post generator. just one."),
    ("human", "Create short and engaging twitter posts on the word: {text}.")
    ])
    twitter_chain = RunnableSequence(
        twitter_post,
        llm,
        parser
        )
    result = twitter_chain.invoke({"text": twitter_text})
    return result

twitter_post_maker_runnable = RunnableLambda(twitter_post_maker)


parallel_chain = RunnableParallel({"instagram_post": instagram_chain,
                                  "twitter_post": twitter_post_maker_runnable
                                  })

final_chain = RunnableSequence(prompt_template, llm, parser, custom_dict_maker, parallel_chain)


user_input = input("Enter a name or topic: ")

response = final_chain.invoke({"input" : user_input}) 

print("Instagram Post:")
print(response["instagram_post"])
print("\nTwitter Post:")
print(response["twitter_post"])