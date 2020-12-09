"""
    CS051P Lab Assignments: Credit Cards, Part 1

    Name: Hannah Mandell

    Date:   10 - 01 - 19

    The goal of this assignment is to give you more practice with functions,
    including testing functions.

    Note: You do not need to submit this file.
"""


def last_digit(num):
    """
    Computes the last digit of the num

    :param num: (int) a positive integer
    :return: (int) the last digit of num
    """
    # enforce that user input is a positive integer
    if type(num) != int or num < 0:
        return None

    else:
        # return the last digit
        return num % 10

    pass


def decimal_right_shift(num):
    """
    Right shifts num by one digit

    :param num: (int) a positive integer
    :return: (int) num right shifted by one digit
    """

    # subtract last digit
    remove_last = num - last_digit(num)

    # move the decimal over one place by dividing by 10.
    # change variable type to int
    right_shifted = int(remove_last/10)
    return right_shifted
    pass


def sum_digits(num):
    """
    Computes the sum of digits in num

    :param num: (int) a positive 3-digit integer
    :return: (int) sum of digits in num
    """
    # prompt user to enter a 3 digit positive integer

    digit_sum = 0

    while num > 0:
        digit_sum += last_digit(num)
        num = decimal_right_shift(num)

    return digit_sum
    pass


def main():
    """
    Enforces the input of a 3-digit positive integer and computes the sum of those digits

    :return: The sum of the digits of user_in is sum_digits(user_in)
    """
    valid = False

    while not valid:
        user_in = input("Please enter a 3-digit positive integer:\n\t")
        if len(user_in) != 3 or not str.isdigit(user_in):
            valid = False
        else:
            valid = True
            int_user_in = int(user_in)
            print("The sum of the digits of " + str(user_in) + " is " + str(sum_digits(int_user_in)))

    return None
    pass


if __name__ == "__main__":
    main()
