from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
SATRT_PRICE = 2000  # * (10**8)
LOCAL_BLOCKCAHIN_ENVIROMENTS = ["development", "ganache-local"]
FORK_LOCAL_ENVIROMENT = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCAHIN_ENVIROMENTS
        or network.show_active() in FORK_LOCAL_ENVIROMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(SATRT_PRICE, "ether"),
            {"from": get_account()},  # Web3.toWei(SATRT_PRICE, "ether")
        )
