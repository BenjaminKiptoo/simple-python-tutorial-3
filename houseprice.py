price = 1000000
good_credit = True
if good_credit:
    downpayment = 0.1*price
    print(f"You need to pay {downpayment} dollars")
else:
    downpayment = 0.2 * price
    print(f"You need to pay {downpayment}")