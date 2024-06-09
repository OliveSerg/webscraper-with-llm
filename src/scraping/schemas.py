from pydantic import BaseModel
from typing import List, Optional

class ScrapeRequest(BaseModel):
    url: str
    keywords: List[str]

class ScrapeTaskResponse(BaseModel):
    task_id: int
    status: str

class ScrapeTaskStatus(BaseModel):
    task_id: int
    status: str
    progress: Optional[str] = None

class ScrapeResult(BaseModel):
    title: str
    url: str
    summary: str
    keywords_found: List[str]