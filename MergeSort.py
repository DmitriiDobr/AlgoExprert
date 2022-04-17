"""MergeSort"""

def JoinSorted(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array, mid=0):
    if len(array) <= 1:
        return array
    else:
        middle = len(array) // 2
        left = mergeSort(array[:middle], mid=middle)
        right = mergeSort(array[middle:], mid=middle)
        return JoinSorted(left, right)
