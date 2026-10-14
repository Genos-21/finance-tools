
# Financial Beast - Profit Margin Calculator v3

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


def get_percentage(label):
    while True:
        try:
            percentage = float(input(label))

            if 0 <= percentage <= 100:
                return percentage

            print("Enter a percentage between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


print("\n===== FINANCIAL BEAST =====")
print("===== PROFIT MARGIN CALCULATOR v3 =====")

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

# 4. Total costs and profit before tax
total_cost = total_direct_costs + total_indirect_costs

profit_before_tax = revenue - total_cost

# 5. Calculate tax on positive PBT
print("\n--- TAX CALCULATION ---")
tax_rate = get_percentage("Enter tax rate (%): ")

tax_amount = max(profit_before_tax, 0) * (tax_rate / 100)

# 6. Profit after tax
profit_after_tax = profit_before_tax - tax_amount

# 7. Profit margins and markup
if revenue > 0:
    pbt_margin = (profit_before_tax / revenue) * 100
    pat_margin = (profit_after_tax / revenue) * 100
else:
    pbt_margin = None
    pat_margin = None

if total_cost > 0:
    markup = (profit_before_tax / total_cost) * 100
else:
    markup = None

# 8. Display cost breakdown
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

# 9. Final results
print("\n========== FINAL RESULTS ==========")

print(f"Revenue: ₹{revenue:,.2f}")
print(f"Total direct costs: ₹{total_direct_costs:,.2f}")
print(f"Total indirect costs: ₹{total_indirect_costs:,.2f}")
print(f"TOTAL COST: ₹{total_cost:,.2f}")

print(f"\nPROFIT BEFORE TAX (PBT): ₹{profit_before_tax:,.2f}")
print(f"Tax rate entered: {tax_rate:.2f}%")
print(f"Estimated tax on PBT: ₹{tax_amount:,.2f}")
print(f"PROFIT AFTER TAX (PAT): ₹{profit_after_tax:,.2f}")

if pbt_margin is not None:
    print(f"\nPBT Margin: {pbt_margin:.2f}%")
    print(f"PAT Margin: {pat_margin:.2f}%")
else:
    print("\nMargins cannot be calculated because revenue is zero.")

if markup is not None:
    print(f"Markup on total cost (before tax): {markup:.2f}%")
else:
    print("Markup cannot be calculated because total cost is zero.")

print("\n===== END OF REPORT =====")
