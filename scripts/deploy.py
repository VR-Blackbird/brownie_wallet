"""
Module used to deploy the smart contracts
"""

from brownie import wallet, config, network, MockV3Aggregator
from scripts.misk import get_account, deploy_mocks, LOCAL_BLOCKCHAINS


def deployment():
    """
    Function used to Deploying the contacts
    """
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    wallet.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )


def main():
    """
    Main program used by brownie.
    """
    deployment()
