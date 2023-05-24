import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]


def findItemIndex(list, item):
    try:
        return list.index(item)
    except ValueError:
        return -1


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
print(word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
userInput = ['_'] * len(word)
wordLetters = list(word)

while findItemIndex(userInput, '_') != -1:
    guessLetter = input("Please enter a letter\n").lower()
    targetIndex = findItemIndex(wordLetters, guessLetter)
    if targetIndex != -1:
        userInput[targetIndex] = wordLetters[targetIndex]
        wordLetters[targetIndex] = ''

    print(wordLetters)
    print(userInput)

#result = containsLetter(word, guess)
#print(f"{result}")
