from scripts.tools import get_account
from brownie import KhelManch


def deploy():
    account = get_account()   
    khelManch = KhelManch.deploy({'from': account})    
    print(khelManch.address)


def main():
    deploy()