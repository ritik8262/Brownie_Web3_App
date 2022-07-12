import shutil
from turtle import update
from brownie import WavePortal, network
from scripts.helpful_scripts import get_account
from web3 import Web3
import yaml
import json
import os
import shutil

VALUE = Web3.toWei(0.1, "ether")


def deploy_waves_portal(front_end_update=False):
    account = get_account()

    print(f"{network.show_active()}\n")

    wave_portal = WavePortal.deploy({"from": account, "value": VALUE})

    # stored_value = wave_portal.getTotalWaves()
    # print(f"We have {stored_value} total waves")

    print(f"Contract Deployed to {wave_portal.address}\n")

    contractBalance = wave_portal.get_Balance() / (10**18)
    print(f"balance of contract is {contractBalance}\n")

    storing = wave_portal.wave("Ritik", {"from": account, "gasLimit": 300000})
    storing.wait(1)

    print(f"{account.address} waved w/ message\n")

    storing1 = wave_portal.wave("Abhi", {"from": account, "gasLimit": 300000})
    storing1.wait(1)
    print(f"{account.address} waved w/ message\n")

    all_waves = wave_portal.getAllWaves()
    print(f"All wavers are:{all_waves}\n")

    # stored_value = wave_portal.getTotalWaves()
    # print(f"We have {stored_value} total waves")

    updated_balance = wave_portal.get_Balance() / 10**18

    print(f"Updated balance of contract is {updated_balance}")
    if front_end_update:
        update_front_end()


def update_front_end():

    # Send the build folder
    copy_folders_to_front_end("./build", "./front_end/src/chain-info")

    # Send the front end our config in JSON format
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./front_end/src/brownie_config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Front end updated!")


def copy_folders_to_front_end(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main():
    deploy_waves_portal(front_end_update=True)
