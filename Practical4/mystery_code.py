# What does this piece of code do?
# Answer: The code is to count the number of attempts it takes until two random numbers that are within the range 1-6 are the same.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0					# This variable is used to track the progress count.
while progress>=0:
	progress+=1
	first_n = randint(1,6)	# generate a random integer between 1 and 6
	second_n = randint(1,6)	# generate a random integer between 1 and 6
	if first_n == second_n:	# check if the values of "first_n" and "second_n" are equal
		print(progress)
		break				# break out of the while loop once the condition is met

