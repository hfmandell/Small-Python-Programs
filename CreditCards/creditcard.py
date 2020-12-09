"""
    CS051P Lab Assignments: Credit Cards

    Author: Hannah Mandell

    Date:   10 - 04 - 2019

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

from random import randint
from creditcard_part1 import last_digit, decimal_right_shift


def verify(number13):
    """
    Takes 13 digit integer and returns True if passes Luhn Algorithm or False if it fails

    :param number13: (int) a 13-digit number
    :return: (bool) True if number13 passes Luhn Algorithm or False if it fails
   """
    # Define variables even_sum and odd_sum
    even_sum = 0
    odd_sum = 0

    # Turn number13 into type str
    str_number13 = str(number13)

    # Create a variable that reverses number13 so the program can start counting from the original right
    backwards_number13 = str_number13[::-1]

    # Step 1: Double the value of alternate digits of the credit card number beginning with the second digit from the right
    # Loop through every other digit in backwards_number13
    for num in backwards_number13[1:len(backwards_number13):2]:
        # Double the digit
        double_even = int(num) * 2
        # If the doubled digit is greater than nine, redefine it as the sum of its two digits
        if double_even > 9:
            double_even = double_even - 9
        # Add double_even to even_sum
        even_sum += int(double_even)

    # Loop through every other digit in backwards_number13, starting with the first digit
    for num in backwards_number13[0:len(backwards_number13):2]:
        # Add the digit to odd_sum
        odd_sum += int(num)

    # Step 2: Sum even_sum and odd_sum
    # Step 3: If the sum of even_sum and odd_sum ends in a zero (passes Luhn algorithm), return True
    if last_digit(even_sum + odd_sum) == 0:
        return True

    # If the total sum does not end in a zero, return False
    return False
    pass


def generate(number6):
    """
    Takes a 6 digit number and returns a valid 13-digit credit card number that begins with the given 6 digits

    :param number6: (int) a 6-digit number
    :return: (int) a valid 13-digit credit card number
    """
    str_number6 = str(number6)
    valid = False

    # Run a while loop until the generated number passes Luhn algorithm
    while not valid:
        # Add seven random digits to the end of str_number6 for a total of 13 digits
        for num in range(7):
            ran = randint(0, 9)
            str_number6 += str(ran)

        # If str_number6 passes Luhn algorithm, return the str_number as an int
        if verify(int(str_number6)):
            valid = True
            return int(str_number6)

        # If str_number6 does not pass Luhn algorithm, delete the randomly generated last 7 digits and begin the while loop again
        else:
            for count in range(7):
                str_number6 = str(decimal_right_shift(int(str_number6)))
            valid = False
    pass

def main():
    """
    Asks user for an initial 6 digit number, then generates and prints three valid credit card numbers that start with those 6 numbers

    :return: Three valid credit card numbers that start with the initial 6 numbers
    """

    valid = False

    # Run a while loop until the user enters a valid 6 digit number
    while not valid:
        # Ask user for a 6 digit number
        user_in = input("Enter a 6 digit number:\n")
        # Ensure that user_in does not start with 0, is comprised of digits, and is 6 digits long
        if user_in[0] == "0" or not str.isdigit(user_in) or len(user_in) != 6:
            valid = False
        else:
            valid = True

    # Print 3 valid credit card numbers by calling generate()
    print("\nThree valid numbers:")
    print(generate(user_in))
    print(generate(user_in))
    print(generate(user_in))

    return None
    pass


if __name__ == "__main__":
    main()
