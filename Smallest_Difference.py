"""
Find the pair of numbers, whose absolute difference is closest to zero.
(one number from first array, another from second array)
"""

def smallestDifference(arrayOne, arrayTwo):
    previous_difference = abs(arrayOne[0] - arrayTwo[0])
    for first_array in arrayOne:
        for second_array in arrayTwo:
            current_difference = abs(first_array - second_array)
            print(current_difference, first_array, second_array, previous_difference)
            if current_difference <= previous_difference:
                previous_difference = current_difference
                current_candidates = [first_array, second_array]

    return current_candidates

