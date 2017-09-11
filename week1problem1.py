#Assume s is a string of lower case characters
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i',
#'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: 5

s = 'azcbobobegghakl'

numVowels = 0

for char in s: #set loop
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': #check for vowels in string s
        numVowels += 1 #increase count for each instance of a vowel

print(numVowels)
