import sys
import random
import pyjokes

sys.argv


first = 1
last = 10

answer = random.randint(first, last)


while True:
	try:
		# print(answer)
		guess = int(input(f"Guess a number between {first} ~ {last} : "))

		if first-1 < guess < last+1:
					if(guess == answer):
						print("You are genuis")

						break
		else:
			print(f"Hey Random Guy Please enter a number {first} ~ {last} !")

	except ValueError:
		print("Please enter a Number!")
		continue



joke = pyjokes.get_joke('en','neutral')
print(" ")
print('Joke For the Day!!')
print(joke);