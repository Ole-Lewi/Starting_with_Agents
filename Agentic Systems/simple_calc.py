from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.tools import Tool

import math

def calculator_tool(query: str) -> str:
    try:
        result = eval(query)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for when you need to calculate something."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=ChatGroq(model="llama3-70b-8192"),
    agent="zero-shot-react-description",
    verbose=True
)
query = "What is the square root of 16 plus 5?"
response = agent.run(query)