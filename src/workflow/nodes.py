from core.language_models import LanguageModels
from workflow.state import State
from langchain_core.prompts import PromptTemplate
import logging

language_models = LanguageModels()


def handle_advanced(state: State):
    """Handle the user query with the advanced language model."""
    prompt = PromptTemplate(
        template="You are running in an example program, simply pretend to handle the user query \
                 user_query: {input}",
        input_variables=[]
    )
    logging.info("Advanced model handling query.")
    routing_chain = prompt | language_models.get_advanced_llm()
    result = routing_chain.invoke({"input": state["user_query"]})
    state["result"] = result
    return state


def handle_simple(state: State):
    """Handle the user query with the simple language model."""
    logging.info("simple model handling query.")
    prompt = PromptTemplate(
        template="You are running in an example program, simply pretend to handle the user query \
                 user_query: {input}",
        input_variables=[]
    )
    routing_chain = prompt | language_models.get_simple_llm()
    result = routing_chain.invoke({"input": state["user_query"]})
    state["result"] = result
    return state


def end(state: State):
    """End the conversation."""
    logging.info(f"Conversation ended with result: {state['result'].content}")