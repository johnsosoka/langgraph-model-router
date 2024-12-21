from langchain_core.messages import BaseMessage
from typing import TypedDict, Annotated


class State(TypedDict):
    """Represents the State for the graph. This is passed between the nodes & router"""
    # The sequence of messages exchanged in the conversation
    user_query: str
    # Annotated is required when branching
    result: Annotated[BaseMessage, "result"]
