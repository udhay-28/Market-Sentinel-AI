import yfinance as yf

targets = {
    "TSLA": 250.00, 
    "BTC-USD": 85000.00,
    "RELIANCE.NS": 3200.00
}

print("--- 🔔 SENTINEL ALERT SYSTEM ACTIVE ---")

for ticker, target_price in targets.items():
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    
    print(f"Checking {ticker}... Current: {current_price:.2f} | Target: {target_price:.2f}")

    if current_price >= target_price:
        print(f"🚀 ALERT: {ticker} has hit your target! TIME TO SELL.")
    else:
        diff = target_price - current_price
        print(f"⏳ Status: Holding. Needs to rise by {diff:.2f} to hit target.")