words = ["network", "love", "iti", "developer", "coder", "python", "numpy"]

random_word_index = 0
random_word = words[random_word_index]
player_name = input("Enter your name: ")
revealed_word = '-' * len(random_word)
num_guesses = 0

for i in range(7):
    user_guess = input("Guess a letter: ")
    for j in range(len(random_word)):
        if random_word[j] == user_guess:
            revealed_word = revealed_word[:j] + user_guess + revealed_word[j+1:]
    num_guesses += 1
    if revealed_word == random_word:
        print("Congratulations, " + player_name + "! You guessed the word: " + random_word)
        break
if revealed_word != random_word:
    print("Sorry, " + player_name + "! You could not guess the word: " + random_word)