from abc import ABC, abstractmethod
from typing import Type
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from src.interpretation.schemas import InterpretationResult, BaseSchema, Activities

class InterpreterInterface(ABC):
    @abstractmethod
    def __init__(self, llm: BaseChatModel, schema: Type[BaseSchema]) -> None:
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
                ("human", "{context}"),
            ]
        )
  
    @abstractmethod
    def interpret(self, content: str) -> InterpretationResult:
        pass

class ActivitiesInterpreter(InterpreterInterface):
    def __init__(self, llm, schema = None):
        if not schema:
            schema = Activities
        super().__init__(llm, schema)
        
    def interpret(self, content):
        runnable = self.prompt | self.llm.with_structured_output(schema=self.schema)
        output = runnable.invoke({"context": content})
        return output
        