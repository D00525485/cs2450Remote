import random
print("I am going to try and guess your age")
name = input("What is your name?: ")
while True:
	guess = str(random.randint(15,30))
	check = input(f"Your age is: {guess}\nWas I right?(Y/N)")
	if check.lower() != "y":
		print("rats")
	else:
		print(f"{name} is {guess} years old")
		break
