"""QuickSort"""

def quickSort(array):
    if len(array) < 2:
        return array
    index = len(array) // 2
    middle = array[index]
    print(middle)

    equal = [element for element in array if middle == element]
    less = [element for element in array if middle > element]
    bigger = [element for element in array if middle < element]
    middle = equal
    return quickSort(less) + middle + quickSort(bigger)