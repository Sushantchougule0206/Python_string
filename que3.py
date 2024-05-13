'''two strings, s1, and s2 return a new string made of the first, middle, and last characters each input
string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan'''

s1 = "America"
s2 = "Japan"
idx1=int(len(s1)/2)
idx2=int(len(s2)/2)

print(s1[:1]+s2[:1]+s1[idx1]+s2[idx2]+s1[6:]+s2[4:])