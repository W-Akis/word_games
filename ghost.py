word = ""
game_over = False

while not game_over:
	letter = input("Enter a letter")
	word = word + letter
	word = word.upper()
	print(word)

	with open("scrabble.txt", 'r') as f:
		for line in f:
			line = line.strip()
			if len(word) > 3 and line == word:
				game_over = True
				break
			elif word == line[0:len(word)]:
				valid = True
				break
		if not valid:
			game_over = True