import requests
from src.scraping import  schemas
    
def get_results(scrape_request: schemas.ScrapeRequest) -> str:   
    response = requests.get('https://r.jina.ai/'+scrape_request.url)
    
    return response.text
    