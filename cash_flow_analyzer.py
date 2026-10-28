# ==========================================
# FINANCIAL BEAST - CASH FLOW ANALYZER v1.0
# ==========================================

from decimal import Decimal, InvalidOperation

def get_amount(label):
    while True:
        try:
            amount = Decimal(input(f"{label}: ₹"))

            if not amount.is_finite():
                print("Please enter a valid number.")
                continue

            if amount < 0:
                print("Enter zero or a positive amount.")
                continue

            return amount

        except InvalidOperation:
            print("Invalid input. Enter a number, such as 15000.")

def get_signed_amount(label):
    while True:
        try:
            amount = Decimal(input(f"{label}: ₹"))

            if not amount.is_finite():
                print("Please enter a valid number.")
                continue

            return amount

        except InvalidOperation:
            print("Invalid input. Enter a number, such as -5000.")

def money(amount):
    if amount < 0:
        return f"-₹{abs(amount):,.2f}"
    return f"₹{amount:,.2f}""

print("=" * 55)
print("FINANCIAL BEAST - CASH FLOW ANALYZER")
print("=" * 55)

company = input("Business name: ")
start_date = input("Period start date: ")
end_date = input("Period end date: ")

print("\n--- OPENING BALANCE ---")
opening_cash = get_amount("Opening cash and cash equivalents")

print("\n--- OPERATING ACTIVITIES ---")
cash_received = get_amount("Cash received from customers")
other_receipts = get_amount("Other operating cash receipts")
supplier_payments = get_amount("Cash paid to suppliers")
employee_payments = get_amount("Cash paid to employees")
other_payments = get_amount("Other operating cash payments")

operating_inflows = cash_received + other_receipts
operating_outflows = (
    supplier_payments
    + employee_payments
    + other_payments
)

net_operating = operating_inflows - operating_outflows

print("\n--- INVESTING ACTIVITIES ---")
asset_sale_proceeds = get_amount("Cash received from asset sales")
asset_purchases = get_amount("Cash paid to purchase assets")

net_investing = asset_sale_proceeds - asset_purchases

print("\n--- FINANCING ACTIVITIES ---")
loans_received = get_amount("Loans received")
loan_repayments = get_amount("Loan principal repaid")
capital_received = get_amount("Capital introduced")
owner_drawings = get_amount("Owner drawings or distributions paid")

net_financing = (
    loans_received
    + capital_received
    - loan_repayments
    - owner_drawings
)

net_change = net_operating + net_investing + net_financing
closing_cash = opening_cash + net_change

print("\n--- CASH FLOW STATEMENT ---")
print("=" * 65)
print("FINANCIAL BEAST")
print(f"Business: {company}")
print(f"Reporting period: {start_date} to {end_date}")
print("=" * 65)

print("\nA. OPERATING ACTIVITIES")
print(f"Cash received:                  {money(operating_inflows)}")
print(f"Cash paid:                     ({money(operating_outflows)})")
print(f"Net operating cash flow:        {money(net_operating)}")

print("\nB. INVESTING ACTIVITIES")
print(f"Asset sale proceeds:            {money(asset_sale_proceeds)}")
print(f"Asset purchases:               ({money(asset_purchases)})")
print(f"Net investing cash flow:        {money(net_investing)}")

print("\nC. FINANCING ACTIVITIES")
print(f"Loans and capital received:     {money(loans_received + capital_received)}")
print(f"Loan repayments and drawings:  ({money(loan_repayments + owner_drawings)})")
print(f"Net financing cash flow:        {money(net_financing)}")

print("\nD. CASH RECONCILIATION")
print(f"Opening cash:                   {money(opening_cash)}")
print(f"Net increase/decrease:          {money(net_change)}")
print(f"Calculated closing cash:        {money(closing_cash)}")

print("\n--- BASIC ANALYSIS ---")

if net_operating > 0:
    print("Operating activities generated cash.")
elif net_operating < 0:
    print("WARNING: Operating activities used cash.")
else:
    print("Operating activities had zero net cash flow.")

if closing_cash < 0:
    print("WARNING: Calculated closing cash is negative.")
else:
    print("Calculated closing cash is not negative.")

print("\nAssumptions:")
print("- This version uses manually entered cash receipts and payments.")
print("- Non-cash transactions are excluded.")
print("- Cash flow classifications should be reviewed by an accountant.")
print("- This is a learning tool, not a substitute for reviewed accounts.")

print("\n===== END OF REPORT =====")
