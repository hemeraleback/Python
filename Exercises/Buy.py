saving = int(0) 
price = int(input("Enter the price: "))
	
while saving < price:
	add = int(input("How many money do you want to add?: "))
	saving += add

rest = saving - price

if rest == 0:
	print("Now you can buy it")
else :
	print("Now you can buy it and you saved ", rest, " euro")
