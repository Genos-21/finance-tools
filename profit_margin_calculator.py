# Profit Margin Calculator

revenue = float(input("Enter total revenue: ₹"))
cost = float(input("Enter total cost: ₹"))

profit = revenue - cost
margin = (profit / revenue) * 100

print(f"\nProfit: ₹{profit:.2f}")
print(f"Profit Margin: {margin:.2f}%")
