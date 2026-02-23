# Run this file to see your results in the terminal
# python question_field.py 

from rag_chain import build_rag_chain

rag_chain = build_rag_chain()

question = "Who is the CEO of Tesla Inc?"  # Example question; replace with your own question as needed

response = rag_chain.invoke(question)

print("Answer:\n", response)