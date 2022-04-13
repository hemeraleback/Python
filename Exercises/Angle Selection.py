angle=int(input("Write the measure of the angle: "))

if angle == 90:
	print("The angle is right")
elif angle < 90 and angle < 360:
	print("The angle is acute")
elif angle > 90 and angle < 360:
	print("The angle is obtuse")
elif angle > 360:
    print("The measure is too big")