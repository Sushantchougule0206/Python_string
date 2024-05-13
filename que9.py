'''9. Find all mobile number mentioned in given paragraph of text
Mobile number is always a 10 digit number no spaces no special characters
Ex. Input= “this is a good number 9089786756 and 8900000000 is a desired number”
Expected output: 9089786756 , 8900000000'''


Input= "this is a good number 9089786756 and 8900000000 is a desired number"
l1=Input.split(" ")
mob_no=''
for i in l1:
    if i.isdigit()==True and len(i)==10:
        mob_no+=i+' '
print(mob_no)