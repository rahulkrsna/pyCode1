#! /usr/bin/python

"""
this program counts the sum of vowels
"""
vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}

def countVowelsInString(str):
	for index in range(len(str)):
		switch(str)
		if str[index] in vowels.keys():
			vowels[str[index]] += 1

	print vowels

def main():
	inputstr = raw_input('Enter string.. ')
	countVowelsInString(inputstr)

if __name__ == '__main__':
	main()
