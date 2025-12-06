# Function to check  a number is positive or negative
def is_positive(number):
    # Check if the number is positive
    # Return True if positive, False otherwise
    return number>=0
continue_loop = True
# Loop to allow multiple checks
print("Welcome to the Positive or Negative Number Checker!")
while continue_loop :
    
    user_number = int(input("Enter your number for check that is positive or negative : "))
    
    if is_positive(user_number):
        print(F"The number {user_number} is positive.")
    else:
        print(F"The number {user_number} is negative.")
    continue_loop= input("you want try again another number?(yes/no) :").lower().strip()
    if continue_loop== "no"or continue_loop=="n": 
        continue_loop = False
