from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Scraping App"
    PROJECT_VERSION: str = "1.0.0"
    ALLOWED_HOSTS: list[str] = ["*"]
    DATABASE_URL: str
    MODEL_BASE_URL: str
    LLM_MODEL_NAME: str

    # Use seperate settings for LLMs to use as interface
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()