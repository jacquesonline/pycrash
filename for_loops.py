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

# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. 
# Currently the code will keep executing the function even if it succeeds. 
# Fill in the blank so the code stops trying after the operation succeeded.

# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")

# retry("create_user", 3)
# retry("stop_service", 5)

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

