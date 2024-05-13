'''Given an input string with the combination of the lower and upper case arrange characters in such a
way that all lowercase letters should come first.'''

'''str1= "aMiT"
l1=list(str1)
print(l1)
l2=[]
max=ord(l1[0])
for i in range(len(l1)):
    if max<ord(l1[i]) and ord(l1[i])!=ord(l1[i-1]):
        max=ord(l1[i])
        ascii=chr(max)
        l2.append(ascii)
print(l2)'''

str1=input('Enter the string: ')

s1=''
s2=''

for i in str1:
    if i.islower():
        s1=s1+i
    else:
        s2=s2+i
print(s1+s2)
