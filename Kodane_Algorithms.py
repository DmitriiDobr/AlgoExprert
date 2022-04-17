"""
Алгоритм Кейдейна
"""

def kadanesAlgorithm(array):
    maximum_so_far = -float('inf')
    current_sum = -float('inf')
    for element in array:
    	current_sum = max(current_sum+element,element)
        if current_sum > maximum_so_far:
			maximum_so_far = current_sum
	return maximum_so_far