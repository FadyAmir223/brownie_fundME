from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
from brownie import accounts


def test_fund_and_withdraw():
    account = get_account()
    smart_contract = deploy_fund_me()
    entrance_fee = smart_contract.getEntranceFee()
    tx = smart_contract.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert smart_contract.addressToAmountFunded[account.address] == entrance_fee
    tx2 = smart_contract.withdraw({"from": account})
    tx2.wait(1)
    assert smart_contract.addressToAmountFunded[account.address] == 0
