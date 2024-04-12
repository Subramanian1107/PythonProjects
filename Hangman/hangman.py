import random

with open("Hangman/wordList.txt", 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowedErrors = 5
done = False
guesses = []
while not done:
    for letter in word:
        if letter.lower() not in guesses:
            print("_", end=" ")
        else:
            print(letter,end=" ")
    print("\n")
    guess = input(f"Guesses Left: {allowedErrors}\nGuess a letter:")
    guesses.append(guess)
    if guess.lower() not in word.lower():
        allowedErrors -= 1
        if allowedErrors == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done == True:
    print(f"Well done! You found the word. The word is indeed '{word}' ")
else:
    print(f"Game Over! The word was '{word}'. Try again")
