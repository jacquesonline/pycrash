# Basic Dictionary
toc = {"Introduction":1000, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?
print(toc["Introduction"])
del toc["Chapter 1"]
print(toc)
print()
#  Iterating 
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animals, appendage in cool_beasts.items():
    print("{} have {}".format(animals, appendage))

def count_letters(text): 
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("this is us making history"))