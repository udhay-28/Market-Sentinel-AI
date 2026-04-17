import csv
from datetime import datetime

while True:
    stock_name = input("Enter the Stock Name(or just type exit to quit):")

    if stock_name.lower() == "exit":
        print("Closing System...GOODBYE ARCHITECT")
        break

    try:
        buy_price = float(input("Enter Buy Price:"))
        current_price = float(input("Enter Current Price:"))

        percentage_change = ((current_price-buy_price)/buy_price) * 100
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if percentage_change > 10:
            status = "PROFIT"
            advice = "Sell Some!"

        elif percentage_change < -5:
            status="LOSS"
            advice="Exit Now!!"
        else:
            status="HOLD"
            advice="Stay Calm"

        print(f"{[status]} stock_name: {percentage_change:.2f}% -> {advice}")
        
        with open("sentinel_v1.csv","a",newline="") as vault:
            writer = csv.writer(vault)
            writer.writerow([timestamp , buy_price , current_price , f"{percentage_change:.2f}%" , status])

    except ValueError:
        print("ERROR : Please Type Numbers Only")
    except ZeroDivisionError:
        print("ERROR : Buy Price Cannot Be Zero")     

