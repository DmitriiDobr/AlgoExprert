"""
maxSubsetSumNoAdjacent Dynamic Programming
"""
def maxSubsetSumNoAdjacent(array):
	if len(array)==0:
		return 0
	elif len(array)==1:
		return array[0]
	second = array[0]
	first = array[0] if array[0] >= array[1] else array[1]
	if len(array)==2:
		return first
	cur = 0
	for idx in range(2, len(array)):
		maximum = cur
		cur = max(second+array[idx],first)
		if maximum >=cur:
			cur=maximum
		first, second = cur, first
	return cur
