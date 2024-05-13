'''8. Given a string in format Emp_name:Emp_id
If emp_id is perfect square -- > Print only vowels from emp_name
Else if emp_id is prime -- > print alternate characters from emp_name
Else if emp_id is odd -- > print sum of ascii values of characters in emp_name
Else print None'''
import math

def is_sqr(n):
    root=int(math.sqrt(n))
    if root*root==n:
        return True

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if i < 2:
            return False
        elif n%i==0:
            return False
    return True


def str_format(empname,empid):
    l=list(empname)
    str1=''
    sum_ascii=0
    if is_sqr(empid)==True:
        str1=''.join(i for i in l if i in ['a','e','i','o','u'] )
        return str1
    elif is_prime(empid)==True:
        for i in range(0,len(empname),2):
            str1+=empname[i]
        return str1
    elif empid%2!=0:
        l=[ord(i) for i in l ]
        for j in l:
            sum_ascii+=j
        return sum_ascii
    else:
        return None

emp_name=input("Enter name:")
emp_id=int(input("Enter id:"))
print(str_format(emp_name,emp_id))



            


    