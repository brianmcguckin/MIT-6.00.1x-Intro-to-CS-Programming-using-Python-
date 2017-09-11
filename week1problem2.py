#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob'
#occurs in s. For example, if s = 'azcbobobegghakl', then your program should print: 2

s = 'azcbobobegghakl'

count = 0

for n in range(len(s)): #set loop
    if s[n:n+3] == 'bob': #loop through string s looking for 'bob'
        count += 1 #increase count for each instance of 'bob'

print(count)
