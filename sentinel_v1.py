print("--- WELCOME TO THE MARKET SENTINEL ---")
active = True

while active:
    try:
        stock = input("\nEnter stock name (or type 'quit' to exit): ")
        
        if stock.lower() == 'quit':
            active = False
            print("Shutting down system... Goodbye, Architect.")
            break

        price = float(input(f"Current price of {stock}: "))
        shares = int(input(f"Number of shares: "))

        total = price * shares
        print(f"Checking {stock}... Total value: ${total:.2f}")

        if total > 5000:
            print("⚠️ ALERT: High Exposure!")
        elif total < 1000:
            print("ℹ️ INFO: Small position. Consider adding.")
        else:
            print("✅ OK: Healthy position size.")

    except ValueError:
        print("❌ ERROR: Invalid numbers. Try again.")