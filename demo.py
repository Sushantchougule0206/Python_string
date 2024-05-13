#Prime number between 100 to 200
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_range(start,end):
    prime_no=[]

    try:
        start=int(start)
        end=int(end)

        if start>end or start<0:
            print("Invalid range")
            return
        for num in range(start,end):
            if is_prime(num):
                prime_no.append(num)
        print(prime_no)    

    except ValueError:
        print("Please enter intergers for start and end")
        return
    
     
    
start=input("Enter the start:")
end=input("Enter the end:")

prime_range(start,end)