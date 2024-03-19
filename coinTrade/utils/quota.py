import numpy
import talib

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
def SMA(inputs, timeperiod,dimensionality=float,reduction_index=0):
    return talib.SMA(dimension_reduction(inputs, dimensionality, reduction_index), timeperiod=timeperiod)

def MA(inputs, timeperiod,dimensionality=float,reduction_index=0):
    return talib.MA(dimension_reduction(inputs, dimensionality, reduction_index), timeperiod=timeperiod)


# 数组降维
def dimension_reduction(inputs,dimensionality,reduction_index):
    if dimensionality :
        return numpy.array(inputs)[:,reduction_index]
    return inputs

