shares_bought = 2000
purchase_price = 40
buy_commission_rate = 3 / 100
num_sold = 2000
selling_price = 42.75
commission_rate = 3 / 100

total_buy_price = shares_bought * purchase_price
total_buy_commission_amount = total_buy_price * commission_rate
total_sell_price = num_sold * selling_price
total_sell_commission_amount = total_sell_price * commission_rate
shares_bought=int(input('How many shares did you purchase?:'))
purchase_price=float(input('What was the purchase price?:'))
selling_price=float(input('What was the selling price?:'))
commission_rate=float(input('What was the commission rate?:'))


print('The amount of money Joe paid for the stock is', total_buy_price)
print('The amount of commission Joe paid his broker when he bought the stock is', total_buy_commission_amount)
print('The amount that Joe sold the stock for is', total_sell_price)
print('The amount of commission Joe paid his broker when he sold the stock is', total_sell_commission_amount)
print('the amount of money that Joe had left when he sold the stock and paid his broker is', (total_sell_price-total_sell_commission_amount) - (total_buy_price+total_buy_commission_amount))
if commission_rate > 0:
    print("Joe made a profit.")

else:
    print("Joe lost money.")
