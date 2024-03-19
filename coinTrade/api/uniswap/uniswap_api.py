#coding:utf-8

#from abis import PAIR_ABI, SYMBOL_ABI, UNISWAP_FACOTRY_ABI, pairabi, routerabi

from web3 import Web3
import requests

# 怎么过滤大单？
# 怎么过滤特定地址的交易？ 怎么查交易时间？ 怎么查交易类型？
# 为什么打印的交易在浏览器查不到？？ 但是查单个交易又可以看到


# 获取合约ABI
def fetch_abi(address):
    url = "https://api.bscscan.com/api"
    params = {
        "module": "contract",
        "action": "getabi",
        "address": address,
        "apikey": "6HQZV977GIY8FNT36XN1JJSE12IP2IYVTQ",
    }
    resp = requests.get(url, params=params).json()
    return resp["result"]


# 创建 Web3 实例
# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed3.binance.org"))
# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed4.binance.org"))
# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed3.defibit.io/"))
# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed4.ninicoin.io/"))
# web3 = Web3(Web3.HTTPProvider("https://bsc-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3"))
# web3 = Web3(Web3.HTTPProvider("https://1rpc.io/bnb"))
web3 = Web3(Web3.HTTPProvider("https://bsc-pokt.nodies.app"))


# Uniswap V2 Pair 合约地址 19380273
# pair_contract_address = '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'  # 替换为你要监听的 Uniswap V2 Pair 合约地址

# pancake 合约地址  36748422
# pair_contract_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'  # 替换为你要监听的 Uniswap V2 Pair 合约地址
# 最后两个网址可以查询到这个信息，这个接口没有关闭，但是其他的公开节点不行
# 另外，上面这个合约地址没有交易信息，所以没有打印，下面这个 usdc 的就很活跃
pair_contract_address = '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'  # 替换为你要监听的 Uniswap V2 Pair 合约地址

# pair_contract_abi = pairabi
pair_contract_abi = fetch_abi(pair_contract_address)
# 这个只能用来获取bsc的合约abi,其他的合约abi获取就会报错

# 创建合约实例
pair_contract = web3.eth.contract(address=pair_contract_address, abi=pair_contract_abi)

# 获取 Swap 事件的 topic
swap_event_topic = web3.keccak(text='Swap(address,address,uint256,uint256,uint256,uint256,address)').hex()

# 获取当前区块高度
block_number = web3.eth.block_number
print(block_number)



# 监听事件
def handle_event(event):
    # 解析 Swap 事件的参数
    print('event ', event)

    txhash2 = event['transactionHash'].hex()
    print('txhash ', txhash2)

    log = web3.eth.get_transaction(txhash2)
    print('tx-log ', log)

    print('----------------------')