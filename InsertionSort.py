"""InsertionSort"""

def insertionSort(array):
    for index in range(1, len(array)):
        while index > 0:
            if array[index] <= array[index - 1]:
                array[index], array[index - 1] = array[index - 1], array[index]
            else:
                break
            index -= 1
    return array
