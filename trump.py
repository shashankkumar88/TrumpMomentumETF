import pandas as pd
import numpy as np
from moomoo import *  # Official Moomoo OpenD library wrapper
import time
from datetime import datetime, timedelta

# -------------------------------------------------------------------
# 1. INITIALIZE CONFIGURATION & YOUR CUSTOM WATCHLIST
# -------------------------------------------------------------------
OPEND_HOST = "127.0.0.1"
OPEND_PORT = 11113
SHARE_QUANTITY_PER_ORDER = 10  # Standard fixed position size

# Your exact requested list normalized to Moomoo OpenAPI syntax
MY_WATCHLIST = [
    "US.NVDA", "US.AVGO", "US.INTC", "US.DELL", "US.SNDK",
    "US.PLTR", "US.MSFT", "US.ORCL", "US.NOW", "US.WDAY",
    "US.ADBE", "US.BA", "US.GE", "US.AAPL", "US.AMZN",
    "US.UBER", "US.BE"
]


# -------------------------------------------------------------------
# 2. TIME-SERIES DAILY MOMENTUM ENGINE
# -------------------------------------------------------------------
def evaluate_daily_momentum(df):
    """
    Computes professional trend indicators on Daily Candlesticks:
    - EMA 12 vs EMA 50 to confirm structural trend directions
    - 21 Trading Days (~1 Calendar Month) Rate of Change (ROC)
    """
    if len(df) < 55:
        return "HOLD"  # Insufficient data to build reliable historical EMAs

    # Calculate indicators via standard pandas data manipulation
    df['EMA12'] = df['close'].ewm(span=12, adjust=False).mean()
    df['EMA50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['ROC_1M'] = df['close'].pct_change(periods=21) * 100

    latest_bar = df.iloc[-1]
    prior_bar = df.iloc[-2]

    # Mathematical cross triggers
    is_bullish_crossover = (prior_bar['EMA12'] <= prior_bar['EMA50']) and (latest_bar['EMA12'] > latest_bar['EMA50'])
    is_bearish_crossover = (prior_bar['EMA12'] >= prior_bar['EMA50']) and (latest_bar['EMA12'] < latest_bar['EMA50'])

    # Strict execution rules
    if is_bullish_crossover and latest_bar['ROC_1M'] > 0:
        return "BUY"
    elif is_bearish_crossover or latest_bar['ROC_1M'] < -5:
        return "SELL"

    return "HOLD"


# -------------------------------------------------------------------
# 3. DIAGNOSTIC: CHECK MOOMOO ACCOUNT API QUOTA
# -------------------------------------------------------------------
def print_moomoo_quota_status(quote_ctx):
    """Fetches and prints the account's historical candlestick token quota."""
    print("=" * 75)
    print("               MOOMOO API QUOTA & ACCOUNT DIAGNOSTICS              ")
    print("=" * 75)
    ret_code, data = quote_ctx.get_history_kl_quota()
    if ret_code == RET_OK:
        # FIX: Access tuple elements by integer indices
        used_quota = data[0]
        remain_quota = data[1]

        print(f" -> Used Quota Stock Count : {used_quota}")
        print(f" -> Remaining Stock Quota  : {remain_quota}")
        if remain_quota == 0:
            print(" ⚠️  WARNING: Your historical data token allowance is completely empty!")
            print("    You must unlock data permissions or fund your Moomoo account.")
    else:
        print(f" ⚠️  CRITICAL: Could not fetch account data status. Gateway error: {data}")
    print("=" * 75 + "\n")


# -------------------------------------------------------------------
# 4. CORE EXECUTION HANDLER
# -------------------------------------------------------------------
def execute_momentum_strategy():
    # Instantiate concurrent connections to local OpenD interface
    quote_ctx = OpenQuoteContext(host=OPEND_HOST, port=OPEND_PORT)
    trade_ctx = OpenSecTradeContext(host=OPEND_HOST, port=OPEND_PORT)

    # Run data permission diagnostics before scanning
    print_moomoo_quota_status(quote_ctx)

    print("=" * 75)
    print("               MOOMOO MOMENTUM SCANNER (DRY RUN ONLY)              ")
    print("=" * 75)
    print(f"{'SYMBOL':<10} | {'CLOSE':<9} | {'1M MOMENTUM':<12} | {'SIGNAL':<8} | {'PROPOSED ORDER'}")
    print("-" * 75)

    # Establish dynamic timeline lookback window boundaries
    end_date_str = datetime.today().strftime('%Y-%m-%d')
    start_date_str = (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d')

    try:
        for symbol in MY_WATCHLIST:

            # Moomoo Native Signature Unpacking format
            ret_code, data, page_req_key = quote_ctx.request_history_kline(
                code=symbol,
                start=start_date_str,
                end=end_date_str,
                ktype=KLType.K_DAY  # Enforces daily candlestick rule
            )

            # Handle explicit Moomoo system/connection faults or missing data permissions
            if ret_code != RET_OK:
                print(f"{symbol:<10} | ERROR     | N/A          | ERROR    | Reason: {data}")
                time.sleep(0.5)
                continue

            # Ensure we have a valid pandas DataFrame to analyze
            if not isinstance(data, pd.DataFrame) or data.empty:
                print(f"{symbol:<10} | NO_DATA   | N/A          | SKIP     | Empty payload or None object returned.")
                time.sleep(0.5)
                continue

            df = data
            action_signal = evaluate_daily_momentum(df)
            current_close = float(df['close'].iloc[-1])

            # Gracefully handle possible NaN values for momentum presentation
            momentum_val = df['ROC_1M'].iloc[-1]
            if pd.isna(momentum_val):
                momentum_str = f"{'N/A':>11}"
            else:
                momentum_str = f"{momentum_val:>10.2f}%"

            # Determine order text display format
            if action_signal == "BUY":
                order_display = f"⚠️ DRY RUN: Would BUY {SHARE_QUANTITY_PER_ORDER} shares @ ${current_close:.2f}"
            elif action_signal == "SELL":
                order_display = f"⚠️ DRY RUN: Would SELL {SHARE_QUANTITY_PER_ORDER} shares @ ${current_close:.2f}"
            else:
                order_display = "No Action Required"

            # Print neatly structured, aligned data row
            print(f"{symbol:<10} | ${current_close:<7.2f} | {momentum_str} | {action_signal:<8} | {order_display}")

            # Brief delay prevents hitting Moomoo API gateway frequency throttling thresholds
            time.sleep(0.5)

    except Exception as general_err:
        print(f"\n[CRITICAL ERROR DURING RUNTIME]: {general_err}")

    finally:
        # Prevent open sockets and context memory leaks by disconnecting cleanly
        quote_ctx.close()
        trade_ctx.close()
        print("=" * 75)
        print("ALGORITHM SCAN COMPLETE: API contexts cleanly terminated.")
        print("=" * 75)


if __name__ == "__main__":
    execute_momentum_strategy()
