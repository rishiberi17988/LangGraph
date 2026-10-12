# LangGraph Basics

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?logo=langchain&logoColor=white)

A hands-on learning repository for exploring **LangGraph fundamentals** and building stateful LLM workflows through graphs, conditional routing, loops, chatbots, persistence, and tool integration.

## Topics Covered

### 1. Graph Workflows
- **Sequential workflows** — execute nodes in a defined order.
- **Parallel workflows** — run independent tasks in parallel.
- **Conditional workflows** — route execution based on conditions.
- **Loops** — repeat graph steps when needed.

### 2. Chatbots and State
- Build a simple chatbot using LangGraph.
- Manage conversation state across graph nodes.
- Persist conversation state with checkpoints.

### 3. Tools and Chatbot Interface
- Connect tools to an LLM workflow.
- Build a LangGraph chatbot backend.
- Connect the backend to a Streamlit frontend.
- Explore streaming responses and threaded interactions.

## Project Structure

```text
LangGraph/
├── 1_sequential.ipynb
├── 2_parallel.ipynb
├── 3_conditional.ipynb
├── 4_loop.ipynb
├── 5_simplechatbot.ipynb
├── 6_persistence.ipynb
├── 7_tools.ipynb
├── simple.py
├── codes/
│   ├── langgraph_backend.py
│   ├── langgraph_tool_backend.py
│   ├── streamlit_frontend.py
│   ├── streamlit_frontend_streaming.py
│   ├── streamlit_frontend_threading.py
│   └── streamlit_frontend_tool.py
├── requirements.txt
└── LICENSE
```

## Learning Outcomes

- Represent workflows as graphs with nodes and edges.
- Use shared state to pass information between graph steps.
- Control execution with sequential, parallel, conditional, and looping workflows.
- Build conversational applications with LangGraph.
- Preserve conversation state using persistence and checkpoints.
- Integrate tools into LLM-powered workflows.
- Connect a LangGraph backend to a Streamlit interface and explore streaming responses.
