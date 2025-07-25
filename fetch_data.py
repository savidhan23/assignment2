import requests
import time

ETHERSCAN_API_KEY = 'D941GKNI165J2MARZJ36MZBRS1ISIFT4IN'  # Replace with your key
COMPOUND_V2_ADDRESS = '0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b'  # Comptroller
# Add V3 addresses as needed

def fetch_compound_transactions(wallet, debug=False):
    url = f'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': wallet,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': ETHERSCAN_API_KEY
    }
    response = requests.get(url, params=params)
    try:
        data = response.json()
    except Exception as e:
        print(f"Error parsing JSON for wallet {wallet}: {e}")
        return []
    if debug:
        print(f"Raw API response for wallet {wallet}:\n", data)
    if data.get('status') != '1' or 'result' not in data:
        print(f"API returned error or no result for wallet {wallet}: {data.get('message', 'No message')}")
        return []
    # Filter for Compound contract interactions if needed
    return data['result']

def fetch_all_wallets(wallets):
    all_data = {}
    for i, wallet in enumerate(wallets):
        all_data[wallet] = fetch_compound_transactions(wallet, debug=(i==0))
        time.sleep(0.2)  # Respect rate limits
    return all_data