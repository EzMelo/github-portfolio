correct_num = 7
guess = int(input("Enter a guessed number between 0 and 10: "))

print("The number you guessed is: "+ str(guess))

if correct_num == guess:
	print("WELL DONE! You guessed the correct number")
else:
	print("Sorry you guessed the wrong number the incorrect number is "+ str(correct_num))


