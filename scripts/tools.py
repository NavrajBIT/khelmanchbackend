from brownie import accounts, network, config

LOCAL_BLOCKCHAIN = ["development"]


def get_account(index=None):
    if index:
        account = accounts[index]
    else:        
        account = accounts[0]
    # else:
    #     account = accounts.add(config["wallets"]["from_key"])
    return account