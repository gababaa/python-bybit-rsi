from decimal import Decimal

from dotenv import dotenv_values
from pydantic import BaseModel


class Settings(BaseModel):
    BYBIT_URL: str
    RSI_MIN: Decimal
    RSI_MAX: Decimal
    TELEGRAM_TOKEN: str
    TELEGRAM_CHAT_ID: str
    CRYPTO_PAIRS: str
    LOGGER_FILE: str


settings = Settings(
    **dotenv_values(".env")
)