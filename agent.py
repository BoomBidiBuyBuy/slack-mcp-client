"""
Example of a custom LangGraph graph with MCP tools.
"""
import asyncio
import json
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langchain_core.messages import AIMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver

from langchain_openai import ChatOpenAI


def build_agent():
    """
    Builds an OpenAI-based agent using the LangChain framework,
    integrated with MCP servers listed in the `mcp-servers.json` file.

    The agent uses an in-memory saver to retain the history
    of the conversation during runtime.
    """

    def load_mcp_servers_json():
        with open("mcp-servers.json") as f:
            return json.load(f)

    llm = ChatOpenAI(
        temperature=0,
        streaming=False,
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=os.environ.get("OPENAI_API_KEY", None)
    )

    mcp_servers = load_mcp_servers_json() 

    client = MultiServerMCPClient(mcp_servers['mcpServers'])

    # get tools
    tools = asyncio.run(client.get_tools())

    def call_model(state: MessagesState):
        response = llm.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}

    checkpointer = InMemorySaver()
    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")

    return builder.compile(checkpointer=checkpointer)
