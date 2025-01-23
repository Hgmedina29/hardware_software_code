def main():
	name = "Hanns"
	print("Hello, I would like to get to know a little about you.")
	print("Please answer a few brief questions.")
	print("What is your name?")
	print()
	print("Do you like programming {}?".format(name))
	answer = input()
	print("Great! You said {}?".format(answer))
	print("Let's start learning some python today")

if __name__== "__main__":
    main()
