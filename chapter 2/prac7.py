#Take the price of a product as input. Apply a discount:

#Price ≥ 10,000 → 20% discount
#Price ≥ 5,000 → 10% discount
#Otherwise → No discount
#Print the final price.

price = input()
price = int(price)

if price >= 10000 :
    price = price - price* 0.2
    print(price)
elif price >= 5000 :
    price = price - price*0.1
    print(price)
else :
    print('no discount')
    