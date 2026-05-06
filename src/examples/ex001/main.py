from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model("ollama:llama3.2")

response = llm.invoke("Olá, tudo bem?")

print(response)
