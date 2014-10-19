#!/usr/bin/python

from reverseString import revString

"""
check if the string is palyndrome (racecar, liril, eve,)
"""

def checkPalyndrome(str):
	if revString(str) == str:
		print 'palyndrome'
	else:
		print 'not palyndrome'

def main():
	strinput = raw_input('input string for palyndrome check.. ')
	checkPalyndrome(strinput)

if __name__ == '__main__':
	main()
