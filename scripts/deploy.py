from scripts.tools import get_account
from brownie import KhelManch, Admin


def deploy():
    account = get_account()
    khelManch = KhelManch.deploy({'from': account})
    print(khelManch.address)
    admin = Admin.deploy(khelManch.address, {"from": account})
    admin_change_tx = khelManch.setOwner(admin.address, {"from": account})
    admin_change_tx.wait(1)
    print(admin.address)


def main():
    deploy()
