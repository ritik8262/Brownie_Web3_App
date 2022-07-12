from brownie import accounts, network, config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "mainnet-fork-dev",
    "mainnet-fork",
    "hardhat",
    "ganache-local",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[1]
    return accounts.add(config["wallets"]["from_key"])
