letters = input("enter a string of letters")
letters = letters.upper()
letters_sorted = ''.join(sorted(letters))
all_words = []

with open("scrabble.txt", 'r') as f:
	for line in f:
		line = line.strip()
		current = ''.join(sorted(line))
		if letters_sorted == current:
			all_words.append(line)

print(all_words)