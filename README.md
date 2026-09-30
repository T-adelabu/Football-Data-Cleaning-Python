# Football Player Data Cleaning (Python + pandas)

## Overview
A data cleaning project using Python and pandas to prepare a raw football player statistics dataset (95 players, 12 columns) for analysis by removing duplicate records and rows with missing data.

## Tools Used
- **Python**
- **pandas**

## Dataset
Player-level football statistics including Age, Team, Position, Games Played, Passing/Rushing/Receiving Yards, Touchdowns, Height, and Weight.

## Code

```python
import pandas as pd

df = pd.read_csv("footballData.csv")

print(df.head())

df = df.drop_duplicates()

df = df.dropna()
```

## What Each Step Does
1. **`pd.read_csv()`** — loads the raw CSV into a pandas DataFrame
2. **`df.head()`** — previews the first 5 rows to confirm the data loaded correctly and check column structure
3. **`drop_duplicates()`** — removes fully duplicate rows
4. **`dropna()`** — removes any row containing at least one missing value in any column

## Results
- **Started with 95 rows, 12 columns**
- **5 duplicate rows** were identified and removed
- **6 additional rows** had missing values (mostly in Age, Team, Games_Played, or Weight) and were dropped
- **Final cleaned dataset: 84 rows**, fully complete with no duplicates or missing values

## A Note on `dropna()`
`dropna()` removes an entire row if *any* single column is missing a value, even if the rest of that row's data is perfectly usable. In this dataset, that meant losing complete records for 6 players over just one missing field each. A next iteration of this project could use `df.fillna()` to fill in reasonable defaults (like a position-average for Games Played) instead of discarding usable data outright, a common real-world tradeoff between data completeness and data availability.

## Skills Demonstrated
Reading and inspecting tabular data with pandas, identifying and removing duplicate records, handling missing data, and understanding the tradeoffs of different data-cleaning strategies.
