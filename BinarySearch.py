"""BinarySearch"""
def binarySearch(array, target):
    middle_index = len(array) // 2 - 1
    search_arr = array
    while search_arr != []:
        element = search_arr[middle_index]
        if element == target:
            return array.index(element)
        elif element > target:
            search_arr = search_arr[:middle_index]
            middle_index = len(search_arr) // 2 - 1
        elif element < target:
            search_arr = search_arr[middle_index + 1:]
            middle_index = len(search_arr) // 2
    return -1



