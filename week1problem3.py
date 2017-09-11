s = 'azcbobobegghakl'
#answer is beggh
s= s + ' ' #add a space to the end of the string to prevent while loop index error
count = 0
substring = ''


while count + 1 < len(s):
    if s[count] <= s[count + 1]: #compare index value to the next index value
        count += 1
    else:
        if len(s[0:count + 1]) > len(substring):
            substring = s[0:count + 1] #set substring to the slice derived in if condition
        s = s[count + 1:] #set s to what hasn't been checked in the string yet
        count = 0 #reset count to perform if condition loop using new string

print(substring)
