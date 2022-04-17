"""SelectionSort"""


def selectionSort(array):
    length = len(array)
    for iteration in range(len(array) - 1):
        index = 0
        index_max = 0
        cur_max = array[0]
        while index < length:
            element = array[index]
            cur_index = index
            if cur_max <= element:
                index_max = cur_index
                cur_max = element
            index += 1
        length = length - 1
        array[index_max], array[length] = array[length], array[index_max]
    return array


