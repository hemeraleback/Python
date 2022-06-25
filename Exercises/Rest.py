money = float(input("Enter how much money you have: "))
cost = float(input("Enter how much the product cost: "))

poor=float(cost-money)
rest=float(money-cost)

if cost>money:
    print("You don't have enough money, you are missing ", poor, " euros ")
else:
    print("You can buy this product, and you are missing ", rest, "euros")
