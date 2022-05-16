from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()

    # Delpoy contract
    simple_storage = SimpleStorage.deploy({"from": account})
    # Retrieve initial value
    stored_value = simple_storage.retrieve()
    # Store a value
    txn = simple_storage.store(20, ({"from": account}))
    txn.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# Checks chain and grabs account accordingly
def get_account():
    # 1. Get first account from all the accounts in ganache
    # account = accounts[0]
    # 2. Get metamask account (Safest method)
    # account = accounts.load("test-account")
    # 3. Env variable
    # account = accounts.add(config["wallets"]["from_key"])
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
