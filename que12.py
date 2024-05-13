'''12. You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w
Example .
String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
Width: 4
Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''

string="ABCDEFGHIJKLIMNOQRSTUVWXYZFHGOEIRHOGOHOH"
width=int(input("Enter the width:"))
for i in range(0,len(string),width):
    print(string[i:i+width])
    
