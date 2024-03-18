# import numpy as np
# import talib
from talib.abstract import *

import numpy as np
# from ta.momentum import rsi
from talib import abstract

# 创建一个二维数组
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [5, 6, 7, 8],
                 [5, 6, 7, 8],
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12]])

# 设置时间窗口大小，对应于RSI指标的时间窗口
timeperiod = 3

# 使用TA-Lib的abstract函数计算RSI指标
rsi_result = abstract.RSI(data, timeperiod=timeperiod)

print(rsi_result)

