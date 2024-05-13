''' Given a string of odd length greater than 7, return a new string made of the middle three characters
of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
bon'''

str1 = "RakeshzipPetabb"
idx=int(len("RakeshzipPetabb")/2)
#print(str1[idx-1]+str1[idx]+str1[idx+1])

print(str1[idx-1:idx+2])