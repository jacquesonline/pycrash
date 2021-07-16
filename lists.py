llist = ["jac", "jane", "jade", "jaimey"]
for index, element in enumerate(llist):
    if index % 2 == 0:
        print("{} - {}".format(index+1, element))

def full_email(people):
    result  = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print()
print(full_email([("jac@home.com", "Jac S"),("jane@home.com", "Jane S")]))

multiple = [ x*7 for x in range(1, 11)]
print(multiple)

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'   
    
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
new_filename = " "
for index, filename in enumerate(filenames):
    new_filename = ""
    if filename.endswith("hpp"):
        new_filename = filename[:filename.index(".hpp")+1] + "h"
        newfilenames.append(new_filename)
    else:
        newfilenames.append(filename)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end.
# For example, python ends up as ythonpay.

def pig_latin(text):
  phrase = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    new_word = word[1:len(word)]
    new_word += word[0] + "ay "
    phrase += new_word

  return phrase
		   
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … 
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
  members = group + ": "
  index = 0
  for user in users:
    index += 1
    members += user
    if index != len(users):
      members += ", "
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. 
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. 
# Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 
def guest_list(guests):
	for name, age, work in guests:
		print("{} is {} years old and works as {}".format(name, age, work))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """





