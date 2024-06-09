from pydantic import BaseModel
from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel as LangBaseModel, Field

class InterpretationResult(BaseModel):
    json_result: List[str]
    summary: str

# This should have base schema properties. Can be split into multiple types of schemas
class BaseSchema(LangBaseModel):
    pass

class Activity(BaseSchema):
    """Information about an activity."""
    name: Optional[str] = Field(default=None, description="The name of the activity")
    summary: Optional[str] = Field(default=None, description="A summary about the activity")
    child_safe: Optional[bool] = Field(default=None, description="Is the activity safe for a child under 8 years old")
    