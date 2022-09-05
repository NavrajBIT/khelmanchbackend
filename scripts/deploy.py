from scripts.tools import get_account
from brownie import Admin, KhelManch, PlatformLogin


def deploy():
    account = get_account()
    platformLogin = PlatformLogin.deploy({"from": account})
    khelManch = KhelManch.deploy({'from': account})
    admin = Admin.deploy(platformLogin.address, khelManch.address, {"from": account})
    admin_change_tx = platformLogin.setOwner(admin.address, {"from": account})
    admin_change_tx.wait(1)
    admin_change_tx = khelManch.setOwner(admin.address, {"from": account})
    admin_change_tx.wait(1)
    print(admin.address)


def main():
    deploy()