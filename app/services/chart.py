import asyncio
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from app.services import parser


async def draw_rsi_chart(data: pd.DataFrame, symbol: str):
    plt.plot(
        data.index, data.RSI, marker='', label='RSI'
    )
    plt.plot(
        data.index, [70] * len(data), marker='', label='Overbought'
    )
    plt.plot(
        data.index, [30] * len(data), marker='', label='Oversold'
    )

    plt.title('RSI')
    plt.xlabel('Time')
    plt.ylabel('PERCENT')
    plt.grid()
    plt.legend()
    now = datetime.now()
    now = now.replace(minute=now.minute // 15 * 15, second=0)
    now_str = now.strftime('%Y-%m-%d:%H-%M')
    plt.savefig(
        f'charts/{symbol}-{now_str}.png',
        dpi=300,
        bbox_inches='tight'
    )
    plt.close()


# async def draw_chart(data: pd.DataFrame, symbol: str):
#     plt.plot(
#         data.index, data.high, marker='', label='High'
#     )
#     plt.plot(
#         data.index, data.low, marker='', label='Low'
#     )
#
#     plt.title('BTCUSDT')
#     plt.xlabel('Time')
#     plt.ylabel('USDT')
#     plt.grid()
#     plt.legend()
#     plt.savefig(f'charts/{symbol}.png', dpi=300, bbox_inches='tight')
#     plt.close()
