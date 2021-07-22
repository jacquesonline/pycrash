# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
# Note: base is assumed to be a positive number.
# Tip: for functions that return a boolean value, you can return the result of a comparison.
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if number == 1:
      return True
    else:
      return False
  number /= base
  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return(n + sum_positive_numbers(n-1))

print(sum_positive_numbers(8)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
