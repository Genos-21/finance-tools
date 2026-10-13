
# Financial Beast - Profit Margin Calculator v2

def get_amount(label):
    while True:
        try:
            amount = float(input(f"{label}: ₹"))

            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue

            return amount

        except ValueError:
            print("Invalid input. Please enter a number.")


print("\n===== PROFIT MARGIN CALCULATOR =====")

# 1. Revenue
revenue = get_amount("\nEnter total revenue")

# 2. Direct costs
print("\n--- DIRECT COSTS ---")

raw_materials = get_amount("Raw materials")
direct_labour = get_amount("Direct labour")
other_direct_costs = get_amount("Other direct costs")

total_direct_costs = (
    raw_materials
    + direct_labour
    + other_direct_costs
)

# 3. Indirect costs
print("\n--- INDIRECT COSTS ---")

administration_cost = get_amount("Administration costs")
selling_cost = get_amount("Selling costs")
marketing_cost = get_amount("Marketing costs")
rent_and_utilities = get_amount("Rent and utilities")
other_indirect_costs = get_amount("Other indirect costs")

total_indirect_costs = (
    administration_cost
    + selling_cost
    + marketing_cost
    + rent_and_utilities
    + other_indirect_costs
)

# 4. Total cost
total_cost = total_direct_costs + total_indirect_costs

# 5. Profit
profit = revenue - total_cost

# 6. Profit margin and markup
if revenue > 0:
    profit_margin = (profit / revenue) * 100
else:
    profit_margin = None

if total_cost > 0:
    markup = (profit / total_cost) * 100
else:
    markup = None

# 7. Display results
print("\n========== COST BREAKDOWN ==========")

print("\n--- DIRECT COSTS ---")
print(f"Raw materials: ₹{raw_materials:,.2f}")
print(f"Direct labour: ₹{direct_labour:,.2f}")
print(f"Other direct costs: ₹{other_direct_costs:,.2f}")
print(f"Total direct costs: ₹{total_direct_costs:,.2f}")

print("\n--- INDIRECT COSTS ---")
print(f"Administration: ₹{administration_cost:,.2f}")
print(f"Selling: ₹{selling_cost:,.2f}")
print(f"Marketing: ₹{marketing_cost:,.2f}")
print(f"Rent and utilities: ₹{rent_and_utilities:,.2f}")
print(f"Other indirect costs: ₹{other_indirect_costs:,.2f}")
print(f"Total indirect costs: ₹{total_indirect_costs:,.2f}")

print("\n========== FINAL RESULTS ==========")
print(f"Revenue: ₹{revenue:,.2f}")
print(f"Total direct costs: ₹{total_direct_costs:,.2f}")
print(f"Total indirect costs: ₹{total_indirect_costs:,.2f}")
print(f"TOTAL COST: ₹{total_cost:,.2f}")
print(f"PROFIT / LOSS: ₹{profit:,.2f}")

if profit_margin is not None:
    print(f"Profit margin: {profit_margin:.2f}%")
else:
    print("Profit margin: Cannot calculate because revenue is zero.")

if markup is not None:
    print(f"Markup on total cost: {markup:.2f}%")
else:
    print("Markup: Cannot calculate because total cost is zero.")

print("\n===== END OF REPORT =====")
