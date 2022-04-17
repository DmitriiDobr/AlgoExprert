"""BubbleSort"""


def bubbleSort(array):
    for iteration in range(len(array)):
        for index in range(0, len(array) - 1):
            if array[index + 1] <= array[index]:
                array[index + 1], array[index] = array[index], array[index + 1]
    return array

