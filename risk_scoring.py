import pandas as pd

def calculate_score(norm_df, weights):
    scores = norm_df.mul(weights).sum(axis=1)
    # Scale to 0–1000
    return (scores / scores.max() * 1000).astype(int)

def save_scores(scores, filename='wallet_scores.csv'):
    scores.to_csv(filename, header=['score']) 