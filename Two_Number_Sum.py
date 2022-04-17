"""
Find pair of element that sum is equal to targetSum, if exists
"""

def twoNumberSum(array, targetSum):
    elements = []
    for element in array:
        if targetSum > element and ((targetSum - element) in array) and ((targetSum - element )!=element):
            return [element ,targetSum - element]
        elif targetSum < element and ((targetSum - element) in array):
            return [element ,targetSum - element]
        elif targetSum == element and (0 in array):
            return [element ,0]
    return elements

