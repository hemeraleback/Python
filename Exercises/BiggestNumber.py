maxnum = int(0)

for i in range(10):
    num = int(input("Enter the number: "))
    if maxnum < num:
        maxnum = num

print("The biggest number is ", maxnum)