import getpass

letters = []
guesses = []
lives = 9
gameOver = False

#print a list on one line
def print_list(l):
	length = len(l)
	for i in range(length):
		print(l[i], end=" ")
	print()

#add a guess to list of previous guesses
def add_guess(guess):
	if guess.lower() not in guesses:
		guesses.append(guess.lower())

#handle correct vs. incorrect guesses
def process_guess(guess, word):
	index = word.find(guess)
	if index == -1:
		add_guess(guess)
		global lives
		lives -= 1
	else:
		length = len(word)
		#replace the guessed underscores
		for i in range(length):
			if word[i] == guess:
				letters[i] = guess

#update the player on their status
def update_game():
	print_list(letters)
	print("Incorrect:", end=" ")
	print_list(guesses)
	print("Lives:", lives)
	print()

#get a secret word from the hangman
word = getpass.getpass(prompt="Hangman, choose a word: ")
while not word.isalpha():
	word = getpass.getpass(prompt="Hangman, choose a word (alpha characters only): ")
word.lower()

#print a list of dashes for the player
length = len(word)
for i in range(length):
	letters.append("_")
print_list(letters)
print()

#guess until the word is revealed or player runs out of lives
while not gameOver:
	guess = input("Player, guess a letter: ")
	while not guess.isalpha() or len(guess) > 1:
		guess = input("Player, guess a letter: ")
	guess.lower()
	
	process_guess(guess, word)
	update_game()

	if lives == 0 or '_' not in letters:
		gameOver = True
		if lives == 0:
			print("The word was:", word)