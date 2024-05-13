'''Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt'''


s1 = "Ault"
s2 = "Kelly"
print(s1[0:2]+s2+s1[2:4])
#OR
print(s1[:2]+s2+s1[2:])
