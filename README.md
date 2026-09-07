# Litecoin Time-Series Analysis

This project analyzes Litecoin (LTC-USD) price behavior over time and interprets the major patterns hidden in the data.

The goal is not simply to plot a chart, but to identify what drove the price movement, how volatility changed over time, and what the resulting market signal means for decision-making.

## Overview

This project examines:

- long-term price trends
- major event periods such as halving cycles and market stress events
- rolling volatility
- monthly return concentration
- the relationship between price changes and trading volume

## Data

- Data file: `data/litecoin.csv`
- Period: 2019-01-01 to 2026-09-04
- Data points: 2,804
- Columns: Date, Open, High, Low, Close, Volume

## Files

- Analysis script: `litecoin_analysis.py`
- Report: `REPORT.md`
- Generated visualizations: `images/`
- Raw dataset: `data/litecoin.csv`

## Run

```bash
python litecoin_analysis.py
```

The script generates four charts:

- `images/01_price_trend.png`
- `images/02_volatility.png`
- `images/03_monthly_return_heatmap.png`
- `images/04_price_volume_zoom.png`

## Report Summary

The report covers:

- analysis topic and research questions
- data explanation
- chart interpretation
- key insights and conclusions
- limitations of the analysis

## Key Findings

- Litecoin delivered strong long-term gains, but with very large drawdowns.
- Volatility increased sharply during market stress and upward breakout periods.
- Return patterns were uneven and concentrated in a few months.
- Trading volume rose with market turbulence, but it acted more as a confirmation signal than a cause.

## Requirements

```bash
pip install pandas numpy matplotlib
```

## License

This project is distributed under the MIT License.
