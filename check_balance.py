import time
from solana.rpc.api import Client
from solders.pubkey import Pubkey

def get_solana_balance(wallet_address):
    """
    Checks the balance of a Solana wallet.

    Args:
        wallet_address (str): Solana wallet address.

    Returns:
        float: Wallet balance in SOL, or None if an error occurs.
    """
    try:
        solana_client = Client("https://api.mainnet-beta.solana.com") 
        pubkey = Pubkey.from_string(wallet_address)
        balance = solana_client.get_balance(pubkey).value
        return balance / 1000000000  
    except Exception as e:
        print(f"An error occurred while checking {wallet_address}: {e}")
        return None

def check_wallets_from_file(filepath):
    """
    Reads wallet addresses from a file and checks their balances.

    Args:
        filepath (str): Path to the text file containing wallet addresses.
    """
    try:
        with open(filepath, "r") as file:
            wallets = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return

    for wallet_address in wallets:
        balance = get_solana_balance(wallet_address)
        if balance is not None:
            print(f"Wallet {wallet_address} balance: {balance} SOL")
        time.sleep(0.5)

if __name__ == "__main__":
    filepath = r"C:\Users\user\Documents\wallets.txt" # Change this to your file path
    check_wallets_from_file(filepath)