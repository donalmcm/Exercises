# Exercise one----------------------------------------------------------------------------------------------------------
# Write a function in Python that sums up the numbers in a list using an iterative approach.
list_of_numbers = [1, 2, 3, 4, 5, 6]


def get_sum_of_list(list):
	sum = 0
	for x in list:
		sum += x
	print(sum)


get_sum_of_list(list_of_numbers)

# Exercise two----------------------------------------------------------------------------------------------------------
# Write a function which returns the unique items in a list (i.e. removes duplicates)
list_of_dups = [1, 2, 2, 3, 3, 4, 5]


def get_unique_elements(list):
	unique_list = set(list)  # turn list to set which can have no duplicates
	print(unique_list)


get_unique_elements(list_of_dups)

# Exercise three -------------------------------------------------------------------------------------------------------
# Write a function that accepts a string containing words as input and prints the words in a
# hyphen-separated sequence after sorting them alphabetically.
input_string = "Foxtrot Delta Gamma Alpha"


def sort_strings(string):
	words = string.split(' ')  # words is now a list with each word
	words.sort()  # sorts list in alphabetical order
	print('-'.join(words))  # joins list elements with specified character


sort_strings(input_string)

# Exercise four---------------------------------------------------------------------------------------------------------
# Write a function which determines whether a number is a perfect number i.e. its proper divisors
# (excluding the number itself) add to that number e.g. 6 is perfect because 1 + 2 + 3 = 6
perfect_no = 6
not_perfect_no = 12


def check_if_perfect_no(number):
	sum = 0
	if number < 6:  # lowest perfect number is 6
		return False
	else:
		for x in range(1, number):  # for loop going from 1 -> 'number' value
			if number % x == 0:
				sum += x
		return sum == number


print(check_if_perfect_no(perfect_no))
print(check_if_perfect_no(not_perfect_no))

# Exercise five---------------------------------------------------------------------------------------------------------
# Write a function that determines if a number is prime or not using trial division. A prime number is a natural
# number greater than 1 and that has no positive divisors other than 1 and itself.
prime_number = 5
not_prime_number = 6


def check_if_prime(number):
	if number <= 1:
		return False
	elif number == 2:
		return True
	else:
		for x in range(2, number):
			if number % x == 0:
				return False
		return True


print(check_if_prime(prime_number))
print(check_if_prime(not_perfect_no))

# Exercise six----------------------------------------------------------------------------------------------------------
# Write a function that determines whether a string is palindrome. Implement both iterative and recursive versions
# of the function.

palindrome_string = "racecar"


def check_if_palindrome_iterative(string):
	left_pos = 0
	right_pos = len(string) - 1
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True


def check_if_palindrome_recursive(string):
	if len(string) <= 1:
		return True
	else:
		if string[0] == string[-1]:
			return check_if_palindrome_recursive(string[1:-1])
		else:
			return False


print(check_if_palindrome_iterative(palindrome_string))
print(check_if_palindrome_recursive(palindrome_string))


# Exercise seven--------------------------------------------------------------------------------------------------------
# The Fibonacci series is a series of numbers in which each number (Fibonacci number) is the sum of the two preceding
# numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc. Write a function in Python to calculate the nth Fibonacci
# number recursively. Use it to populate a list of the first 10 Fibonacci numbers.

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


# list of first 10 fibonacci numbers
fibs = [fibonacci(i) for i in range(0, 10)]
print(fibs)

# Exercise eight--------------------------------------------------------------------------------------------------------
# Write a function which multiplies the numbers in list by each other, ignoring items in the list which are zero
# e.g. [3, 0, 5] gives 15 and [2, 4, 5] gives 40. Use reduce()and supply function you have written. And then
# implement an alternative solution using filter().
from functools import reduce


def product(a, b):
	if (a == 0) and (b == 0):
		return 0
	elif (a == 0) and (b != 0):
		return b
	elif (a != 0) and (b == 0):
		return a
	else:
		return a * b


ans = reduce(product, [3, 0, 5])
print(ans)

# or use filter to filter out 0s
ans = reduce(product, filter(lambda i: i != 0, [3, 5, 0]))
print(ans)


# Exercise nine---------------------------------------------------------------------------------------------------------
# Write a function that calculates n! (factorial) using recursion. Apply the function to the list of digits to
# calculate factorial for 1 .. 9. Use map().

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)


print(factorial(10))

# Exercise ten----------------------------------------------------------------------------------------------------------
# Write a function which counts the number of words in a list of words excluding the words 'the', 'is', and 'and'.
stopwords = ['the', 'is', 'and']


def count(a, b):
	if (b not in stopwords):
		return a + 1
	else:
		return a


text = ['hello', 'there', 'world', 'python', 'and', 'functional']
wordcount = reduce(count, text, 0)
print(wordcount)

# or
print(len([word for word in text if word not in stopwords]))


# Exercise eleven-------------------------------------------------------------------------------------------------------
# Write a function using a closure which allows the day of week in English or Irish to be determined for a specified
# day number (1 .. 7). The function takes the language as an input and returns a function which takes the day number
# as input.

def day_of_week(language):
	if language == "english":
		days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	else:
		days = ['Luain', 'Mhairt', 'Cheadaoin', 'Deardoin', 'Aoine', 'Satharn', 'Domhnach']

	def day(n):
		if 1 <= n <= len(days):
			return days[n - 1]
		else:
			raise Exception

	return day


day = day_of_week("english")
print(day(2))
day = day_of_week("irish")
print(day(2))
