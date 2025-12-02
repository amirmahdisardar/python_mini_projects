# this program generates a random password based on user-defined criteria
import random
import string
password_characters = [string.ascii_lowercase]
def str_to_bool(s):
    #this function converts string input to boolean (yes/no to True/False)
    return s.strip().lower() in ["true", "yes", "y", "1","YES","Yes",""]

def characters():
    
    #this function adds character sets to the password based on user preferences
    capital =str_to_bool(input("Do you want your password to have a capital letter ?(yes/no) : "))
    digit=str_to_bool(input("Do you want your password to have a digits ?(yes/no) : "))
    symbol=str_to_bool(input("Do you want your password to have symbol ?(yes/no) : "))
    #adding necessary characters
    if capital:
        password_characters.append(string.ascii_uppercase)
    if digit:
        password_characters.append(string.digits)
    if symbol:
        password_characters.append(string.punctuation)


characters()
#combine all selected character sets into a single string
password_characters = "".join(password_characters)
#length of the password
length = int(input("Enter the length of the password you want: "))
#generate password
password = ''.join(random.choice(password_characters) for _ in range(length))

print (f"\nYour generated password is : [{password}] ")
print("Please save it somewhere safe !")