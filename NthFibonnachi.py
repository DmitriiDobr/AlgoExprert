"""get nth Fibbonacci"""

def getNthFib(n, index=2, number=1, prev_number=0):
    if n == 1:
        return 0
    elif index == n:
        return number
    number_new = number + prev_number
    return getNthFib(n, index=index + 1, number=number_new, prev_number=number)
