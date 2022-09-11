money = float(input("Enter how much money you have: "))
cost = float(input("Enter how much the product cost: "))

if cost>money:
    print("You don't have enough money, you are missing ", cost-money , " euros")
else:
    print("You can buy this product, and you are missing ", money-cost, "euros")
