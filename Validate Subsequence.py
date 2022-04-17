"""
Check, that subsequence in array
"""

def isValidSubsequence(array, sequence):
	check_array = []
	for element in array:
		if element in sequence and (check_array  < sequence):
				check_array.append(element)
	return check_array == sequence