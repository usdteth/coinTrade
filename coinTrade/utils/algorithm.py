import numpy as np
import talib
from talib.abstract import *

close = np.random.random(100)
output = talib.SMA(close) # 默认是SMA30
output = talib.SMA(close, timeperiod=5) # SMA5

inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}
from talib.abstract import *
output = talib.SMA(inputs, timeperiod=25) # 默认对close价格计算
output = talib.SMA(inputs, timeperiod=25, price='open') # 对open价格计算