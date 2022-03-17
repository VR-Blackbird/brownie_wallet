from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
NO_DECIMALS = 8
INITIAL_VALUE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAINS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(NO_DECIMALS, INITIAL_VALUE, {"from": get_account()})
