def stock_portfolio():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "AMZN": 130,
        "MSFT": 320
    }

    print("📊 Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    portfolio = {}
    total_value = 0

    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        elif stock not in stock_prices:
            print("⚠️ Stock not found. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        investment = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_value += investment
        print(f"Added {quantity} shares of {stock} worth ${investment}")

    print("\n===== 🧾 Portfolio Summary =====")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}")
    print(f"\n💰 Total Investment Value: ${total_value}")

    # Optional: Save to file
    save = input("\nWould you like to save this report to a file? (y/n): ").lower()
    if save == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=======================\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
        print("✅ Report saved as 'portfolio_report.txt'.")

# Run the tracker
stock_portfolio()
