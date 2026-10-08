# P&L Analyzer

revenue = float(input("Enter total revenue: ₹"))
cogs = float(input("Enter cost of goods sold: ₹"))
operating_expenses = float(input("Enter operating expenses: ₹"))

gross_profit = revenue - cogs
net_profit = gross_profit - operating_expenses

gross_margin = (gross_profit / revenue) * 100
net_margin = (net_profit / revenue) * 100

print("\n--- P&L RESULTS ---")
print(f"Revenue: ₹{revenue:.2f}")
print(f"COGS: ₹{cogs:.2f}")
print(f"Gross Profit: ₹{gross_profit:.2f}")
print(f"Operating Expenses: ₹{operating_expenses:.2f}")
print(f"Net Profit: ₹{net_profit:.2f}")
print(f"Gross Profit Margin: {gross_margin:.2f}%")
print(f"Net Profit Margin: {net_margin:.2f}%")
