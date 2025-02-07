def conversation():
	while True:
		print("1. What is your name?")
		name=input()
		if name=='exit':
			print("Too bad you did not want to chat! Maybe next time!")
			print("You did not answer any questions.")
			break
		print("2. What is your favorite show, {}?".format(name))
		show=input()
		if show=='exit':
			print("I'll talk to you next time, {}".format(name))
			print("You answered 1 question.")
			break
		print("3. Do you like programming, {}?".format(name))
		answer=input()
		if answer=='exit':
			print("It was nice talking to you, {}".format(name))
			print("You answered 2 questions.")
			break
		print("4. What is your favorite sports team, {}?".format(name))
		team=input()
		if team=='exit':
			print("Thanks for chatting with me, {}".format(name))
			print("You answered 3 questions.")
			break
		
def greeting():
	print("Welcome to my conversation program")
	print("I will keep asking you questions until you type 'exit'.")
	conversation()

def main():

	greeting()

if __name__ == "__main__":
		main()
