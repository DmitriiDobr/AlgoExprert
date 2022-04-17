"""
Square elements of array, then sort it

"""

def sortedSquaredArray(array):
    squared_array = list(map(lambda x: x ** 2, array))
    squared_array.sort()
    return squared_array
