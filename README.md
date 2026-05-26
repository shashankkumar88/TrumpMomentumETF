<img src="etfconstituents.png" alt="Alternative Text" width="500">
Reference : https://www.youtube.com/watch?v=fbn64JV-hXU 

# Moomoo Time-Series Momentum Trading Bot 📈

A professional-grade algorithmic scanner built on top of the official Futu/Moomoo OpenD API wrapper. This system analyzes structured historical time-series data to execute momentum-driven trend strategies across a custom equities watchlist.

---

## 🚀 Strategy Architecture

The execution engine evaluates market structure over a rolling **120-day historical time frame** using dual-layered mathematical indicators:

1. **Structural Trend Direction**: Computes exponential moving averages (**EMA 12** vs **EMA 50**) on daily candlesticks to identify systematic, high-conviction trend crossovers.
2. **Velocity Multiplier**: Calculates a 21-trading-day (~1 calendar month) **Rate of Change (ROC)** matrix to verify underlying transaction velocity.

### 📐 Execution Rules
* **BUY Trigger**: Occurs when a *bullish crossover* finishes (EMA 12 passes above EMA 50) and 1-month momentum is strictly positive (`ROC_1M > 0`).
* **SELL Trigger**: Occurs instantly if a *bearish crossover* materializes (EMA 12 falls beneath EMA 50) **OR** the asset's monthly momentum declines rapidly (`ROC_1M < -5`).

---

## 🛠️ Performance & Runtime Verification

Below is an active pipeline log tracking operational asset evaluation, quota consumption metrics, and risk-managed execution signals.

```text
===========================================================================
               MOOMOO API QUOTA & ACCOUNT DIAGNOSTICS              
===========================================================================
 -> Used Quota Stock Count : 17
 -> Remaining Stock Quota  : 1983
===========================================================================

===========================================================================
               MOOMOO MOMENTUM SCANNER (DRY RUN ONLY)              
===========================================================================
SYMBOL     | CLOSE     | 1M MOMENTUM  | SIGNAL   | PROPOSED ORDER
---------------------------------------------------------------------------
US.NVDA    | $219.51  |       8.40% | HOLD     | No Action Required
US.AVGO    | $414.57  |      -1.91% | HOLD     | No Action Required
US.INTC    | $118.50  |      81.55% | HOLD     | No Action Required
US.DELL    | $252.80  |      17.77% | HOLD     | No Action Required
US.SNDK    | $1542.24 |      57.52% | HOLD     | No Action Required
US.PLTR    | $137.41  |      -9.96% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $137.41
US.MSFT    | $419.09  |      -2.98% | HOLD     | No Action Required
US.ORCL    | $189.77  |       1.21% | HOLD     | No Action Required
US.NOW     | $99.69   |      -3.28% | HOLD     | No Action Required
US.WDAY    | $121.85  |      -3.75% | HOLD     | No Action Required
US.ADBE    | $244.10  |      -4.63% | HOLD     | No Action Required
US.BA      | $219.61  |      -5.05% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $219.61
US.GE      | $301.76  |       9.22% | HOLD     | No Action Required
US.AAPL    | $304.99  |      11.75% | HOLD     | No Action Required
US.AMZN    | $268.46  |       5.13% | HOLD     | No Action Required
US.UBER    | $73.61   |      -2.61% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $73.61
US.BE      | $307.88  |      34.01% | HOLD     | No Action Required
===========================================================================
ALGORITHM SCAN COMPLETE: API contexts cleanly terminated.
===========================================================================
```
===========================================================================
               MOOMOO MOMENTUM SCANNER (DRY RUN ONLY)              
===========================================================================
SYMBOL     | CLOSE     | 1M MOMENTUM  | SIGNAL   | PROPOSED ORDER
---------------------------------------------------------------------------
US.MMM     | $153.54  |       5.72% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $153.54
US.AOS     | $58.07   |      -9.29% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $58.07
US.ABT     | $86.41   |      -5.18% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $86.41
US.ABBV    | $213.71  |       7.55% | HOLD     | No Action Required
US.ACN     | $177.95  |      -0.23% | HOLD     | No Action Required
US.ADBE    | $242.37  |      -1.25% | HOLD     | No Action Required
US.AMD     | $489.39  |      40.71% | HOLD     | No Action Required
US.AES     | $14.67   |       2.49% | HOLD     | No Action Required
US.AFL     | $117.11  |       2.70% | HOLD     | No Action Required
US.A       | $114.37  |      -1.02% | HOLD     | No Action Required
US.APD     | $287.44  |      -4.74% | HOLD     | No Action Required
US.ABNB    | $133.50  |      -6.52% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $133.50
US.AKAM    | $147.80  |      55.17% | HOLD     | No Action Required
US.ALB     | $177.51  |      -5.75% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $177.51
US.ALK     | $43.33   |       4.18% | HOLD     | No Action Required
US.ALGN    | $163.86  |     -13.58% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $163.86
US.ALLE    | $131.51  |      -9.99% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $131.51
US.LNT     | $73.57   |       2.50% | HOLD     | No Action Required
US.ALL     | $214.08  |       0.56% | HOLD     | No Action Required
US.GOOGL   | $386.48  |      12.22% | HOLD     | No Action Required
US.GOOG    | $382.51  |      11.74% | HOLD     | No Action Required
US.MO      | $72.14   |       7.86% | HOLD     | No Action Required
US.AMZN    | $263.56  |      -0.16% | HOLD     | No Action Required
US.AMCR    | $38.72   |      -0.59% | HOLD     | No Action Required
US.AEE     | $110.96  |      -0.14% | HOLD     | No Action Required
US.AAL     | $14.77   |      22.05% | HOLD     | No Action Required
US.AEP     | $131.12  |      -1.97% | HOLD     | No Action Required
US.AXP     | $310.60  |      -1.11% | HOLD     | No Action Required
US.AIG     | $77.75   |       3.47% | HOLD     | No Action Required
US.AMT     | $183.78  |       3.12% | HOLD     | No Action Required
US.AWK     | $124.62  |      -5.22% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $124.62
US.AMP     | $453.46  |      -1.94% | HOLD     | No Action Required
US.AME     | $226.77  |      -2.65% | HOLD     | No Action Required
US.AMGN    | $337.34  |      -1.35% | HOLD     | No Action Required
US.APH     | $143.29  |      -4.29% | HOLD     | No Action Required
US.ADI     | $417.39  |       4.46% | HOLD     | No Action Required
US.ANSS    | ERROR     | N/A          | ERROR    | Reason: Unknown stock ANSS
US.AON     | $321.13  |       0.26% | HOLD     | No Action Required
US.APA     | $38.46   |       1.93% | HOLD     | No Action Required
US.APO     | $130.66  |       5.59% | HOLD     | No Action Required
US.AAPL    | $310.69  |      14.72% | HOLD     | No Action Required
US.AMAT    | $448.64  |       7.71% | HOLD     | No Action Required
US.APTV    | $57.91   |      -3.64% | HOLD     | No Action Required
US.ACGL    | $95.66   |      -0.55% | HOLD     | No Action Required
US.ADM     | $78.89   |      14.70% | HOLD     | No Action Required
US.ANET    | $159.35  |      -9.93% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $159.35
US.AJG     | $203.97  |      -5.30% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $203.97
US.AIZ     | $256.02  |      11.41% | HOLD     | No Action Required
US.T       | $25.02   |      -4.48% | HOLD     | No Action Required
US.ATO     | $177.80  |      -3.58% | HOLD     | No Action Required
US.ADSK    | $238.37  |       0.39% | HOLD     | No Action Required
US.ADP     | $221.05  |      12.48% | HOLD     | No Action Required
US.AZO     | $3009.53 |     -15.89% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $3009.53
US.AVB     | $185.91  |       7.85% | HOLD     | No Action Required
US.AVY     | $159.01  |      -3.92% | HOLD     | No Action Required
US.AXON    | $399.50  |       0.60% | HOLD     | No Action Required
US.BKR     | $67.12   |      -2.31% | HOLD     | No Action Required
US.BALL    | $56.37   |      -8.07% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $56.37
US.BAC     | $52.09   |       0.07% | HOLD     | No Action Required
US.BK      | $137.16  |      -0.16% | HOLD     | No Action Required
US.BBWI    | $18.07   |     -10.05% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $18.07
US.BAX     | $19.36   |       6.64% | HOLD     | No Action Required
US.BDX     | $146.71  |      -3.57% | HOLD     | No Action Required
US.BRK-B   | ERROR     | N/A          | ERROR    | Reason: Unknown stock BRK-B
US.BBY     | $62.55   |       3.47% | HOLD     | No Action Required
US.BIO     | $289.81  |       0.68% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $289.81
US.TECH    | $47.86   |     -11.51% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $47.86
US.BIIB    | $193.87  |       5.15% | HOLD     | No Action Required
US.BLK     | $1073.07 |       2.69% | HOLD     | No Action Required
US.BX      | $118.49  |      -1.70% | HOLD     | No Action Required
US.BA      | $220.21  |      -5.26% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $220.21
US.BKNG    | $163.96  |      -9.04% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $163.96
US.BWA     | $66.62   |      18.36% | HOLD     | No Action Required
US.BSX     | $57.67   |      -7.09% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $57.67
US.BMY     | $58.24   |      -0.80% | HOLD     | No Action Required
US.AVGO    | $423.21  |       0.11% | HOLD     | No Action Required
US.BR      | $147.20  |      -5.08% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $147.20
US.BRO     | $57.47   |     -12.54% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $57.47
US.BCC     | $67.42   |     -19.88% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $67.42
US.BLDR    | $74.74   |     -16.99% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $74.74
US.BG      | $122.80  |      -1.09% | HOLD     | No Action Required
US.BXP     | $60.65   |       5.05% | HOLD     | No Action Required
US.CHRW    | $177.13  |      -3.22% | HOLD     | No Action Required
US.CDNS    | $380.81  |      14.40% | HOLD     | No Action Required
US.CZR     | $28.34   |       0.78% | HOLD     | No Action Required
US.CPT     | $107.85  |       6.00% | HOLD     | No Action Required
US.CPB     | $20.39   |      -1.09% | HOLD     | No Action Required
US.COF     | $187.43  |      -1.65% | HOLD     | No Action Required
US.CAH     | $200.37  |       0.26% | HOLD     | No Action Required
US.KMX     | $40.86   |       6.77% | HOLD     | No Action Required
US.CCL     | $26.75   |      -0.96% | HOLD     | No Action Required
US.CARR    | $64.58   |       6.29% | HOLD     | No Action Required
US.CAT     | $902.95  |       8.69% | HOLD     | No Action Required
US.CBOE    | $356.07  |      17.20% | HOLD     | No Action Required
US.CBRE    | $129.84  |     -12.44% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $129.84
US.CDW     | $110.55  |     -17.82% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $110.55
US.CE      | $52.72   |     -18.85% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $52.72
US.COR     | $272.25  |     -11.46% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $272.25
US.CNC     | $57.92   |      38.50% | HOLD     | No Action Required
US.CNP     | $42.90   |       1.57% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $42.90
US.CF      | $121.22  |       0.65% | HOLD     | No Action Required
US.CHTR    | $144.76  |     -19.64% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $144.76
US.CVX     | $187.61  |       2.22% | HOLD     | No Action Required
US.CMG     | $32.26   |      -5.71% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $32.26
US.CB      | $326.45  |       0.10% | HOLD     | No Action Required
US.CHD     | $97.00   |       2.42% | HOLD     | No Action Required
US.CI      | $280.73  |       1.84% | HOLD     | No Action Required
US.CINF    | $167.55  |       1.87% | HOLD     | No Action Required
US.CTAS    | $170.78  |      -2.65% | HOLD     | No Action Required
US.CSCO    | $118.26  |      32.86% | HOLD     | No Action Required
US.C       | $125.94  |      -1.12% | HOLD     | No Action Required
US.CFG     | $63.24   |      -0.15% | HOLD     | No Action Required
US.CLX     | $96.41   |      -2.30% | HOLD     | No Action Required
US.CME     | $283.73  |      -0.47% | HOLD     | No Action Required
US.CMS     | $74.31   |      -1.82% | HOLD     | No Action Required
US.KO      | $80.46   |       5.00% | HOLD     | No Action Required
US.CTSH    | $52.14   |      -4.72% | HOLD     | No Action Required
US.CL      | $90.50   |       6.91% | HOLD     | No Action Required
US.CMCSA   | $25.05   |      -9.09% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $25.05
US.CMA     | ERROR     | N/A          | ERROR    | Reason: Unknown stock CMA
US.CAG     | $13.22   |      -4.35% | HOLD     | No Action Required
US.COP     | $118.33  |      -2.09% | HOLD     | No Action Required
US.ED      | $107.85  |      -0.28% | HOLD     | No Action Required
US.STZ     | $144.00  |      -7.08% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $144.00
US.CEG     | $304.28  |      -2.80% | HOLD     | No Action Required
US.COO     | $62.49   |      -3.00% | HOLD     | No Action Required
US.CPRT    | $33.05   |      -0.08% | HOLD     | No Action Required
US.GLW     | $197.97  |      12.55% | HOLD     | No Action Required
US.CPAY    | $345.30  |      10.35% | HOLD     | No Action Required
US.CTVA    | $79.63   |      -0.21% | HOLD     | No Action Required
US.CSGP    | $33.14   |      -9.06% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $33.14
US.COST    | $1001.39 |      -0.82% | HOLD     | No Action Required
US.CTRA    | ERROR     | N/A          | ERROR    | Reason: Unknown stock CTRA
US.CRWD    | $674.95  |      50.61% | HOLD     | No Action Required
US.CCI     | $90.91   |       5.29% | HOLD     | No Action Required
US.CSX     | $46.34   |       2.04% | HOLD     | No Action Required
US.CMI     | $658.84  |       0.02% | HOLD     | No Action Required
US.CVS     | $91.47   |      17.36% | HOLD     | No Action Required
US.DHR     | $171.73  |      -3.11% | HOLD     | No Action Required
US.DRI     | $202.39  |       0.66% | HOLD     | No Action Required
US.DVA     | $197.58  |      30.12% | HOLD     | No Action Required
US.DAY     | ERROR     | N/A          | ERROR    | Reason: Unknown stock DAY
US.DECK    | $109.45  |       0.85% | HOLD     | No Action Required
US.DE      | $527.13  |      -6.31% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $527.13
US.DAL     | $78.75   |      15.35% | HOLD     | No Action Required
US.DVN     | $46.33   |      -3.36% | HOLD     | No Action Required
US.DXCM    | $72.52   |      17.78% | HOLD     | No Action Required
US.FANG    | $199.10  |       2.78% | HOLD     | No Action Required
US.DLR     | $193.35  |      -3.32% | HOLD     | No Action Required
US.DFS     | ERROR     | N/A          | ERROR    | Reason: Unknown stock DFS
US.DG      | $103.07  |     -14.61% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $103.07
US.DLTR    | $92.42   |     -10.92% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $92.42
US.D       | $67.61   |       8.04% | HOLD     | No Action Required
US.DPZ     | $314.43  |     -14.52% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $314.43
US.DOV     | $212.72  |      -5.37% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $212.72
US.DOW     | $35.39   |      -8.46% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $35.39
US.DHI     | $144.41  |      -9.41% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $144.41
US.DTE     | $144.69  |      -1.49% | HOLD     | No Action Required
US.DUK     | $125.35  |      -0.66% | HOLD     | No Action Required
US.DD      | $49.26   |       6.75% | HOLD     | No Action Required
US.EMN     | $73.97   |       2.74% | HOLD     | No Action Required
US.ETN     | $407.79  |      -3.54% | HOLD     | No Action Required
US.EBAY    | $115.46  |      17.89% | HOLD     | No Action Required
US.ECL     | $252.44  |      -6.32% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $252.44
US.EIX     | $70.95   |       3.04% | HOLD     | No Action Required
US.EW      | $86.82   |       3.17% | HOLD     | No Action Required
US.EA      | $200.70  |      -0.97% | HOLD     | No Action Required
US.ELV     | $387.32  |      12.35% | HOLD     | No Action Required
US.EMR     | $138.73  |      -1.46% | HOLD     | No Action Required
US.ENPH    | $67.45   |      88.57% | HOLD     | No Action Required
US.EOG     | $139.03  |       4.43% | HOLD     | No Action Required
US.EPAM    | $101.01  |     -15.10% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $101.01
US.EQT     | $56.82   |      -3.28% | HOLD     | No Action Required
US.EFX     | $163.77  |      -4.72% | HOLD     | No Action Required
US.EQIX    | $1082.36 |      -1.90% | HOLD     | No Action Required
US.EQR     | $66.32   |       6.52% | HOLD     | No Action Required
US.ESS     | $276.56  |       8.30% | HOLD     | No Action Required
US.EL      | $88.09   |      13.20% | HOLD     | No Action Required
US.ETR     | $112.15  |      -0.77% | HOLD     | No Action Required
US.EOG     | $139.03  |       4.43% | HOLD     | No Action Required
US.EVRG    | $84.01   |       4.29% | HOLD     | No Action Required
US.ES      | $69.58   |       2.57% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $69.58
US.EXC     | $46.23   |      -1.47% | HOLD     | No Action Required
US.EXPE    | $221.32  |     -11.98% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $221.32
US.EXPD    | $160.56  |       8.81% | HOLD     | No Action Required
US.EXR     | $143.65  |       1.10% | HOLD     | No Action Required
US.XOM     | $151.81  |       2.64% | HOLD     | No Action Required
US.FFIV    | $396.04  |      30.64% | HOLD     | No Action Required
US.FDS     | $233.83  |       4.33% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $233.83
US.FICO    | $1248.85 |      24.30% | HOLD     | No Action Required
US.FAST    | $44.07   |      -0.86% | HOLD     | No Action Required
US.FRT     | $119.82  |       7.91% | HOLD     | No Action Required
US.FDX     | $398.50  |       2.71% | HOLD     | No Action Required
US.FIS     | $42.35   |      -7.39% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $42.35
US.FITB    | $49.85   |       0.38% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $49.85
US.FSLR    | $273.17  |      40.98% | HOLD     | No Action Required
US.FE      | $46.49   |      -4.93% | HOLD     | No Action Required
US.FI      | ERROR     | N/A          | ERROR    | Reason: Unknown stock FI
US.FLT     | ERROR     | N/A          | ERROR    | Reason: Unknown stock FLT
US.FMC     | $13.12   |     -11.83% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $13.12
US.F       | $15.22   |      24.49% | HOLD     | No Action Required
US.FTNT    | $134.59  |      59.58% | HOLD     | No Action Required
US.FTV     | $59.84   |      -2.05% | HOLD     | No Action Required
US.FOXA    | $64.36   |       2.40% | HOLD     | No Action Required
US.FOX     | $57.56   |       2.48% | HOLD     | No Action Required
US.BEN     | $31.43   |      15.89% | HOLD     | No Action Required
US.FCX     | $63.98   |       4.80% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $63.98
US.GRMN    | $238.87  |      -7.91% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $238.87
US.IT      | $159.16  |       5.72% | HOLD     | No Action Required
US.GE      | $311.31  |       9.39% | HOLD     | No Action Required
US.GEHC    | $64.61   |      -6.13% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $64.61
US.GEV     | $1075.67 |      -6.40% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $1075.67
US.GEN     | $24.93   |      31.61% | HOLD     | No Action Required
US.GNRC    | $275.31  |      24.62% | HOLD     | No Action Required
US.GD      | $343.19  |       9.57% | HOLD     | No Action Required
US.GIS     | $33.41   |      -4.45% | HOLD     | No Action Required
US.GM      | $79.39   |       1.72% | HOLD     | No Action Required
US.GPC     | $96.72   |     -11.05% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $96.72
US.GILD    | $135.18  |       3.67% | HOLD     | No Action Required
US.GPN     | $73.30   |       8.17% | HOLD     | No Action Required
US.GL      | $156.38  |       2.50% | HOLD     | No Action Required
US.GS      | $992.37  |       7.06% | HOLD     | No Action Required
US.HAL     | $41.36   |       2.48% | HOLD     | No Action Required
US.HIG     | $134.90  |       0.33% | HOLD     | No Action Required
US.HAS     | $89.44   |      -5.94% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $89.44
US.HCA     | $390.86  |      -9.62% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $390.86
US.PEAK    | ERROR     | N/A          | ERROR    | Reason: Unknown stock PEAK
US.HSIC    | $73.98   |      -4.59% | HOLD     | No Action Required
US.HSY     | $192.86  |       1.50% | HOLD     | No Action Required
US.HES     | ERROR     | N/A          | ERROR    | Reason: Unknown stock HES
US.HPE     | $38.06   |      35.16% | HOLD     | No Action Required
US.HLT     | $323.00  |      -3.72% | HOLD     | No Action Required
US.HOLX    | ERROR     | N/A          | ERROR    | Reason: Unknown stock HOLX
US.HD      | $309.82  |      -7.76% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $309.82
US.HON     | $232.15  |       9.50% | HOLD     | No Action Required
US.HRL     | $20.92   |      -2.92% | HOLD     | No Action Required
US.HST     | $22.89   |       9.52% | HOLD     | No Action Required
US.HWM     | $259.27  |       6.99% | HOLD     | No Action Required
US.HPQ     | $24.35   |      23.04% | HOLD     | No Action Required
US.HUBB    | $476.82  |     -13.79% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $476.82
US.HUM     | $302.91  |      40.74% | HOLD     | No Action Required
US.HBAN    | $15.99   |      -2.47% | HOLD     | No Action Required
US.HII     | $320.44  |     -10.81% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $320.44
US.IBM     | $249.10  |       8.17% | HOLD     | No Action Required
US.IEX     | $210.14  |       3.00% | HOLD     | No Action Required
US.IDXX    | $555.40  |      -1.86% | HOLD     | No Action Required
US.ITW     | $250.12  |      -7.12% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $250.12
US.ILMN    | $145.45  |      13.74% | HOLD     | No Action Required
US.INCY    | $96.97   |       2.45% | HOLD     | No Action Required
US.IR      | $71.56   |     -14.59% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $71.56
US.PODD    | $154.78  |     -18.35% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $154.78
US.INTC    | $121.72  |      47.47% | HOLD     | No Action Required
US.ICE     | $150.58  |      -4.97% | HOLD     | No Action Required
US.IFF     | $75.83   |       6.59% | HOLD     | No Action Required
US.IP      | $31.74   |      -1.34% | HOLD     | No Action Required
US.IPG     | ERROR     | N/A          | ERROR    | Reason: Unknown stock IPG
US.INTU    | $308.10  |     -22.19% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $308.10
US.ISRG    | $436.52  |      -9.48% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $436.52
US.IVZ     | $27.43   |       8.39% | HOLD     | No Action Required
US.INVH    | $29.36   |       8.24% | HOLD     | No Action Required
US.IQV     | $162.15  |      -0.08% | HOLD     | No Action Required
US.IRM     | $128.01  |      10.33% | HOLD     | No Action Required
US.JBHT    | $264.67  |       6.67% | HOLD     | No Action Required
US.JBL     | $376.40  |      10.20% | HOLD     | No Action Required
US.JKHY    | $137.71  |      -8.89% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $137.71
US.J       | $116.47  |      -7.71% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $116.47
US.JNJ     | $229.96  |       1.66% | HOLD     | No Action Required
US.JCI     | $139.52  |      -1.69% | HOLD     | No Action Required
US.JPM     | $306.99  |      -0.42% | HOLD     | No Action Required
US.JNPR    | ERROR     | N/A          | ERROR    | Reason: Unknown stock JNPR
US.K       | ERROR     | N/A          | ERROR    | Reason: Unknown stock K
US.KVUE    | $17.61   |       1.87% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $17.61
US.KMT     | $36.32   |      -6.84% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $36.32
US.KEY     | $21.64   |       0.07% | HOLD     | No Action Required
US.KEYS    | $351.62  |       1.34% | HOLD     | No Action Required
US.KMB     | $99.60   |       1.79% | HOLD     | No Action Required
US.KIM     | $24.25   |       2.38% | HOLD     | No Action Required
US.KMI     | $33.17   |       5.46% | HOLD     | No Action Required
US.KLAC    | $1973.00 |       2.09% | HOLD     | No Action Required
US.KHC     | $23.91   |       9.00% | HOLD     | No Action Required
US.KR      | $65.50   |      -2.07% | HOLD     | No Action Required
US.LHX     | $311.29  |      -1.96% | HOLD     | No Action Required
US.LH      | $259.05  |      -1.80% | HOLD     | No Action Required
US.LRCX    | $313.73  |      17.16% | HOLD     | No Action Required
US.LW      | $42.48   |      -3.29% | HOLD     | No Action Required
US.LVS     | $50.05   |      -4.68% | HOLD     | No Action Required
US.LDOS    | $127.22  |     -12.90% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $127.22
US.LEN     | $88.80   |      -5.58% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $88.80
US.LLY     | $1077.95 |      22.16% | HOLD     | No Action Required
US.LIN     | $513.36  |       0.60% | HOLD     | No Action Required
US.LYV     | $166.41  |       6.24% | HOLD     | No Action Required
US.LKQ     | $26.82   |     -14.13% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $26.82
US.LMT     | $531.67  |       3.55% | HOLD     | No Action Required
US.LNC     | $35.79   |      -3.19% | HOLD     | No Action Required
US.LIN     | $513.36  |       0.60% | HOLD     | No Action Required
US.LYB     | $69.47   |      -0.57% | HOLD     | No Action Required
US.MTB     | $214.88  |      -0.02% | HOLD     | No Action Required
US.MRO     | ERROR     | N/A          | ERROR    | Reason: Unknown stock MRO
US.MPC     | $257.05  |      15.12% | HOLD     | No Action Required
US.MKTX    | $132.01  |     -18.66% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $132.01
US.MAR     | $372.76  |       1.73% | HOLD     | No Action Required
US.MMC     | ERROR     | N/A          | ERROR    | Reason: Unknown stock MMC
US.MLM     | $550.43  |     -10.54% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $550.43
US.MAS     | $67.78   |      -8.19% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $67.78
US.MA      | $493.24  |      -2.17% | HOLD     | No Action Required
US.MTCH    | $35.53   |      -3.32% | HOLD     | No Action Required
US.MAT     | $15.23   |       4.77% | HOLD     | No Action Required
US.MKC     | $46.76   |      -9.26% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $46.76
US.MCD     | $280.51  |      -6.30% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $280.51
US.MCK     | $754.85  |      -8.85% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $754.85
US.MDT     | $77.67   |      -6.78% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $77.67
US.MRK     | $120.56  |       7.74% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $120.56
US.META    | $608.16  |      -9.91% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $608.16
US.MET     | $83.48   |       8.26% | HOLD     | No Action Required
US.MTD     | $1098.41 |     -14.35% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $1098.41
US.MGM     | $38.42   |      -2.83% | HOLD     | No Action Required
US.MCHP    | $97.46   |       9.51% | HOLD     | No Action Required
US.MU      | $870.80  |      75.31% | HOLD     | No Action Required
US.MSFT    | $415.65  |      -1.90% | HOLD     | No Action Required
US.MAA     | $130.75  |       4.05% | HOLD     | No Action Required
US.MRNA    | $47.72   |      -5.93% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $47.72
US.MHK     | $103.15  |      -4.26% | HOLD     | No Action Required
US.MOH     | $175.49  |      -0.26% | HOLD     | No Action Required
US.TAP     | $40.93   |      -3.56% | HOLD     | No Action Required
US.MDLZ    | $61.86   |       7.38% | HOLD     | No Action Required
US.MPWR    | $1670.37 |       2.35% | HOLD     | No Action Required
US.MNST    | $87.14   |      11.39% | HOLD     | No Action Required
US.MCO     | $450.80  |      -0.92% | HOLD     | No Action Required
US.MS      | $200.75  |       7.32% | HOLD     | No Action Required
US.MOS     | $22.71   |      -4.39% | HOLD     | No Action Required
US.MSI     | $410.26  |      -6.39% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $410.26
US.MSCI    | $587.67  |      -0.49% | HOLD     | No Action Required
US.NDAQ    | $91.04   |       1.27% | HOLD     | No Action Required
US.NTAP    | $138.20  |      27.13% | HOLD     | No Action Required
US.NFLX    | $87.82   |      -5.00% | HOLD     | No Action Required
US.NEM     | $110.69  |      -8.30% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $110.69
US.NWL     | $3.63    |     -14.18% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $3.63
US.NWR     | ERROR     | N/A          | ERROR    | Reason: Unknown stock NWR
US.NWSA    | $25.87   |      -1.26% | HOLD     | No Action Required
US.NWS     | $29.62   |      -2.03% | HOLD     | No Action Required
US.NEE     | $87.96   |      -7.68% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $87.96
US.NKE     | $44.61   |      -0.18% | HOLD     | No Action Required
US.NI      | $47.79   |       0.21% | HOLD     | No Action Required
US.NDSN    | $287.56  |       1.84% | HOLD     | No Action Required
US.NSC     | $319.28  |       0.30% | HOLD     | No Action Required
US.NTRS    | $168.73  |       2.88% | HOLD     | No Action Required
US.NOC     | $552.93  |      -3.86% | HOLD     | No Action Required
US.NCLH    | $16.91   |      -8.67% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $16.91
US.NRG     | $139.62  |     -12.37% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $139.62
US.NUE     | $238.71  |      11.39% | HOLD     | No Action Required
US.NVDA    | $213.53  |       2.53% | HOLD     | No Action Required
US.NVR     | $6095.04 |      -6.29% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $6095.04
US.NXPI    | $327.32  |      34.13% | HOLD     | No Action Required
US.ORLY    | $88.17   |      -5.32% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $88.17
US.OXY     | $58.88   |       3.07% | HOLD     | No Action Required
US.ODFL    | $215.03  |      -2.25% | HOLD     | No Action Required
US.OMC     | $74.50   |      -1.64% | HOLD     | No Action Required
US.OKE     | $91.72   |       6.08% | HOLD     | No Action Required
US.ORCL    | $192.19  |      10.92% | HOLD     | No Action Required
US.OTIS    | $72.42   |      -6.53% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $72.42
US.PCAR    | $110.47  |     -12.75% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $110.47
US.PKG     | $216.35  |       1.63% | HOLD     | No Action Required
US.PANW    | $258.82  |      44.96% | HOLD     | No Action Required
US.PARA    | ERROR     | N/A          | ERROR    | Reason: Unknown stock PARA
US.PH      | $864.70  |     -11.06% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $864.70
US.PAYX    | $96.03   |       8.29% | HOLD     | No Action Required
US.PAYC    | $136.02  |      10.24% | HOLD     | No Action Required
US.PYPL    | $44.06   |     -12.72% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $44.06
US.PNR     | $74.14   |     -19.20% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $74.14
US.PEP     | $147.10  |      -5.37% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $147.10
US.PFE     | $25.77   |      -2.96% | HOLD     | No Action Required
US.PCG     | $16.43   |      -1.11% | HOLD     | No Action Required
US.PM      | $183.77  |      11.92% | HOLD     | No Action Required
US.PSX     | $178.17  |      10.20% | HOLD     | No Action Required
US.PNW     | $102.70  |       1.28% | HOLD     | No Action Required
US.PXD     | ERROR     | N/A          | ERROR    | Reason: Unknown stock PXD
US.PNC     | $219.92  |       0.03% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $219.92
US.POOL    | $182.00  |     -21.15% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $182.00
US.PPG     | $109.25  |       0.15% | HOLD     | No Action Required
US.PPL     | $35.81   |      -7.57% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $35.81
US.PFG     | $104.43  |       5.12% | HOLD     | No Action Required
US.PG      | $143.84  |      -2.93% | HOLD     | No Action Required
US.PGR     | $198.00  |      -1.44% | HOLD     | No Action Required
US.PLD     | $146.82  |       3.32% | HOLD     | No Action Required
US.PRU     | $102.64  |      10.43% | HOLD     | No Action Required
US.PEG     | $80.41   |      -0.41% | HOLD     | No Action Required
US.PTC     | $145.54  |       6.10% | HOLD     | No Action Required
US.PSA     | $305.70  |      -0.84% | HOLD     | No Action Required
US.PHM     | $116.28  |      -8.84% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $116.28
US.PWR     | $738.73  |      18.23% | HOLD     | No Action Required
US.QCOM    | $249.35  |      67.52% | HOLD     | No Action Required
US.DGX     | $193.04  |      -1.64% | HOLD     | No Action Required
US.RL      | $387.97  |       4.51% | HOLD     | No Action Required
US.RJF     | $151.89  |      -1.00% | HOLD     | No Action Required
US.RTX     | $177.63  |       2.36% | HOLD     | No Action Required
US.O       | $62.16   |      -1.43% | HOLD     | No Action Required
US.REG     | $78.77   |      -1.77% | HOLD     | No Action Required
US.REGN    | $641.45  |     -14.52% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $641.45
US.RF      | $28.07   |       1.13% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $28.07
US.RSG     | $206.57  |      -1.53% | HOLD     | No Action Required
US.RMD     | $209.17  |      -4.58% | HOLD     | No Action Required
US.RVMD    | $153.72  |      13.61% | HOLD     | No Action Required
US.RHI     | $27.31   |       9.00% | HOLD     | No Action Required
US.ROK     | $452.68  |      13.19% | HOLD     | No Action Required
US.ROL     | $53.01   |      -6.02% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $53.01
US.ROP     | $320.97  |      -9.18% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $320.97
US.ROST    | $233.80  |       3.28% | HOLD     | No Action Required
US.RCL     | $266.37  |       0.20% | HOLD     | No Action Required
US.SPGI    | $411.83  |      -5.71% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $411.83
US.CRM     | $182.09  |       2.21% | HOLD     | No Action Required
US.SBAC    | $202.73  |      -7.07% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $202.73
US.SLB     | $58.16   |       3.59% | HOLD     | No Action Required
US.STX     | $843.25  |      43.84% | HOLD     | No Action Required
US.SRE     | $92.05   |      -1.23% | HOLD     | No Action Required
US.NOW     | $101.97  |      13.09% | HOLD     | No Action Required
US.SHW     | $309.48  |      -8.12% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $309.48
US.SPG     | $205.81  |       2.31% | HOLD     | No Action Required
US.SWKS    | $81.81   |      29.65% | HOLD     | No Action Required
US.SJM     | $103.14  |       8.55% | HOLD     | No Action Required
US.SNA     | $369.44  |      -1.71% | HOLD     | No Action Required
US.SOLV    | $75.67   |      10.43% | HOLD     | No Action Required
US.SO      | $94.19   |       1.58% | HOLD     | No Action Required
US.LUV     | $42.03   |       6.55% | HOLD     | No Action Required
US.SWK     | $78.11   |       1.92% | HOLD     | No Action Required
US.SBUX    | $101.84  |       3.82% | HOLD     | No Action Required
US.STT     | $156.79  |       4.01% | HOLD     | No Action Required
US.STLD    | $248.24  |       9.46% | HOLD     | No Action Required
US.STE     | $214.64  |      -3.23% | HOLD     | No Action Required
US.SYK     | $311.02  |      -5.03% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $311.02
US.SMCI    | $36.48   |      25.43% | HOLD     | No Action Required
US.SYF     | $72.56   |      -4.52% | HOLD     | No Action Required
US.SNPS    | $535.38  |       6.90% | HOLD     | No Action Required
US.SYY     | $75.54   |      -1.33% | HOLD     | No Action Required
US.TMUS    | $191.24  |       0.76% | HOLD     | No Action Required
US.TROW    | $103.48  |       4.46% | HOLD     | No Action Required
US.TTWO    | $221.98  |       5.33% | HOLD     | No Action Required
US.TPR     | $139.23  |      -4.57% | HOLD     | No Action Required
US.TRGP    | $271.75  |      13.47% | HOLD     | No Action Required
US.TGT     | $124.64  |      -2.66% | HOLD     | No Action Required
US.TEL     | $210.75  |      -1.45% | HOLD     | No Action Required
US.TDY     | $632.24  |      -2.53% | HOLD     | No Action Required
US.TFX     | $133.31  |      -2.13% | HOLD     | No Action Required
US.TER     | $379.33  |      -9.23% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $379.33
US.TSLA    | $431.00  |      14.53% | HOLD     | No Action Required
US.TXN     | $321.61  |      16.64% | HOLD     | No Action Required
US.TXT     | $92.39   |       5.04% | HOLD     | No Action Required
US.TMO     | $446.71  |      -4.90% | HOLD     | No Action Required
US.TJX     | $158.65  |       1.36% | HOLD     | No Action Required
US.TSCO    | $29.80   |     -18.90% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $29.80
US.TT      | $460.46  |      -5.34% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $460.46
US.TDG     | $1214.15 |       5.75% | HOLD     | No Action Required
US.TRV     | $305.50  |       0.92% | HOLD     | No Action Required
US.TRMB    | $56.16   |     -16.61% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $56.16
US.TFC     | $48.51   |      -3.37% | HOLD     | No Action Required
US.TYL     | $310.34  |      -9.27% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $310.34
US.TSN     | $65.50   |       2.30% | HOLD     | No Action Required
US.USB     | $54.91   |      -1.21% | HOLD     | No Action Required
US.UBER    | $70.52   |      -5.52% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $70.52
US.UDR     | $38.10   |       9.58% | HOLD     | No Action Required
US.ULTA    | $515.87  |      -7.64% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $515.87
US.UNP     | $271.08  |       0.89% | HOLD     | No Action Required
US.UAL     | $105.66  |      13.61% | BUY      | ⚠️ DRY RUN: Would BUY 10 shares @ $105.66
US.UPS     | $101.72  |      -3.35% | HOLD     | No Action Required
US.URI     | $955.35  |      -1.75% | HOLD     | No Action Required
US.UNH     | $378.42  |       6.62% | HOLD     | No Action Required
US.UHS     | $156.87  |     -10.03% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $156.87
US.VLO     | $247.84  |       5.59% | HOLD     | No Action Required
US.VTR     | $87.61   |       4.77% | HOLD     | No Action Required
US.VRSN    | $309.36  |      15.22% | HOLD     | No Action Required
US.VRSK    | $169.45  |      -4.58% | HOLD     | No Action Required
US.VZ      | $48.24   |       4.02% | HOLD     | No Action Required
US.VRTX    | $436.66  |       1.48% | HOLD     | No Action Required
US.VFC     | $16.40   |     -17.13% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $16.40
US.VTRS    | $16.43   |      13.40% | HOLD     | No Action Required
US.VICI    | $28.47   |       0.18% | HOLD     | No Action Required
US.V       | $326.18  |       5.64% | HOLD     | No Action Required
US.VMC     | $266.00  |      -8.74% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $266.00
US.WRB     | $67.41   |       1.32% | HOLD     | No Action Required
US.WAB     | $259.90  |      -2.56% | HOLD     | No Action Required
US.WBA     | ERROR     | N/A          | ERROR    | Reason: Unknown stock WBA
US.WMT     | $118.76  |      -8.42% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $118.76
US.WBD     | $26.98   |      -0.31% | HOLD     | No Action Required
US.WM      | $215.99  |      -5.90% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $215.99
US.WAT     | $339.62  |       9.60% | HOLD     | No Action Required
US.WEC     | $113.23  |      -0.35% | HOLD     | No Action Required
US.WFC     | $77.31   |      -2.11% | HOLD     | No Action Required
US.WELL    | $216.20  |       3.92% | HOLD     | No Action Required
US.WST     | $316.96  |       3.61% | HOLD     | No Action Required
US.WDC     | $528.59  |      30.84% | HOLD     | No Action Required
US.WRK     | ERROR     | N/A          | ERROR    | Reason: Unknown stock WRK
US.WY      | $23.80   |      -4.89% | HOLD     | No Action Required
US.WHR     | $42.68   |     -20.67% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $42.68
US.WMB     | $76.86   |       6.49% | HOLD     | No Action Required
US.GWW     | $1244.37 |       8.61% | HOLD     | No Action Required
US.WYNN    | $98.31   |      -6.72% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $98.31
US.XEL     | $80.94   |       2.26% | HOLD     | No Action Required
US.XYL     | $111.07  |      -8.55% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $111.07
US.YUM     | $155.25  |      -3.14% | HOLD     | No Action Required
US.ZBRA    | $252.15  |      10.73% | HOLD     | No Action Required
US.ZBH     | $84.48   |      -7.43% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $84.48
US.ZTS     | $80.73   |     -30.92% | SELL     | ⚠️ DRY RUN: Would SELL 10 shares @ $80.73
---

## 💻 Technical Implementation

```python
import pandas as pd
import numpy as np
from moomoo import *
import time
from datetime import datetime, timedelta

OPEND_HOST = "127.0.0.1"
OPEND_PORT = 11113
SHARE_QUANTITY_PER_ORDER = 10

MY_WATCHLIST = [
    "US.NVDA", "US.AVGO", "US.INTC", "US.DELL", "US.SNDK",
    "US.PLTR", "US.MSFT", "US.ORCL", "US.NOW", "US.WDAY",
    "US.ADBE", "US.BA", "US.GE", "US.AAPL", "US.AMZN",
    "US.UBER", "US.BE"
]

def evaluate_daily_momentum(df):
    if len(df) < 55:
        return "HOLD"

    df['EMA12'] = df['close'].ewm(span=12, adjust=False).mean()
    df['EMA50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['ROC_1M'] = df['close'].pct_change(periods=21) * 100

    latest_bar = df.iloc[-1]
    prior_bar = df.iloc[-2]

    is_bullish_crossover = (prior_bar['EMA12'] <= prior_bar['EMA50']) and (latest_bar['EMA12'] > latest_bar['EMA50'])
    is_bearish_crossover = (prior_bar['EMA12'] >= prior_bar['EMA50']) and (latest_bar['EMA12'] < latest_bar['EMA50'])

    if is_bullish_crossover and latest_bar['ROC_1M'] > 0:
        return "BUY"
    elif is_bearish_crossover or latest_bar['ROC_1M'] < -5:
        return "SELL"

    return "HOLD"

def print_moomoo_quota_status(quote_ctx):
    print("=" * 75)
    print("               MOOMOO API QUOTA & ACCOUNT DIAGNOSTICS              ")
    print("=" * 75)
    ret_code, data = quote_ctx.get_history_kl_quota()
    if ret_code == RET_OK:
        print(f" -> Used Quota Stock Count : {data[0]}")
        print(f" -> Remaining Stock Quota  : {data[1]}")
    else:
        print(f" ⚠️ CRITICAL: Error fetching status: {data}")
    print("=" * 75 + "\n")

def execute_momentum_strategy():
    quote_ctx = OpenQuoteContext(host=OPEND_HOST, port=OPEND_PORT)
    trade_ctx = OpenSecTradeContext(host=OPEND_HOST, port=OPEND_PORT)

    print_moomoo_quota_status(quote_ctx)

    print("=" * 75)
    print("               MOOMOO MOMENTUM SCANNER (DRY RUN ONLY)              ")
    print("=" * 75)
    print(f"{'SYMBOL':<10} | {'CLOSE':<9} | {'1M MOMENTUM':<12} | {'SIGNAL':<8} | {'PROPOSED ORDER'}")
    print("-" * 75)

    end_date_str = datetime.today().strftime('%Y-%m-%d')
    start_date_str = (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d')

    try:
        for symbol in MY_WATCHLIST:
            ret_code, data, page_req_key = quote_ctx.request_history_kline(
                code=symbol, start=start_date_str, end=end_date_str, ktype=KLType.K_DAY
            )

            if ret_code != RET_OK:
                print(f"{symbol:<10} | ERROR     | N/A          | ERROR    | Reason: {data}")
                continue

            if not isinstance(data, pd.DataFrame) or data.empty:
                print(f"{symbol:<10} | NO_DATA   | N/A          | SKIP     | Empty payload.")
                continue

            df = data
            action_signal = evaluate_daily_momentum(df)
            current_close = float(df['close'].iloc[-1])
            momentum_val = df['ROC_1M'].iloc[-1]
            
            momentum_str = f"{'N/A':>11}" if pd.isna(momentum_val) else f"{momentum_val:>10.2f}%"

            if action_signal == "BUY":
                order_display = f"⚠️ DRY RUN: Would BUY {SHARE_QUANTITY_PER_ORDER} shares @ \${current_close:.2f}"
            elif action_signal == "SELL":
                order_display = f"⚠️ DRY RUN: Would SELL {SHARE_QUANTITY_PER_ORDER} shares @ \${current_close:.2f}"
            else:
                order_display = "No Action Required"

            print(f"{symbol:<10} | \${current_close:<7.2f} | {momentum_str} | {action_signal:<8} | {order_display}")
            time.sleep(0.5)

    except Exception as general_err:
        print(f"\n[CRITICAL ERROR]: {general_err}")
    finally:
        quote_ctx.close()
        trade_ctx.close()
        print("=" * 75)
        print("ALGORITHM SCAN COMPLETE: API contexts cleanly terminated.")
        print("=" * 75)

if __name__ == "__main__":
    execute_momentum_strategy()
```

## ⚙️ Requirements & Local Setup

1. **Infrastructure**: Running local instance of the desktop **Moomoo OpenD** client application.
2. **Authentication**: Account credentials must maintain verified market access privileges for US Equities.
3. **Environment**:
   ```bash
   pip install pandas numpy moomoo-api
   ```
