# def display_menu():

menu_options = ('1' , '2')

while True:
	print('(1) binary to decimal')
	print('(2) decimal to binary')
		
	print()
	user_input = input('Selection:')

	if user_input in menu_options:
		break

	else:
		print()
		print('Invalid option, Try again!')

	if user_input=='1':
		binary_to_decimal(binary)

def binary_to_decimal(binary):
    result=0
    if len(binary)>0:
    	power=len(str(binary))-1 
    	for num in str(binary):
    		result+=int(num)*2**power
    		power-=1	
    	return result

def decimal_to_binary(number):
		remainder=[]
		if len(number)>0:
			while int(number)>1:
				number=int(number)/2
				remainder.append(str(int(number)%2))
		return("".join(remainder[::-1]))

# if __name__=="main":
