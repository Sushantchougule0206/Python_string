'''Find all overlapping occurrences of given substring in given string
Ex.
String = 0111
Substring = 11
Expected answer : 2
String : ANANAAAANNN
Substring: ANA
Expected answer : 2
String : ANANAAAANNN
Substring: AA
Expected answer : 3'''

def count_str(str1,substr):
    start=0
    count=0
    end=len(str1)
    while True:
        idx=str1.find(substr,start,end)
        if idx == -1:
            break
        count+=1
        start=idx+1
    
    return count

str1 = input()
substr = input()
print(count_str(str1,substr))


