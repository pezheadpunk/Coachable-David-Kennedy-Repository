'''03/11/25 Practice Problems'''

'''
Write a single line of Python code using a list comprehension to generate a
list of squares for all even numbers from 0 to 10.
'''
squares = [x*x for x in range(11) if x % 2 == 0]

'''
Use a list comprehension to create a list of the squares of all odd numbers from
1 to 20.
'''
squares = [x*x for x in range(21) if x % 2 != 0]

'''
Generate a multiplication table (a 2D list) for numbers 1 to 5 using a list
comprehension.
'''
times_table = [[(x+1)*(y+1) for y in range(5)] for x in range(5)]


def zero_initialized_2D_grid(m: int, n: int):
	'''
	Create a zero-initialized 2D grid of size m x n using a list comprehension.
	Each row should have n elements, and there should be m rows.
	'''
	return [[0 for _ in range(n)] for _ in range(m)]


def multiplication_table(rows: int, cols: int):
	'''
	Write a function multiplication_table(rows: int, cols: int) that generates a 2D
	list representing a multiplication table of size rows x cols.
	'''
	return [[row * col for col in range(cols)] for row in range(rows)]


def merge_sorted_lists(list_1, list_2):
	'''
	Write a function merge_sorted_lists that takes two sorted lists and merges them
	into a single sorted list without using built in sorting functions.
	'''
	i, j = 0, 0
	merged_list = []
	while i < len(list_1) or j < len(list_2):
		if j >= len(list_2):
			merged_list.append(list_1[i])
			i += 1
		elif i >= len(list_1):
			merged_list.append(list_2[j])
			j += 1
		elif list_1[i] <= list_2[j]:
			merged_list.append(list_1[i])
			i += 1
		else:
			merged_list.append(list_2[j])
			j += 1
	return merged_list


def sum_diagonals(matrix):
	'''
	Write a function sum_diagonals that takes a square matrix NxN and returns the
	sum of its main diagonal and anti-diagonal.
	'''
	ret_sum = 0
	for i in range(len(matrix)):
		ret_sum += (matrix[i][i] + matrix[i][(i+1)*(-1)]
	return ret_sum


def first_occurance(target, nums):
	'''
	Write a function first_occurrence that returns the index of the first occurrence
	of target in nums. If the target is not found, return -1.
	'''
	for i, num in enumerate(nums):
		if num == target:
			return i
	return -1


def find_missing_number(nums_list):
	'''
	Write a function find_missing_number that takes a list containing n distinct
	numbers from 0 to n (but missing one number) and finds the missing number.
	'''
	nums = [0 for _ in range(len(nums_list)+1)]
	for num in nums_list:
		nums[num] = 1
	for i, num in enumerate(nums):
		if num == 0:
			return i
	return -1
