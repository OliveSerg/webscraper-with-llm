from fastapi import APIRouter, HTTPException
from src.scraping import schemas, services

router = APIRouter()

@router.post('/')
def start_scraping_task(request: schemas.ScrapeRequest):
    try:
        scraped_result = services.get_results(request)
        
        return scraped_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))