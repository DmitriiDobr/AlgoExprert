"""Minimum Waiting Time Greedy"""

def minimumWaitingTime(queries):
    queries.sort()
    summa = 0
    for idx, number in enumerate(queries[:(len(queries) - 1)]):
        cur_number = queries[idx]
        add = cur_number * (len(queries) - (idx + 1))
        summa += add
    return summa
