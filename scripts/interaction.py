from brownie import wallet
from scripts.misk import get_account


def interact():
    """
    Interact with the contract deployed on the blockchain.
    """
    connected = True
    while connected:
        latest_contract_address = wallet[-1]
        account = get_account()
        entry_fee = latest_contract_address.getEntranceFee()
        print(f"The chosen contract address is --> {latest_contract_address}")
        option = input(
            "Choose what you want to do with the smart contract...\n1 - Get the contract balance.\n2 - Fund the contract.\n 3 - Withdraw the funds\n 4 - Quit\n"
        )
        if option == "1":
            balance = latest_contract_address.get_balance({"from": account})
            print(f"Contract balance ---> {balance}\n\n\n\n\n")
        elif option == "2":
            entry_fee_option = input("Do you wish to transfer the entry fee Y/N ?")
            if entry_fee_option.upper() == "N":
                entry_fee = int(input("Send the amount to be transferred"))
            print("Funding to the wallet..\n")
            latest_contract_address.add_funds({"from": account, "value": entry_fee})
        elif option == "3":
            latest_contract_address.withdraw_amount({"from": account})
        elif option == "4":
            connected = False
            print("Quitting...!")
        else:
            print("Enter a valid option .. Try again ...!!")


def main():
    interact()
