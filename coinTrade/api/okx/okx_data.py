import okx.market as Market


def get_tickers():
   d = Market.Market().get_tickers(instType="SPOT")
   return d["data"]
