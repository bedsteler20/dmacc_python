TAX_RATE = 0.06
purchase_amount = float(input("Enter the purchase amount: "))
cash_coupon = int(input("Enter the cash coupon (5 or 10): "))
percent_coupon = int(input("Enter the percent coupon (10, 15, or 20): "))

cash_off_subtotal = purchase_amount - cash_coupon

percent_off_subtotal = cash_off_subtotal * (1 - percent_coupon / 100)

tax_amount = percent_off_subtotal * TAX_RATE

shipping_cost = 0.0
if purchase_amount <= 10:
    shipping_cost = 5.95
elif purchase_amount <= 30:
    shipping_cost = 7.95
elif purchase_amount <= 50:
    shipping_cost = 11.95

total = percent_off_subtotal + tax_amount + shipping_cost

print("Total: $", format(total, ".2f"))