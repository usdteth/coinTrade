from coinTrade.api.okx.okx_data import get_candles


def run_trade():
    print("自动化交易")
    # 交易币种
    coin_code = "BTC"
#    获取数据
    data = get_candles("BTC-USDT","1m")
    print(data)

