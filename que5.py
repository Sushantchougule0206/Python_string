'''create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1
and second last char of s2, and so on. Any leftover chars go at the end of the result.
Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX'''

s1 = "Abc"
s2 = "Xyz"

for i in range(len(s1)):
    s3=s3+s1[i]
    s3=s3+s2[len(s2)-1]
    result

