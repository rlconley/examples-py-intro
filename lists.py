languages = [
    "English",
    "French",
    "Arabic",
    "Russian",
    "Kinyamulenge",
    "Spanish",
    "Haitian Creole",
]
# lists have [] and can have whitespace between items. Note the trailing comma

for language in languages:
    # any word can be used to represent the singular item, same as in JS
    print("Someone in our class speaks " + language)

print("The last value of language in the loop was: ", language)

for index in range(len(languages)):
    print(index)
    print("Someone in our class speaks " + languages[index])

# both of these for loops achieve the same end result
