# def get_menu_option():
	
# 	menu_options=('1' , '2')

# 	while True:
# 		print()
# 		print('Choose the following number conversions')
# 		print('(1) binary to decimal')
# 		print('(2) decimal to binary')

# 		print()
# 		user_input=input()

# 		if user_input in menu_options:
# 			return user_input

# 		else:
# 			print()
# 			print('Invalid selection, Try again!')
# 	# if user_input=='1':
# 	# 	print()
#     	# result=0
#     	# if len(binary)>0:
#     	# 	power=len(str(binary))-1 
#     	# 	for num in str(binary):
#     	# 		result+=int(num)*2**power
#     	# 		power-=1	
#        	# 	return result


def greetings():

	print("This program adds two numbers.")
	
def add_numbers(num1,num2):
	
	total = int(num1) + int(num2)
	return total

def main():

	greetings()
		num1=int(input("Enter first number:"))
		while num1!=integer():
			print("{} is a good number".format(num1))
			break
		else:
			print("Invalid number, Try again!")
	
			# print()
		# num2=input("Enter Second number:")
		# if num1.isnumeric() and num2.isnumeric():
		# 	print("Let's do some adding!")
		# 	print(add_numbers(num1,num2))
		# 	break
		# else:
		# 	print("Invalid number, Try again!")

		# 	print()
		# answer=input("Type 'yes' to end program:")
		# if answer=='yes':
		# 	print("Goodbye!")
		# 	print("Come back when you want to add more numbers!")
		# 	break

if __name__=="__main__":
	main()
