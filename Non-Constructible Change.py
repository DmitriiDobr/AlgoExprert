"""
Minimum amount of change, that you cannot create. For example: [1,2,5], minimum change is 4.
"""

def nonConstructibleChange(coins):
    if coins == []:
        return 1
    else:
        coins.sort()
        sums = [0]
        for coin in coins:
            temp_arr = [digit + coin for digit in sums]
            if (temp_arr[0] - sums[-1]) > 1:
                minimum = sums[-1] + 1
                return minimum
            sums = (sums + temp_arr)
        return sums[-1] + 1
