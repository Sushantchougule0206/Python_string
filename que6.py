'''Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the
starting position
Given:
str1 = "Welcome to USA. usa awesome, isn't it?
Expected answer : 16, 11'''

def find_position(str1,substr):
    str1_lower=str1.lower()

    l=[]
    start=0
    end=len(str1)

    while True:
        idx=str1_lower.find(substr,start,end)
        if idx != -1 and str1_lower.count(substr,start,end)!=0:
            l.append(idx)
            start=idx+1
        else:
            break
    return l

str1 = "Welcome to USA. usa awesome, isn't it?"
substr=input()
print(find_position(str1,substr))