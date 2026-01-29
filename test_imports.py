"""Test script to verify all imports work correctly across the project."""

print("Testing all imports used in the project...\n")

# CH_1 imports
print("CH_1-LLM_CALLS imports:")
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
print("  ✓ langchain_openai.ChatOpenAI")
print("  ✓ dotenv.load_dotenv")
print("  ✓ os")

# CH_2 imports
print("\nCH_2-MESSAGES imports:")
from langchain_core.messages import HumanMessage, SystemMessage
print("  ✓ langchain_core.messages.HumanMessage")
print("  ✓ langchain_core.messages.SystemMessage")

# CH_3 imports
print("\nCH_3-PROMT_TEMPLATES imports:")
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
print("  ✓ langchain_core.prompts.PromptTemplate")
print("  ✓ langchain_core.prompts.ChatPromptTemplate")

# CH_4 imports
print("\nCH_4 imports:")
from pydantic import BaseModel
from typing import TypedDict
print("  ✓ pydantic.BaseModel")
print("  ✓ typing.TypedDict")

# CH_5 imports
print("\nCH_5 imports:")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, Runnable
from langchain.chat_models import init_chat_model
print("  ✓ langchain_core.output_parsers.StrOutputParser")
print("  ✓ langchain_core.runnables.RunnableSequence")
print("  ✓ langchain_core.runnables.RunnableParallel")
print("  ✓ langchain_core.runnables.Runnable")
print("  ✓ langchain.chat_models.init_chat_model")

print("\n" + "="*50)
print("✅ All imports successful! Project is ready to use.")
print("="*50)
