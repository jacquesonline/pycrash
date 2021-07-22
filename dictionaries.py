print("big" > "small")


def sum(x, y):
    return(x+y)


print(sum(sum(1, 2), sum(3, 4)))

print((10 >= 5*2) and (10 <= 5*2))

dict_inp = {'t': 'u',
            't': 'o',
            'r': 'i',
            'a': 'l',
            's': 'p',
            'o': 'i',
            'n': 't'}

# Iterate over the string
for value in dict_inp:
    print(value, end='')

print()

for value in dict_inp.values():
    print(value, end='')

print()

for value in dict_inp.keys():
    print(value, end='')

print()

wardrobe = {"shirt": ["red", "blue", "white"],
            "jeans": ["blue", "black"]}

for garment in wardrobe.keys():
    colors = wardrobe[garment]
    for color in colors:
        print("{} {}".format(color, garment))


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary

    for group in group_dictionary:
        # Now go through the users in the group
        users = group_dictionary[group]

        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)

            # Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))

# Simple dictionary 
host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", 
                  "google": "8.8.8.8"}
print(host_addresses.keys())
print(host_addresses)


def email_list(domains):
    emails = []

    for domain in domains:

        users = domains[domain]
        for user in users:
            emails.append(user + "@" + domain)

    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for items in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += items
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44


animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

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