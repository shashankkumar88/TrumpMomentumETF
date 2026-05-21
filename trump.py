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
# 3. CORE EXECUTION HANDLER
# -------------------------------------------------------------------
def execute_momentum_strategy():
    # Instantiate concurrent connections to local OpenD interface
    quote_ctx = OpenQuoteContext(host=OPEND_HOST, port=OPEND_PORT)
    trade_ctx = OpenSecTradeContext(host=OPEND_HOST, port=OPEND_PORT)

    print("=" * 75)
    print("               MOOMOO MOMENTUM SCANNER (DRY RUN ONLY)              ")
    print("=" * 75)
    # Printed table header for clean data alignment
    print(f"{'SYMBOL':<10} | {'CLOSE':<9} | {'1M MOMENTUM':<12} | {'SIGNAL':<8} | {'PROPOSED ORDER'}")
    print("-" * 75)

    # Establish dynamic timeline lookback window boundaries
    end_date_str = datetime.today().strftime('%Y-%m-%d')
    start_date_str = (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d')

    try:
        for symbol in MY_WATCHLIST:

            # Fetch continuous daily charts
            ret_code, market_data = quote_ctx.request_history_kline(
                code=symbol,
                start=start_date_str,
                end=end_date_str,
                ktype=KLType.K_DAY  # Enforces daily candlestick rule
            )

            if ret_code != RET_OK:
                print(f"{symbol:<10} | ERROR     | N/A          | ERROR    | Fetch failed: {market_data}")
                continue

            df = pd.DataFrame(market_data)
            action_signal = evaluate_daily_momentum(df)
            current_close = float(df['close'].iloc[-1])
            momentum_val = df['ROC_1M'].iloc[-1]

            # Determine order text display format
            if action_signal == "BUY":
                order_display = f"⚠️ DRY RUN: Would BUY {SHARE_QUANTITY_PER_ORDER} shares @ ${current_close:.2f}"
            elif action_signal == "SELL":
                order_display = f"⚠️ DRY RUN: Would SELL {SHARE_QUANTITY_PER_ORDER} shares @ ${current_close:.2f}"
            else:
                order_display = "No Action Required"

            # Print neatly structured, aligned data row
            print(
                f"{symbol:<10} | ${current_close:<7.2f} | {momentum_val:>10.2f}% | {action_signal:<8} | {order_display}")

            # ---------------------------------------------------------------
            # 4. ORDER DISPATCH LOGIC (DISABLED / COMMENTED OUT)
            # ---------------------------------------------------------------
            # if action_signal in ["BUY", "SELL"]:
            #     # Unlock trade functions using your account transaction PIN
            #     unlock_status, unlock_err = trade_ctx.unlock_trade(password="YOUR_6_DIGIT_PIN")
            #     if unlock_status != RET_OK:
            #         print(f" -> System Error: Trade unlock failed: {unlock_err}")
            #         continue
            #
            #     order_side = TrdSide.BUY if action_signal == "BUY" else TrdSide.SELL
            #
            #     # TrdEnv.SIMULATE sends orders straight to your Moomoo Paper Trading profile
            #     order_status, order_resp = trade_ctx.place_order(
            #         price=current_close,
            #         qty=SHARE_QUANTITY_PER_ORDER,
            #         code=symbol,
            #         trd_side=order_side,
            #         order_type=OrderType.MARKET,
            #         trd_env=TrdEnv.SIMULATE  # Change to TrdEnv.REAL for live cash trading
            #     )
            #
            #     if order_status == RET_OK:
            #         print(f" [SUCCESS] Market {order_side} order transmitted for {symbol}")
            #     else:
            #         print(f" [FAILED] Order rejected for {symbol}: {order_resp}")

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
