from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mock,
    LOCAL_BLOCKCAHIN_ENVIROMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address
    fundMe = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fundMe.address}")
    return fundMe


def main():
    deploy_fund_me()
