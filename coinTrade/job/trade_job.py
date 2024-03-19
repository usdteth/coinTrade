import numpy

from coinTrade.api.okx.okx_data import *
from coinTrade.utils.quota import SMA


def get_day(instId):
    data = get_candles(instId, "1d",limit=32)
    dt = numpy.ndarray(data)
    a = SMA(numpy.ndarray(data),5)
    print(a)


def run_trade():
    print("自动化交易")
    # 交易币种
    coin_code = "BTC"
#    获取数据
#     data = get_candles("BTC-USDT","1m")
    d = get_day("BTC-USDT")
    # data = get_block_trades()
    print(data)

