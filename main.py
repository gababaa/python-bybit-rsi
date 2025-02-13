import asyncio
import logging

from app.services import rsi
from app.pkg.settings import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=settings.LOGGER_FILE,
    filemode='a'
)

async def main():
    logger.info("Start")
    while True:
        try:
            await asyncio.gather(
                *[
                    rsi.check_rsi(symbol=symbol)
                    for symbol in settings.CRYPTO_PAIRS.split(", ")
                ]
            )
        except Exception as e:
            logger.critical(e)
        finally:
            logger.info("=" * 60)
            await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
