import okx.trade as Trade
import okx.account as Account
import okx.market as Market

def get_account(apikey,secretkey,passphrase,flag):
   return Account.Account(key=apikey, secret=secretkey, passphrase=passphrase, flag=flag)

def get_trade(apikey,secretkey,passphrase,flag):
   return Trade.Trade(key=apikey, secret=secretkey, passphrase=passphrase, flag=flag)


def use_order(instId, clOrdId,side , sz , trade):
    if side == 'buy':
       return order_buy(instId, clOrdId,side , sz , trade)
    else:
      return  order_sell(instId, clOrdId, side, sz, trade)

#  下单，以市价立马成交 多单
def order_buy(instId, clOrdId,side , sz , trade):
    return trade.set_order(
        instId=instId,
        tdMode="cash",
        clOrdId=clOrdId,
        side=side,
        ordType='market',
        sz=sz
    )

#  下单，以市价立马成交 空单
def order_sell(instId, clOrdId,side , sz  , trade):
    return trade.set_order(
        instId=instId,
        tdMode='isolated',
        clOrdId=clOrdId,
        side=side,
        ccy='USDT',
        ordType='market',
        sz=sz,
    )
#

#   Parameter         	Type    	Required	Description
#         lever             	String  	是       	杠杆倍数
#         mgnMode           	String  	是       	保证金模式isolated：逐仓cross：全仓如果ccy有效传值，该参数值只能为cross。
#         instId            	String  	可选      	产品ID：币对、合约instId和ccy至少要传一个；如果两个都传，默认使用instId
#         ccy               	String  	可选      	保证金币种仅适用于跨币种保证金模式的全仓币币杠杆。设置自动借币的杠杆倍数时必填
#         posSide           	String  	可选      	持仓方向long：双向持仓多头short：双向持仓空头仅适用于逐仓交割/永续在双向持仓且保证金模式为逐仓条件下必填
#         '''

def set_leverage(instId,lever,posSide,account):
     return  account.set_leverage(lever,"isolated",instId,'',posSide)

def wallet_transfer(instId,sz,addres):
    print("钱包转账")

