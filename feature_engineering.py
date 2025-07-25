import pandas as pd

def extract_features(transactions):
    # Debug: print the first transaction to inspect its structure
    if transactions:
        print("Sample transaction:", transactions[0])
    # If transactions are not dicts, return zeros
    if not transactions or not isinstance(transactions[0], dict):
        return {
            'num_borrows': 0,
            'num_supplies': 0,
            'num_liquidations': 0,
        }
    num_borrows = sum(1 for tx in transactions if tx.get('functionName', '').lower().startswith('borrow'))
    num_supplies = sum(1 for tx in transactions if tx.get('functionName', '').lower().startswith('mint'))
    num_liquidations = sum(1 for tx in transactions if tx.get('functionName', '').lower().startswith('liquidate'))
    # Add more features as needed
    return {
        'num_borrows': num_borrows,
        'num_supplies': num_supplies,
        'num_liquidations': num_liquidations,
        # ...
    }

def build_features_dataframe(all_transactions):
    features = []
    for wallet, txs in all_transactions.items():
        feats = extract_features(txs)
        feats['wallet_id'] = wallet
        features.append(feats)
    return pd.DataFrame(features).set_index('wallet_id')

def normalize_features(df):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    norm = scaler.fit_transform(df)
    return pd.DataFrame(norm, columns=df.columns, index=df.index) 