
from langgraph.graph import StateGraph,START
from langgraph.prebuilt import ToolNode, tools_condition

from app.agent.nodes.assistant import assistant_node, tools
from app.agent.state import OrderAgentState

#create the graph builder
builder = StateGraph(OrderAgentState)

#register nodes
builder.add_node("assistant", assistant_node)
builder.add_node("tools",ToolNode(tools))


#define the starting point
builder.add_edge(START,"assistant")

#conditional routing
builder.add_conditional_edges("assistant",tools_condition)

#return to assistant after tool execution
builder.add_edge("tools", "assistant")

order_graph = builder.compile()