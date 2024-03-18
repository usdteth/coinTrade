import okx.market as Market

# get_tickers = ['/api/v5/market/tickers', 'GET']  # 获取所有产品行情信息
# get_ticker = ['/api/v5/market/ticker', 'GET']  # 获取单个产品行情信息
# get_index_tickers = ['/api/v5/market/index-tickers', 'GET']  # 获取指数行情
# get_books = ['/api/v5/market/books', 'GET']  # 获取产品深度
# get_books_lite = ['/api/v5/market/books-lite', 'GET']  # 获取产品轻量深度
# get_candles = ['/api/v5/market/candles', 'GET']  # 获取交易产品K线数据
# get_history_candles = ['/api/v5/market/history-candles', 'GET']  # 获取交易产品历史K线数据
# get_index_candles = ['/api/v5/market/index-candles', 'GET']  # 获取指数K线数据
# get_history_index_candles = ['/api/v5/market/history-index-candles', 'GET']  # 获取指数历史K线数据
# get_mark_price_candles = ['/api/v5/market/mark-price-candles', 'GET']  # 获取标记价格K线数据
# get_history_mark_price_candles = ['/api/v5/market/history-mark-price-candles', 'GET']  # 获取标记价格历史K线数据
# get_trades = ['/api/v5/market/trades', 'GET']  # 获取交易产品公共成交数据
# get_history_trades = ['/api/v5/market/history-trades', 'GET']  # 获取交易产品公共历史成交数据
# get_instrument_family_trades = ['/api/v5/market/option/instrument-family-trades', 'GET']  # 获取期权品种公共成交数据
# get_platform_24_volume = ['/api/v5/market/platform-24-volume', 'GET']  # 获取平台24小时总成交量
# get_open_oracle = ['/api/v5/market/open-oracle', 'GET']  # Oracle  上链交易数据
# get_exchange_rate = ['/api/v5/market/exchange-rate', 'GET']  # 获取法币汇率
# get_index_components = ['/api/v5/market/index-components', 'GET']  # 获取指数成分数据
# get_block_tickers = ['/api/v5/market/block-tickers', 'GET']  # 获取大宗交易所有产品行情信息
# get_block_ticker = ['/api/v5/market/block-ticker', 'GET']  # 获取大宗交易单个产品行情信息
# get_block_trades = ['/api/v5/market/block-trades', 'GET']  # 获取大宗交易公共成交数据




def get_candles(instId,bar, after: str = '', before: str = '', limit: str = ''):
   return Market.Market().get_candles(instId, bar, after, before, limit)["data"]

def get_tickers():
   return Market.Market().get_tickers(instType="SPOT")["data"]
