word = 'dragonfruit'


# user makes the first guess
# guesses = 3

# # while loop
# while guesses > 0:
#     # as long as the guesses are correct, keep prompting the user to guess
#     letter = input("Guess a letter: ")
#     if letter in word:
#         print("That letter is in the word")
#     else:
#         print("Nope, that letter is not in the word.")
#         guesses -= 1
#         print("You have " + str(guesses) + " remaining guesses")
# # we get to line 12 when they guess a letter that's not in the word
# print("You have used up your guesses, game over")

display = ''
# for loop
for letter in word:
    print(letter)
    display += ' _'

print(display)
