#! /usr/bin/python

"""
count the number of words in a string
read the string from a file
"""
count = 0

def countWords(str):
	global count
	count += len(str.split(" "))
	#count += tcount


def readStringsFromFile(file1):
	input_file = open(file1)

	for line in input_file:
		countWords(line)

def main():
	global count
	fileName = raw_input('enter file name.. ')
	readStringsFromFile(fileName)
	print count

if __name__ == '__main__':
	main()