"""

Given a string containing digits from 2-9, return all possible letter combinations that the number could 
represent based on phone numbers/letters. For example, 2 could be a, b, or c, 3 could be d, e, or f, 
and so on.

Example:

$ phoneLetter('9')
$ ['w', 'x', 'y', 'z']

$ phoneLetter('23')
$ ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

"""

import math

keypad = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
	 '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
	 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
	 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

def merge(list1, list2):
	List = list()
	for e in list1:
		List += [e + i for i in list2]
	return List

def phoneLetter(string):
	mid = int(math.floor(len(string) / 2))
	if len(string) == 1:
		return keypad[string]
	if len(string) > 1:
		list1 = phoneLetter(string[:mid])
		list2 = phoneLetter(string[mid:])
		return(merge(list1, list2))

if __name__ == "__main__":
	print(phoneLetter("274"))


"""

Input: "274"

Output: ['apg', 'aph', 'api', 'aqg', 'aqh', 'aqi', 'arg', 'arh', 'ari', 'asg', 'ash', 'asi', 
'bpg', 'bph', 'bpi', 'bqg', 'bqh', 'bqi', 'brg', 'brh', 'bri', 'bsg', 'bsh', 'bsi', 'cpg', 'cph', 
'cpi', 'cqg', 'cqh', 'cqi', 'crg', 'crh', 'cri', 'csg', 'csh', 'csi']

"""