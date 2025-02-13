import pandas as pd

from datetime import datetime

from app.pkg.requestor import make_request
from app.pkg.settings import settings


async def get_courses(
    symbol: str = "BTCUSDT",
    interval: int = 15,
    dots: int = 100000
) -> dict:
    """Get course of crypto pair.

    Args:
        symbol: crypto pair.
        interval: time interval between candles.
        dots: number of candles.
    Returns:
        response from Bybit API: dict.
    """
    end = int(datetime.now().timestamp())
    start = end - interval * dots * 60
    response = await make_request(
        url=settings.BYBIT_URL,
        method="GET",
        params={
            "category": "linear",
            "interval": interval,
            "symbol": symbol,
            "start": int(start * 1e3),
            "end": int(end * 1e3),
        }
    )
    return response["result"]["list"][::-1]

async def convert_to_pandas(candles: dict) -> pd.DataFrame:
    """Convert BYBIT course api response to pandas DataFrame.

    Args:
        candles: BYBIT course api response.

    Returns:
        Dataframe: structured candles data.
    """
    return pd.DataFrame(
        data={
            "open": [float(candle[1]) for candle in candles],
            "high": [float(candle[2]) for candle in candles],
            "low": [float(candle[3]) for candle in candles],
            "close": [float(candle[4]) for candle in candles],
            "volume": [float(candle[5]) for candle in candles],
        },
        index=pd.DatetimeIndex(
            [datetime.fromtimestamp(int(candle[0]) * 1e-3) for candle in candles]
        )
    )
