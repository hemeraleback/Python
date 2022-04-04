import random

length = int(input("enter how many characters you want to have in your password: "))
lowertext = str("abcdefghijklmnopqrstuvwxyz")
uppertext = str("ABCDEFGHIJKLMNOPQRSTUVWXZY")
number = str("0123456789")
symbol = str("[]{}*()/&$_+;,.:-")

build = lowertext + uppertext + number + symbol
password = "".join(random.sample(build, length))
print(password)
