def display_menu(choose="selection"):
		menu_dict={'(1) binary to decimal',
								'(2) decimal to binary',
								'(3) binary to hexadecimal',
								'(4) hexadecimal to binary'}
print("Selection:{}").format(selecion)
selecion=input()
def binary_to_decimal(number):
    result=0
    if len(number)>0:
    	power=len(str(number))-1 # determine greatest power
    	for num in str(number):
    		result+=int(num)*2**power
    		power-=1	# decrease by 1
    	return result
# def decimal_to_binary(number):

def main():
	
	display_menu(choose="selection")
	choice=input("Selection: ")
	if int(choice)=='1'
		return binary_to_decimal()

if __name__ == "__main__":
	main()