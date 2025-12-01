# this project taks a number ftom the user and returns Magical or Curses or Legendary or Normal
def magic_spell(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Legendary"
    elif number % 3 == 0:
        return "Magical"
    elif number % 5 == 0:
        return "Curses"
    else:
        return "Normel"
# Example usage:
user_input = int(input("Enter a number: "))
print(magic_spell(user_input))