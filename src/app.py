import logging
from workflow.graph import graph
from workflow.state import State

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
# Silence httpx logging
logging.getLogger("httpx").setLevel(logging.ERROR)


def handle_query(user_query: str, description: str):
    """
    Handles routing of a query to the graph with the given state.
    """
    logging.info(description)
    state: State = {"user_query": user_query}
    graph.invoke(state)


if __name__ == "__main__":
    # Advanced routing request
    advanced_message = (
        "Please ensure that product ID 18235 has inventory and doesn't have any "
        "availability overrides set. If there are no overrides set, and inventory is zero, "
        "please order a new batch."
    )
    handle_query(
        advanced_message,
        "The first query should route to the advanced model."
    )

    # Simple routing request
    simple_message = "Does product ID 1234 come in red?"
    handle_query(
        simple_message,
        "The second query should route to the simple model."
    )
