from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str
    mongodb_database: str = "vanmitra_government_dev"
    jwt_secret: str
    jwt_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173"
    model_config = {"env_file": ".env", "extra": "ignore"}

settings = Settings()
