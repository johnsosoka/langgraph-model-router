from langchain.output_parsers import EnumOutputParser
from langchain_core.prompts import PromptTemplate
from core.language_models import LanguageModels
from workflow.routing_options import RoutingOptions
from workflow.state import State
import logging

language_models = LanguageModels()


# This is the Conditional Edge
def query_router(state: State):
    """Determine if the user query should be routed to the advanced or simple language model."""
    logging.info("Determining where to route the user query.")
    parser = EnumOutputParser(enum=RoutingOptions)

    # TODO - Utilize create_structured_output_runnable to avoid hard coding valid outputs
    prompt = PromptTemplate(
        template="Determine if the user query requires a simple or advanced model. An 'advanced' request might require \
        multiple steps like retrieving an order ID and looking up shipping information, whereas a 'simple' request can \
        handle more straightforward queries. return either 'simple' or 'advanced'. Do not explain your reasoning Your \
        only task is to determine where to route the user query. \
        user_query: {input}",
        input_variables=["input"]
    )

    routing_chain = prompt | language_models.get_router_llm() | parser
    result = routing_chain.invoke({"input": state["user_query"]})
    logging.info(f"Query Router Determined Model: {result.value}")
    return result.value
