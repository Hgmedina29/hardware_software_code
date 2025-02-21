def greetings():

	print("This program adds two numbers.")
	
	
def add_numbers(num1,num2):
	
	total = int(num1) + int(num2)
	return total

def main():

	greetings()
	while True:
		num1=input("Enter first number:")
		if num1.isnumeric():
			print("{} is a good number".format(num1))
			

		else:
			print("Invalid number, Try again!")
			continue

		num2=input("Enter Second number:")
		if num2.isnumeric():
			print("{} is a good number".format(num2))
			print("Let's do some adding!")
			print(add_numbers(num1,num2))

		else:
			print("Invalid number, Try again!")
			continue 

		answer=input("Type 'yes' to end program:")
		if answer=='yes':
			print("Goodbye!")
			print("Come back when you want to add more numbers!")
			break


if __name__=="__main__":
	main()
