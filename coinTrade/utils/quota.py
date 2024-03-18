


# 均线指标，如EMA、SMA、WMA等
# 动量指标，如MACD、MOM、RSI等
# 成交量指标，如AD、OBV等
# 易变指标，如ATR、NATR等
# 价格变换，如AVGPRICE、MEDPRICE等
# 循环指标，如HT_DCPERIOD、HT_SINE等
# 模式识别，如CDL2CROWS、CDLHAMMER等
# 统计函数，如VAR,STDDEV, LINEARREG等
# 数学变换，如ACOS、ASIN、CEIL、COS、EXP、LN、SQRT等
# 数学操作，如ADD、DIV、MAX、MULT、SUM等


# SMA：简单移动平均线(Simple Moving Average)
# talib.SMA() 要求数据是numpy.ndarray格式
# talib.abstract.SMA() 要求数据是Numpy数组的字典格式
def SMA(inputs, timeperiod, key='open'):
    return talib.SMA(inputs, timeperiod=timeperiod, price=key)