from langgraph.graph import START, END, StateGraph
from workflow.nodes import handle_advanced, handle_simple, end
from workflow.routers import query_router
from workflow.state import State

# Create a new StateGraph
workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("handle_advanced", handle_advanced)
workflow.add_node("handle_simple", handle_simple)
workflow.add_node("review", end)

# Set the entry point
# (This entrypoint is ALSO a conditional edge)
workflow.add_conditional_edges(START,
                               query_router,
                               {
                                   "advanced": "handle_advanced",
                                   "simple": "handle_simple"
                               }
                               )

# Join the branches to the review node & END
workflow.add_edge("handle_advanced", "review")
workflow.add_edge("handle_simple", "review")
workflow.add_edge("review", END)

# Compile the graph
graph = workflow.compile()
