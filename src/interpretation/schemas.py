from pydantic import BaseModel, Field
from typing import List, Optional

class InterpretationResult(BaseModel):
    json: List[str]
    summary: str

# This should have base schema properties. Can be split into multiple types of schemas
class BaseSchema(BaseModel):
    pass

class Activity(BaseSchema):
    name: Optional[str] = Field(default=None, description="The name of the activity")
    summary: Optional[str] = Field(default=None, description="Summary of the activity")
    child_safe: Optional[bool] = Field(default=None, description="Is the activity safe for a child under 8 years old")