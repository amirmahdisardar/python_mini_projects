# this app checks the strength of a password entered by the user
'''
if in password there is uppercase,digit,special character and length is more than 8 then it is strong password
if any two of the above conditions are met and length is at least 6 then it is medium password
otherwise it is weak password
'''

import string

def password_checker(password=""):
    # this function checks the strength of the password
    strong = 0
    length = 0
    # check length first if less than 6 then weak password
    if len(password) <6 :
        return "Weak Password"
    if len(password) >=6 :
        length +=1
    if len(password) >=8 :
        length +=1
    # check for digit,uppercase,special character
    if  any(c.isdigit() for c in password) :
        strong +=1
    if  any(c.isupper() for c in password):
        strong +=1
    if  any(char in string.punctuation for char in password):
        strong +=1
    # final evaluation
    if strong ==0:
        return "Weak Password"
    elif strong ==3 and length >=2:
        return "Strong Password"
    elif strong ==2 and length >=1:
        return "Medium Password"


password = input("Enter your password :").strip()
print(password_checker(password))
