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

# The groups_per_user function receives a dictionary, which contains group names with the list of users. 
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

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

<<<<<<< HEAD
# Simple dictionary 
host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", 
                  "google": "8.8.8.8"}
print(host_addresses.keys())
print(host_addresses)

=======
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
>>>>>>> ca869bf6dcc52a0ff949b388ad9d8c116f2587ed

def email_list(domains):
    emails = []

    for domain in domains:

        users = domains[domain]
        for user in users:
            emails.append(user + "@" + domain)

    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

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

# The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long.
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  number = ""
  street = ""
  address = []

  # Separate the address string into parts
  address = address_string.split()
  # Traverse through the address parts
  for part in address:
    # Determine if the address part is the
    # house number or part of the street name
    if part.isnumeric() == True:
      number = str(part)
    else:
      street = street + part + " " 
      
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(number, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. 
# Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. 
# Jamie emailed a follow-up, saying that her list is in reverse order.
# Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse 
  return_list = []
  for name in list2:
    return_list.append(name)

  for name in reversed(list1):
     return_list.append(name)

  return(return_list)

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].
def squares(start, end):
	return [ x**2 for x in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for car, cost in car_prices.items():
    result += "{} costs {} dollars".format(car, cost) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. 
# Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
# Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  return_guests = {**guests2, **guests1}

  return return_guests

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. 
# Upper case should be considered the same as lower case. 
# For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
def count_letters(text):
  result = {}
  # Go through each letter in the text

  for letter in text.lower():
    if letter.isalpha(): 
      # Check if the letter needs to be counted or not
      if letter.lower() not in result:
        result[letter] = 0
      # Add or increment the value in the dictionary
      result[letter] +=1
     
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

