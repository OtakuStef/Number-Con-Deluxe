import number_calculation
import introduction
import ascii_logo

VIOLET = '\033[38;5;165m'
RESET = '\033[0m'
STEEL_BLUE = '\033[96m'
PEACH = '\033[33m'

introduction
ascii_logo
number = input(VIOLET + "Please enter a number between 0 and 999999999 to beginn!  " + RESET)
print("")
print("")
print(STEEL_BLUE + f"{number} in words is: " + RESET)
print(PEACH + number_calculation.convert_number_to_words(int(number)) + RESET)

