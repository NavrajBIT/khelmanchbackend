from django.conf import settings
from . import contract_config
import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware


# Contract data
contract_address = contract_config.config["contract_address"]
public_key = contract_config.config["public_key"]
private_key = contract_config.config["private_key"]

contract_filepath = os.path.join(
    settings.BASE_DIR, "api/Admin.json")

with open(contract_filepath, "r") as file:
    contract_json = json.load(file)

abi = contract_json["abi"]
bytecode = contract_json["bytecode"]

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
w3.eth.defaultAccount = public_key
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
myContract = w3.eth.contract(address=contract_address, abi=abi)


def add_creator(_userName, _profilepic):
    print("Calling contract---------------------")
    nonce = w3.eth.get_transaction_count(public_key)
    add_creator_tx = myContract.functions.addCreator(
        _userName, _profilepic).build_transaction({"from": public_key, "nonce": nonce, "gasPrice": 100000})
    signed_tx = w3.eth.account.sign_transaction(
        add_creator_tx, private_key=private_key)
    add_creator_tx_data = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(add_creator_tx_data)
    return True


def add_profile(
    _name,
    _age,
    _gender,
    _fatherName,
    _motherName,
    _address,
    _imgHash,
    _skillName,
    _description
):
    print("Calling contract---------------------")
    nonce = w3.eth.get_transaction_count(public_key)
    add_profile_tx = myContract.functions.addClub(
        _name,
        _age,
        _gender,
        _fatherName,
        _motherName,
        _address,
        _imgHash,
        _skillName,
        _description).build_transaction({"from": public_key, "nonce": nonce, "gasPrice": 100000})
    signed_tx = w3.eth.account.sign_transaction(
        add_profile_tx, private_key=private_key)
    add_profile_tx_data = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(add_profile_tx_data)
    return True


def upload_video(
    _profileId,
    _videoLink,
    _description,
    _skillName
):
    print("Calling contract---------------------")
    nonce = w3.eth.get_transaction_count(public_key)
    upload_video_tx = myContract.functions.addClub(
        _profileId,
        _videoLink,
        _description,
        _skillName).build_transaction({"from": public_key, "nonce": nonce, "gasPrice": 100000})
    signed_tx = w3.eth.account.sign_transaction(
        upload_video_tx, private_key=private_key)
    upload_video_tx_data = w3.eth.send_raw_transaction(
        signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(upload_video_tx_data)
    return True
