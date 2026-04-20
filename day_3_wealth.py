import yfinance as yf

portfolio = {
    "BTC-USD": 0.05,    
    "NVDA": 10,         
    "RELIANCE.NS": 50,  
    "TCS.NS": 20       
}

try:
    print(f"\n{'='*50}")
    print(f"{'🚀 DAY 3: GLOBAL WEALTH CALIBRATION':^50}")
    print(f"{'='*50}\n")

    exchange_data = yf.Ticker("USDINR=X").history(period="1d")
    usd_to_inr = exchange_data['Close'].iloc[-1]

    total_net_worth_inr = 0

    for ticker, amount in portfolio.items():
        data = yf.Ticker(ticker).history(period="1d")
        
        if data.empty:
            print(f"❌ Error: {ticker} not found.")
            continue
            
        price = data['Close'].iloc[-1]
        
        if ".NS" in ticker:
            value_inr = price * amount
        else:
            value_inr = (price * amount) * usd_to_inr
            
        total_net_worth_inr += value_inr
        print(f"✅ {ticker:<12} | Value: ₹{value_inr:>11.2f}")

    print(f"\n{'='*50}")
    print(f"💰 LIVE USD/INR RATE: ₹{usd_to_inr:.2f}")
    print(f"🏆 TOTAL NET WORTH:    ₹{total_net_worth_inr:,.2f}")
    print(f"{'='*50}\n")

except Exception as e:
    print(f"❌ Error: {e}")