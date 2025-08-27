import random
name = input(f"I am going to try and guess your age\nWhat is your name?: ")
while True:
	check = input(f"Your age is: {(x:=random.randint(15,30))}\nWas I right?(Y/N)")
	if check.lower() != "y":
		print("rats")
	else:
		print(f"{name} is {x} years old")
		break
