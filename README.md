# Compound Wallet Risk Scoring

## Data Collection
- Used Etherscan API to fetch all ERC-20 token transactions for each wallet in the provided Excel file.
- Filtered transactions to those interacting with Compound V2 contracts (can be extended for V3).

## Feature Selection
- Number of borrows, supplies, and liquidations were chosen as risk indicators.
- More liquidations and borrows increase risk; more supplies decrease risk.
- Features can be expanded to include collateralization ratio, activity span, protocol version, etc.

## Normalization
- Features are min-max normalized to [0, 1] for comparability.

## Scoring
- Weighted sum of normalized features, scaled to 0–1000.
- Example weights: liquidations (0.7), borrows (0.2), supplies (0.1).
- Liquidations weighted highest as they are the strongest risk signal.

## Justification
- Liquidations indicate poor risk management.
- High borrow/supply ratio signals aggressive leverage.
- Feature set and weights can be expanded for more nuanced analysis.

## Output
- Results are saved to `wallet_scores.csv` with columns: `wallet_id`, `score`. 