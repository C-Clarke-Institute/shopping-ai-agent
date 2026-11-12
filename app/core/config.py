from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Setting(BaseSettings):

    database_url : str
    openai_api_key : str
    openai_model : str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR/".env",
        extra="ignore"
    )

settings = Setting()

