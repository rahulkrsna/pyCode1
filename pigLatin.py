#! /usr/bin/python


"""
this converts string to pig latin words
"""
vowels = ['a','e','i','o','u']

def convertToPigLatin(str):
	finalString = ""
	found = False
	for i in range(len(str)):
		if (str[i] in vowels):
			found = True
			break

	if found == True:
		if i == 0:
			finalString = str[:]
			finalString += "way"
		else:
			finalString = str[i:]
			finalString = finalString + str[0:i]
			finalString += "ay"
	else:
		finalString = str[:]+"way"

	print "output string: ",finalString

def main():
	strn = raw_input("Enter a string.. ")
	convertToPigLatin(strn)

if __name__ == '__main__':
	main()


