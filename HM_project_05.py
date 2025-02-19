def greetings():

	print("This program adds two numbers.")
	
def add_numbers(num1,num2):
	
	total = int(num1) + int(num2)
	return total
	print("Type 'yes' to end program:")

if __name__=="__main__":
	while True:
		greetings()
		num1=input("Enter first number:")
		print("{} is a good number!".format(num1))
		if num1=='yes':
			print("Goodbye!")
			print("Come back when you want to add more numbers")
			break
		else:
			print("Invalid number, Try again!")
		num2=input("Enter Second number:")
		print("Let's do some adding!")
		if num2=='yes':
			print("Goodbye!")
			print("Come back when you want to add more numbers!")
			break
		if num1.isnumeric() and num2.isnumeric():
			print(add_numbers(num1,num2))
		else:
			print("Invalid number, Try again!")

