def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""