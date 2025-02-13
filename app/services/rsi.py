import talib
import logging
import pandas as pd

from decimal import Decimal

from app.services import parser, chart
from app.pkg import telegram_bot
from app.pkg.settings import settings

logger = logging.getLogger(__name__)

async def count_rsi(pd_candles: pd.DataFrame) -> pd.DataFrame:
    pd_candles["RSI"] = talib.RSI(pd_candles.close, 14)
    return pd_candles


async def check_rsi(symbol: str):
    candles = await parser.get_courses(symbol=symbol)
    pd_candles = await parser.convert_to_pandas(candles=candles)
    pd_candles_rsi = await count_rsi(pd_candles=pd_candles)
    logger.info(f"{symbol}: RSI - {pd_candles_rsi.iloc[-1].RSI}")

    if Decimal(str(pd_candles_rsi.iloc[-1].RSI)) < Decimal(settings.RSI_MIN):
        trend_message = f"BUY! {symbol}"
        await build_telegram_message(data=pd_candles_rsi, message=trend_message, symbol=symbol)
        return

    if Decimal(str(pd_candles_rsi.iloc[-1].RSI)) > Decimal(settings.RSI_MAX):
        trend_message = f"SELL! {symbol}"
        await build_telegram_message(data=pd_candles_rsi, message=trend_message, symbol=symbol)
        return

    logger.info(f"Skip iteration {symbol}")

async def build_telegram_message(
    data: pd.DataFrame,
    message: str,
    symbol: str,
):
    # logger.info("Draw RSI chart")
    # await chart.draw_rsi_chart(data=data, symbol=symbol)
    logger.info("Send message to telegram")
    await telegram_bot.send_telegram_message(
        message=message
    )
