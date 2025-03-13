**Solana Wallet Balance Checker**

Solana Wallet Balance Checker is a simple Python script that retrieves and displays the balance of Solana wallets. 
It reads wallet addresses from a file and queries the Solana blockchain via RPC to fetch their balances.

**Features**:

Checks the balance of multiple Solana wallets.
Uses Solana RPC API for real-time balance fetching.
Outputs balance in SOL (converted from lamports).
Handles errors and missing files gracefully.
To run this script, you'll need to install the following Python libraries:
- `solana` – A Python library for interacting with the Solana blockchain.
- `solders` – A library for working with Solana public keys.
You can install these dependencies by running:
pip install solana solders

Usage:

Place wallet addresses (one per line) in a text file (e.g., wallets.txt).
Specify the correct path to wallets.txt in line 45 of the script:
filepath = r"C:\Users\user\Documents\wallets.txt"  # Change this to your file path

Run the script to check balances: python check_balance.py

The script will display each wallet's balance and wait 0.5 seconds between requests to avoid rate limits.
