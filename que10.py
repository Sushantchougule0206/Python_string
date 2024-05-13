'''10. Count occurrence of spaces, and special characters in given string
Ex.
Input: Fgh^f #89
Expected output :
Spaces: 1
Special characters: 2'''

def count_char(Input):
    spaces=0
    specialchar=0
    for char in Input:
        if char==" ":
            spaces+=1
        elif not char.isalnum():
            specialchar+=1
    print("Spaces:",spaces)
    print("special character:",specialchar)
Input=input("Enter the string:")
count_char(Input)


