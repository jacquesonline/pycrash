# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

# In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.
def factorial(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)      
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))


# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.
for multiple in range(0,101,7):
    print(multiple)

# This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). 
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3 

# 2 4 6 

# 3 6 9

def multiplication_table(start, stop):
	for x in range (start, stop+1):
		for y in range (start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter


# Complete the function digits(n) that returns how many digits the number has.
# For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n >= 1):
		count += 1
		n /= 10  
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 
# Fill in the blanks to make this work correctly.
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop :
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. 
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.
def even_numbers(maximum):
	return_string = ""
	for x in range (2, maximum+1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed