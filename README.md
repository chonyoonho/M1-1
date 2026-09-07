# Litecoin Time-Series Analysis

This project analyzes Litecoin (LTC-USD) price trends and market structure using historical daily data. The goal is to identify meaningful patterns in price movement, volatility, and trading volume, then interpret what those patterns imply for market behavior.

## Project Overview

The analysis explores:

- long-term price movement and trend changes
- major market events such as halving cycles and exchange stress events
- rolling volatility behavior
- monthly return concentration
- relationship between price and trading volume

## Data

- File: `data/litecoin.csv`
- Period: 2019-01-01 to 2026-09-04
- Data points: 2,804
- Fields: Date, Open, High, Low, Close, Volume

## Analysis Script

- File: `litecoin_analysis.py`

Run the analysis:

```bash
python litecoin_analysis.py
```

This script generates the following charts in the `images/` directory:

- `01_price_trend.png`
- `02_volatility.png`
- `03_monthly_return_heatmap.png`
- `04_price_volume_zoom.png`

## Report

- File: `REPORT.md`

The report includes the analysis topic, questions, data description, visualizations, insights, and conclusions.

## Repository Structure

```text
.
├── README.md
├── REPORT.md
├── litecoin_analysis.py
├── data/
│   └── litecoin.csv
├── images/
│   ├── 01_price_trend.png
│   ├── 02_volatility.png
│   ├── 03_monthly_return_heatmap.png
│   └── 04_price_volume_zoom.png
└── .gitignore
```

## Key Findings

- Litecoin showed a strong long-term upward trend over the sample period.
- Large price moves were accompanied by elevated volatility.
- Monthly return patterns were uneven, suggesting that a few strong months drove much of the long-term gain.
- Trading volume increased during turbulent periods but should be interpreted as a context signal rather than a direct cause of price direction.

## Requirements

Install the dependencies:

```bash
pip install pandas numpy matplotlib
```

## License

This project is for educational and portfolio-use purposes.
