from brownie import accounts, config, SimpleStorage


def read_contract():
    # Access previously deployed contracts (-1 for the latest)
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
