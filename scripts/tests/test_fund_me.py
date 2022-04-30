from asyncio import exceptions
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me, LOCAL_BLOCKCAHIN_ENVIROMENTS
from brownie import network, accounts, exeptions
import pytest


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


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIROMENTS:
        pytest.skip("only for local testing")
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
