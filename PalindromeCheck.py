"""
Check that string is palindrome
"""

def isPalindrome(string):
	cur_flag = True
	end_id=len(string) - 1
	length = len(string)//2
	for id_char in range(length):
		if string[id_char] == string[end_id]:
			cur_flag = True
		else:
			cur_flag = False
			break
		end_id-=1
	return cur_flag