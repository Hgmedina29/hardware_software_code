def binary_to_decimal(binary):
    result = 0
    power = len(binary) - 1
    for digit in binary:
        result += int(digit) * (2 ** power)
        power -= 1
    return result

def decimal_to_binary(number):
    remainder = []
    while number > 0:
        remainder.append(str(number % 2))
        number = number // 2
    return ''.join(remainder[::-1])

def show_menu():
    print("Choose the following number conversion:")
    print("(1) Binary to Decimal")
    print("(2) Decimal to Binary")
    return input("Selection: ")

def handle_binary_to_decimal():
    print("Converting Binary to Decimal")
    print("['0', '1'] are valid numbers")
    binary = input("Enter a valid binary number: ")
    if all(c in "01" for c in binary):  
        print("Decimal:", binary_to_decimal(binary))
        input("Hit 'Enter' to continue")
        exit_prompt = input("Type 'yes' to end program or press Enter to continue: ")
        if exit_prompt.lower() == 'yes':
            print("Goodbye!")
            return True  
    else:
        print("Invalid binary number.")
    return False  

def handle_decimal_to_binary():
    print("Converting Decimal to Binary")
    print("['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] are valid numbers")
    try:
        decimal = int(input("Enter a valid decimal number: ")) 
        print("Binary:", decimal_to_binary(decimal))
        input("Hit 'Enter' to continue")
        exit_prompt = input("Type 'yes' to end program or press Enter to continue: ")
        if exit_prompt.lower() == 'yes':
            print("Goodbye!")
            return True  
    except ValueError:
        print("Invalid decimal number.")
    return False  

def main():
    while True:
        user_input = show_menu()
        if user_input == "1":
            if handle_binary_to_decimal():
                break  
        elif user_input == "2":
            if handle_decimal_to_binary():
                break  
        else:
            print("Invalid selection, Try again!")

if __name__ == "__main__":
    main()

