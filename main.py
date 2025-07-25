import pandas as pd
from fetch_data import fetch_all_wallets
from feature_engineering import build_features_dataframe, normalize_features
from risk_scoring import calculate_score, save_scores

def load_wallets(filename):
    df = pd.read_excel(filename)
    # Try to find the column with wallet addresses
    for col in df.columns:
        if 'wallet' in col.lower():
            return df[col].dropna().unique().tolist()
    raise ValueError('No wallet address column found in Excel file.')

def main():
    wallets = load_wallets('Wallet id.xlsx')
    print(f"Loaded {len(wallets)} wallets.")
    all_transactions = fetch_all_wallets(wallets)
    features_df = build_features_dataframe(all_transactions)
    print("Feature DataFrame (first 5 rows):")
    print(features_df.head())
    norm_df = normalize_features(features_df)
    print("\nNormalized Features (first 5 rows):")
    print(norm_df.head())
    # Example weights (adjust as justified)
    weights = {
        'num_borrows': 0.2,
        'num_supplies': 0.1,
        'num_liquidations': 0.7,
        # Add more features and weights as needed
    }
    scores = calculate_score(norm_df, weights)
    print("\nRisk Scores (first 10):")
    print(scores.head(10))
    save_scores(scores)
    print("\nResults saved to wallet_scores.csv")

if __name__ == "__main__":
    main() 