#!/usr/bin/python

"""
this program prints the reverse string
"""

def revString(str1):
	if(len(str1) > 1) :
		return str1[-1] + revString(str1[:-1])
	else :
		return str1

def main():
	userinput = raw_input("enter a string.. ")
	print revString(userinput)

if __name__ == '__main__' :
	main()