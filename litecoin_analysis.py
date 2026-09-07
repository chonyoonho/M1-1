import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
IMG_DIR = ROOT / "images"
DATA_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(exist_ok=True)

CSV_PATH = DATA_DIR / "litecoin.csv"
TICKER = "LTC-USD"

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


def load_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH, parse_dates=["Date"]).sort_values("Date")
    df = df.set_index("Date")
    return df[["Open", "High", "Low", "Close", "Volume"]]


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Return"] = df["Close"].pct_change()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["Volatility30"] = df["Return"].rolling(30).std() * np.sqrt(252) * 100
    return df


EVENTS = [
    ("2020-05-11", "라이트코인 반감기"),
    ("2021-05-10", "암호화폐 시장 고점 구간"),
    ("2022-11-11", "FTX 파산 신청"),
    ("2023-08-02", "라이트코인 반감기"),
    ("2024-04-20", "비트코인 반감기"),
]


def plot_price_trend(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["Close"], label="종가", color="#1f77b4", linewidth=1.5)
    ax.plot(df.index, df["MA50"], label="50일 이동평균", color="orange", linewidth=1.2)
    ax.plot(df.index, df["MA200"], label="200일 이동평균", color="green", linewidth=1.2)

    y_offsets = [35, 30, 20, 25, 28]
    for (date_str, label), y_off in zip(EVENTS, y_offsets):
        d = pd.Timestamp(date_str)
        if d < df.index.min() or d > df.index.max():
            continue
        ax.axvline(d, color="red", linestyle="--", alpha=0.35)
        y = df["Close"].asof(d)
        ax.annotate(
            label,
            xy=(d, y),
            xytext=(12, y_off),
            textcoords="offset points",
            fontsize=8,
            color="red",
            ha="left",
            arrowprops=dict(arrowstyle="->", color="red", alpha=0.5),
        )

    ax.set_title(f"{TICKER} 가격 추이 (2019~2026, 로그 스케일) — 주요 이벤트 표시")
    ax.set_xlabel("날짜")
    ax.set_ylabel("종가 (USD, log scale)")
    ax.legend(loc="upper left")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig(IMG_DIR / "01_price_trend.png", dpi=150)
    plt.close(fig)


def plot_volatility(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["Volatility30"], color="#d62728", linewidth=1.2)
    ax.fill_between(df.index, df["Volatility30"], alpha=0.2, color="#d62728")

    for date_str, label in EVENTS:
        d = pd.Timestamp(date_str)
        if d < df.index.min() or d > df.index.max():
            continue
        ax.axvline(d, color="gray", linestyle="--", alpha=0.35)

    ax.set_title(f"{TICKER} 30일 롤링 변동성 (연율화, %)")
    ax.set_xlabel("날짜")
    ax.set_ylabel("연율화 변동성 (%)")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig(IMG_DIR / "02_volatility.png", dpi=150)
    plt.close(fig)


def plot_monthly_return_heatmap(df: pd.DataFrame):
    monthly = df["Close"].resample("ME").last().pct_change().dropna() * 100
    monthly.index = pd.MultiIndex.from_arrays(
        [monthly.index.year, monthly.index.month], names=["year", "month"]
    )
    table = monthly.unstack(level="month")
    table = table.reindex(columns=range(1, 13))

    fig, ax = plt.subplots(figsize=(10, 6))
    vmax = np.nanmax(np.abs(table.values))
    im = ax.imshow(table.values, cmap="RdYlGn", vmin=-vmax, vmax=vmax, aspect="auto")

    ax.set_xticks(range(12))
    ax.set_xticklabels([f"{m}월" for m in range(1, 13)])
    ax.set_yticks(range(len(table.index)))
    ax.set_yticklabels(table.index)
    ax.set_title(f"{TICKER} 월별 수익률 히트맵 (%)")

    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            val = table.values[i, j]
            if not np.isnan(val):
                ax.text(j, i, f"{val:.0f}", ha="center", va="center", fontsize=7)

    fig.colorbar(im, ax=ax, label="월 수익률 (%)")
    fig.tight_layout()
    fig.savefig(IMG_DIR / "03_monthly_return_heatmap.png", dpi=150)
    plt.close(fig)


def plot_price_volume(df: pd.DataFrame):
    recent = df.loc["2022-06-01":]
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(12, 7), sharex=True, gridspec_kw={"height_ratios": [3, 1]}
    )
    ax1.plot(recent.index, recent["Close"], color="#1f77b4", linewidth=1.5)
    ax1.set_title(f"{TICKER} 가격 & 거래량 (2022.06 ~ 현재)")
    ax1.set_ylabel("종가 (USD)")

    ax2.bar(recent.index, recent["Volume"], color="gray", width=1)
    ax2.set_ylabel("거래량")
    ax2.set_xlabel("날짜")

    fig.tight_layout()
    fig.savefig(IMG_DIR / "04_price_volume_zoom.png", dpi=150)
    plt.close(fig)


def print_summary(df: pd.DataFrame):
    total_return = (df["Close"].iloc[-1] / df["Close"].iloc[0] - 1) * 100
    cummax = df["Close"].cummax()
    drawdown = (df["Close"] / cummax - 1) * 100
    max_dd = drawdown.min()
    monthly = df["Close"].resample("ME").last().pct_change().dropna() * 100

    print(f"분석 기간: {df.index.min().date()} ~ {df.index.max().date()}")
    print(f"데이터 포인트 수: {len(df)}")
    print(f"누적 수익률: {total_return:.1f}%")
    print(f"최대 낙폭(MDD): {max_dd:.1f}%")
    print(f"최고 상승 월: {monthly.idxmax()} ({monthly.max():.1f}%)")
    print(f"최고 하락 월: {monthly.idxmin()} ({monthly.min():.1f}%)")
    print(f"평균 30일 변동성: {df['Volatility30'].mean():.1f}%")


def main():
    df = load_data()
    df = add_indicators(df)
    plot_price_trend(df)
    plot_volatility(df)
    plot_monthly_return_heatmap(df)
    plot_price_volume(df)
    print_summary(df)


if __name__ == "__main__":
    main()
