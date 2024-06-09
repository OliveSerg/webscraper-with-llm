from abc import ABC, abstractmethod
from typing import Type
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from src.interpretation.schemas import InterpretationResult, BaseSchema, Activity, Person

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
                ("human", "{text}"),
            ]
        )
  
    @abstractmethod
    def interpret(self, content: str) -> InterpretationResult:
        pass

class ActivitiesInterpreter(InterpreterInterface):
    def __init__(self, llm, schema = None):
        if not schema:
            schema = Activity
        super().__init__(llm, schema)
        # ChatPromptTemplate would help elminate the <> but gets error
        self.prompt = PromptTemplate.from_template(
                            """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
                            You are a smart assistant take the following context and question below and return your answer in JSON.
                            <|eot_id|><|start_header_id|>user<|end_header_id|>
                            QUESTION: {question} \n
                            CONTEXT: {context} \n
                            JSON:
                            <|eot_id|>
                            <|start_header_id|>assistant<|end_header_id|>
                            """
                            )

    def interpret(self, content):
        print(content)
        runnable = self.prompt | self.llm.with_structured_output(schema=Person)
        output = runnable.invoke({"question": "What are the child friendly activities or events?","context": content})
        return output
    