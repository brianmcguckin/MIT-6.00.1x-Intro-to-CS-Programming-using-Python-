s = 'azcbobobegghakl'

count = 0

for n in range(len(s)): #set loop
    if s[n:n+3] == 'bob': #loop through string s looking for 'bob'
        count += 1 #increase count for each instance of 'bob'

print(count)
