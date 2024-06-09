from abc import ABC, abstractmethod
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from src.interpretation.schemas import InterpretationResult, BaseSchema

class InterpreterInterface(ABC):
    @abstractmethod
    def __init__(self, llm: BaseChatModel, schema: BaseSchema) -> None:
        self.llm = llm
        self.schema = schema
        self.prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
        ("human", "{text}"),
    ]
)
  
    @abstractmethod
    def interpret(self, content: str) -> InterpretationResult:
        pass

class ActivitiesInterpreter(InterpreterInterface):
    def __init__(self, llm, schema):
        super().__init__(self, llm, schema)

    def interpret(self, content) -> InterpretationResult:
        pass