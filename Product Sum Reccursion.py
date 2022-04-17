
"""ProductSum Reccurssion"""
def productSum(array, depth=1):
    summa = 0
    for element in array:
        if type(element) == list:
            summa += productSum(element,depth+1)
        elif type(element) == int:
            summa+=element
    return summa*depth
