import yfinance as yf
import csv
from datetime import datetime

print("--- 🏗️ MARKET SENTINEL v3.0: PERSISTENT GUARD ---")

while True:
    ticker_symbol = input("\nEnter Ticker (e.g., TSLA, NVDA, RELIANCE.NS) or 'exit': ").upper()
    
    if ticker_symbol == 'EXIT':
        print("📴 Shutting down Sentinel... System safe.")
        break

    try:
        print(f"🔍 Searching for {ticker_symbol}...")
        stock = yf.Ticker(ticker_symbol)
        
        data = stock.history(period="1d")
        
        if data.empty:
            print("❌ Error: Ticker not found. Try again.")
            continue 
            
        current_price = data['Close'].iloc[-1]
        
        buy_price = float(input(f"Enter your buy price for {ticker_symbol}: "))

        percentage_change = ((current_price - buy_price) / buy_price) * 100
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        status = "HOLD"
        if percentage_change > 10: status = "PROFIT"
        elif percentage_change < -5: status = "LOSS"

        print(f"✅ Price: ${current_price:.2f} ({percentage_change:.2f}%) -> Status: {status}")
        
        with open("sentinel_vault.csv", "a", newline="") as vault:
            writer = csv.writer(vault)
            writer.writerow([timestamp, ticker_symbol, buy_price, current_price, f"{percentage_change:.2f}%", status])
        
        print("📂 Entry secured in sentinel_vault.csv")

    except Exception as e:
        print(f"❌ System Error: {e}")