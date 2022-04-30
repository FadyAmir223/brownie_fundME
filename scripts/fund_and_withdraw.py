from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entrance_fee = fundMe.getEntranceFee()
    print(entrance_fee)
    fundMe.fund({"from": account, "value": entrance_fee})


def withdraw():
    fundMe = FundMe[-1]
    account = get_account()
    fundMe.withdraw({"from": account})


def main():
    fund()
    withdraw()
