s = 'azcbobobegghakl'

numVowels = 0

for char in s: #set loop 
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': #check for vowels in string s
        numVowels += 1 #increase count for each instance of a vowel

print(numVowels)
