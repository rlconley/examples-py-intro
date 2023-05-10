# do not use let or const to declare variable
name = "Nutmeg"
# have to assign a value to a variable when it is declared

# can reassign values to variables
name = "Bubba"
name = "Lady Poopington"
name = "Butmeg"

# python reads programs from top to bottom, variables and functions must be defined before they are used
# python uses snake_case instead of camelCase

# user_name = input("What is your name? ")
# print("Hello, " + user_name)

# number = int(input("Guess a number between 1 and 10: "))
# print("You guessed " + number)
# # input from user is of the type string. Here we convert it to an integer in order to do comparisons with it.

# if number > 10:
#     print("That's out of range!")

# conditionals can use truthiness and falsiness
if 1:
    print("truthy")

if not 0:
    print("falsy")
# not is the Python equivalent of !

results = ["content", "other content"]
if results:
    # do a thing
    print(results)
