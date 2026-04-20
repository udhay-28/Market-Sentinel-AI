## 🚀 Progress Log

### Day 4: Global Wealth Engine (April 20, 2026)
- **Feature:** Multi-Currency Portfolio Calibration.
- **Innovation:** Integrated live `USDINR=X` exchange rate fetching to unify global assets.
- **Logic:** Built a conversion engine to calculate total net worth across international (USD) and domestic (INR) markets.
- **Status:** System now provides a single "Source of Truth" for total wealth.

### Day 3: The Persistent Vault (April 19, 2026 - Backfilled)
- **Feature:** Historical Data Logging.
- **Tools:** Implemented Python `csv` module for local database management.
- **Function:** Added automated writing to `sentinel_vault.csv` to track P/L (Profit/Loss) over time.
- **Interface:** Created a continuous `while True` loop for multi-ticker manual entry.

### Day 2: Advanced Price Fetching (April 18, 2026)
- Improved error handling for invalid tickers using `try/except`.
- Formatted terminal output for better readability.

### Day 1: The Pulse (April 17, 2026)
- Initialized connection to Yahoo Finance API.
- Basic real-time price fetching for TSLA and NVDA.
