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


#데이터 분석 사고

분석 질문 정의 (3개 이상):

질문 1: 전체 기간 동안 라이트코인(LTC)의 장기적인 가격 트렌드는 어떠한가?

질문 2: 변동성이 가장 높게 나타나는 특정 주기가 존재하는가?

질문 3: 거래량의 급증이 가격 상승 또는 하락 신호와 어떠한 상관관계를 보이는가?

결측치 및 이상치 처리 기준:

결측치(Missing Values): 데이터 누락 구간을 의미하며, 시계열 흐름을 깨지 않기 위해 보간법(Interpolation)이나 이전 값 대체(Forward Fill)를 적용하거나 삭제 처리함.

이상치(Outliers): 일반적인 범주를 벗어난 극단적인 값(예: 급격한 숏스퀴즈/플래시 크래시)으로, 실제 시장 사건(이벤트)인지 단순 수집 오류인지 구별하여 유지할지 제거할지 결정함.

관찰(Fact) vs 해석(Hypothesis) 구분:

관찰 (사실): "2021년 5월에 거래량이 평소 대비 3배 이상 급증하며 가격 변동폭이 커졌다."

해석 (가설): "시장 악재로 인한 투매 현상이 발생했거나 큰 변동성에 따른 차익 실현 물량이 대량 출회되었을 것이다."

시계열 데이터 이해

시계열 핵심 개념:

트렌드(Trend): 장기적으로 나타나는 가격의 전반적인 상승/하락 방향성.

계절성(Seasonality): 일정한 주기(월별, 분기별, 반감기 등)로 반복되는 패턴.

노이즈(Noise): 단기 이슈나 무작위적인 변동으로 인해 나타나는 불규칙한 미세 흔들림.

기본 시계열 기법 적용 이유 및 방법:

이동평균(Moving Average): 단기 노이즈를 제거하여 장기 추세(트렌드)를 명확하게 파악하기 위해 적용 (예: 20일/50일 이동평균선 활용).

변화율(Percentage Change): 절대 금액 단위의 차이 대신 기간별 수익률을 상대적으로 비교·평가하기 위해 계산.

AI 활용 역량

목적에 맞는 AI 질문 및 코드/해석 검증:

분석하고자 하는 목표(예: "라이트코인의 30일 이동평균선을 구하고 변동성을 시각화하는 파이썬 코드를 작성해줘")를 구체적으로 전달.

AI가 작성한 코드의 가상 데이터/오류 유무를 실행으로 직접 검증하고, 계산된 수치가 실제 데이터의 도메인 지식과 부합하는지 체크.

최종 판단 및 논리 구축:

AI의 해석은 참고 자료로만 활용하며, 시각화 자료 및 정량적 수치 데이터(거래량, 수익률, 변동성 지표 등)를 직접적인 근거로 삼아 최종 보고서 및 결론을 도출.
