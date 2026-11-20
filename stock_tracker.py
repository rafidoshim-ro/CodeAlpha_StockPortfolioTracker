"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
Concepts used: dictionary, input/output, basic arithmetic, file handling
"""

import csv
from datetime import datetime

# Hardcoded stock prices (USD per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    print("-" * 28)
    for name, price in STOCK_PRICES.items():
        print(f"{name:<8} ${price:>8.2f}")
    print("-" * 28)


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict {stock: qty}."""
    portfolio = {}
    print("\nEnter your stocks. Type 'done' when finished.")

    while True:
        name = input("\nStock name (or 'done'): ").strip().upper()

        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print(f"'{name}' is not available. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a positive whole number for quantity.")
            continue

        # If the same stock is entered twice, add to existing quantity
        portfolio[name] = portfolio.get(name, 0) + int(qty_text)
        print(f"Added {qty_text} x {name}.")

    return portfolio


def calculate_investments(portfolio):
    """Return (list of rows, total value)."""
    rows = []
    total = 0
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * qty
        rows.append((name, qty, price, value))
        total += value
    return rows, total


def print_summary(rows, total):
    print("\n" + "=" * 46)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>16}")
    print("=" * 46)
    for name, qty, price, value in rows:
        print(f"{name:<8}{qty:>6}{price:>12.2f}{value:>16.2f}")
    print("=" * 46)
    print(f"{'TOTAL INVESTMENT:':<26}{total:>20.2f}")
    print("=" * 46)


def save_to_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
        f.write(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>16}\n")
        for name, qty, price, value in rows:
            f.write(f"{name:<8}{qty:>6}{price:>12.2f}{value:>16.2f}\n")
        f.write(f"\nTotal Investment: ${total:.2f}\n")
    print(f"Saved to {filename}")


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    rows, total = calculate_investments(portfolio)
    print_summary(rows, total)

    choice = input("\nSave result? (txt / csv / both / no): ").strip().lower()
    if choice in ("txt", "both"):
        save_to_txt(rows, total)
    if choice in ("csv", "both"):
        save_to_csv(rows, total)


if __name__ == "__main__":
    main()
