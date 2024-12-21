from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from config.config_loader import load_config


class LanguageModels:
    """
    This class manages our three model types.
    1. router_llm - Tasked with determining which model to route the user query to.
    2. simple_llm - The cheaper/Simpler model, for handling less complex tasks
    3. advanced_llm - The more expensive model, tasked with handling complex tasks

    Note: As this project is only an example, it always assumes Anthropic for router & Advanced, while using OpenAI for
    the simple model.

    If this needs to change for your uses, ensure to initialize them differently, or re-implement with a more dynamic
    LLM initialization method.
    """

    def __init__(self):
        """Initialize the language models"""
        self.config = load_config()

        self.router_llm = ChatAnthropic(
            api_key=self.config["api_keys"]["anthropic"],
            model=self.config["models"]["evaluator"]
        )

        self.advanced_llm = ChatAnthropic(
            api_key=self.config["api_keys"]["anthropic"],
            model=self.config["models"]["advanced"]
        )

        self.simple_llm = ChatOpenAI(
            api_key=self.config["api_keys"]["open_ai"],
            model=self.config["models"]["simple"]
        )

    def get_router_llm(self):
        return self.router_llm

    def get_advanced_llm(self):
        return self.advanced_llm

    def get_simple_llm(self):
        return self.simple_llm
