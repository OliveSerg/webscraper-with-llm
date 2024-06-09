import requests
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_community.chat_models import ChatOllama
from src.scraping import  schemas
from src.interpretation.interpreters import ActivitiesInterpreter
from src.config import settings
    
def get_results(scrape_request: schemas.ScrapeRequest) -> str:   
    llm = OllamaFunctions(base_url=settings.MODEL_BASE_URL, model="llama3", format="json", temperature=0)
    interpreter = ActivitiesInterpreter(llm=llm)
    response = requests.get('https://r.jina.ai/'+scrape_request.url)
    return interpreter.interpret(response.text)
    