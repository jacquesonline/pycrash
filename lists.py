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