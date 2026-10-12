from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-120b")
print(model.invoke('How far is moon from the earth? in 10 words').content)