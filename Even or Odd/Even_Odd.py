# Function to determine if a number is even or odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
continue_loop = True
# Loop to allow multiple checks
print("Welcome to the Even or Odd Number Checker!")
while continue_loop:
    user_number = int(input("Enter your number to check if it is even or odd: "))

    result = even_or_odd(user_number)
    print(f"The number {user_number} is {result}.")

    continue_loop = input("Do you want to try another number? (yes/no): ").lower().strip()
    # Check if the user wants to continue if answer is no exit the loop
    if continue_loop in ["no", "n"]:
        continue_loop = False