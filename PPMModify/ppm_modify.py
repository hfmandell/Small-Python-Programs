"""
    CS051P Lab Assignments: PPM Image Modifier

    Name: HANNAH MANDELL

    Date: 10/31/19

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt


def decode(in_filename, out_filename):
    """
    Takes a PPM file and creates a modified version of it
    :param in_filename: (str) name of existing file
    :param out_filename: (str) name of new file created by the function
    """

    # Open <file_in> in reading mode
    file_in = open(in_filename, "r")
    # Create a new file <file_out>
    file_out = open(out_filename, "w")

    count = 0

    # Go through each line in <file_in>
    for line in file_in:

        # Write the first 3 lines of <file_in> into <file_out>
        if count < 3:
            file_out.write(line)
            count += 1
        else:
            # Convert line into a list
            rgb_values = line.split()
            item_count = 0

            # For each number in the list, perform the correct modifications
            for item in rgb_values:

                # To perform calculations, convert each item into an int
                item_int = int(item)
                if item_int % 3 == 0:
                    item_int = 0
                elif item_int % 3 == 1:
                    item_int = 153
                elif item_int % 3 == 2:
                    item_int = 255

                # Convert item_int into type str
                # Write the newly modified item into <file_out>
                if item_count < 1:
                    file_out.write(str(item_int))
                # Include a space before the item if it is not the first item
                else:
                    file_out.write(" " + str(item_int))
                item_count += 1

    # Close files
    file_out.close()
    file_in.close()


def main_part1():
    decode("files/part1.ppm", "files/new_part1.ppm")


def negate(line):
    """
    Takes a line of ppm values and returns a new list with those values negated
    :param line: (str) a sequence of integers, each with value between 0 and 255 (inclusive) separated by whitespace
    :return: (str) an inverted version of the initial sequence
    """
    # Create an empty string to put the negated color values into
    negated_str = ""

    # Convert line into a list
    rgb_values = line.split()

    count = 0
    # Go through each item in the list rgb_values
    for item in rgb_values:

        # Calculate the negated value for each item
        negate_item = str(255 - int(item))

        # Add the calculated negated color to negated_str, with spaces in between each value
        if count > 0:
            negated_str += " " + negate_item
        else:
            negated_str += negate_item
        count += 1

    # Return the string of negated values
    return negated_str


def grey_scale(line):
    """
    Takes a line of ppm values and returns a new line of those values grey-scaled
    :param line: (str) a sequence of integers,each with value between 0 and 255 (inclusive), separated by whitespace
    :return: (str) a new line that is grey-scaled version of the initial sequence
    """
    # Create an empty string to put the grey-scaled values into
    grey_str = ""
    # Create an empty list to put the grey-scaled values into
    grey_lst = []

    # Convert line into a list
    rgb_values = line.split()

    # Go through a while loop until the len(rgb_values) is less than 0
    while len(rgb_values) > 0:

        # Reset squares_total
        squares_total = 0

        # Go through the first 3 items in rgb_values
        for value in rgb_values[0:3]:
            # Turn each value into type int
            # Sum the squares of each value in the range
            squares_total += int(value)**2

        # Calculate the grey value for the given rbg values by square-rooting squares_total
        grey = int(sqrt(squares_total))

        # Any grey value calculated over 255 should be set equal to 255
        if grey > 255:
            grey = 255

        # Append grey to grey_lst 3 times
        for count in range(0, 3):
            grey_lst.append(grey)
            count += 1

        # Delete the first 3 items of rgb_values so that the while loop moves onto the next 3 values in the list
        del rgb_values[0:3]

    count = 0
    # Go through each grey_value in grey_lst
    for grey_value in grey_lst:

        # Turn each grey_value into type str and add it to grey_str
        # Add whitespace between each grey_value
        if count < 1:
            grey_str += str(grey_value)
            count += 1
        else:
            grey_str += " " + str(grey_value)
            count += 1

    # Return the grey-scaled line
    return grey_str


def remove_color(line, color):
    """
    Takes a line and returns
    :param line: (str) a sequence of integers, each with value between 0 and 255 (inclusive), separated by whitespace
    :param color: (str) a color
    :return: (str) the same string with the desired color removed
    """
    # Create a string to eventually put the modified line into
    remove_str = ""

    # Convert line into a list
    rgb_values = line.split()

    # Cycle through every third number in the range from 0 to len(rgb_values)
    for index in range(0, len(rgb_values), 3):
        # If the removed color is red
        if color == "red":
            # Convert the indexed value in rgb_values to 0
            rgb_values[index] = "0"

        # If the removed color is green
        if color == "green":
            # Convert the value after the indexed value in rgb_values to 0
            rgb_values[index + 1] = "0"

        # If the removed color is blue
        if color == "blue":
            # Convert the value 2 spots after the indexed value in rgb_values to 0
            rgb_values[index + 2] = "0"

    count = 0
    # Go through each value in the newly modified rgb_values
    for value in rgb_values:

        # Turn each value into type str and add it to remove_str
        # Add whitespace between each value
        if count < 1:
            remove_str += str(value)
            count += 1
        else:
            remove_str += " " + str(value)
            count += 1

    # Return the modified string
    return remove_str


def main():
    # TODO: implement the following required items:
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. List the possible image manipulation functions and ask the user to
       choose one of them. If they don't enter a valid choice, ask them again.
    4. Perform the requested manipulation on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    """
    # Ask user for an input file
    file_in_name = input("Give me an input file:\n\t")
    # Open the input file in reading mode
    user_file_in = open(file_in_name, "r")

    # Ask user for an output file
    file_out_name = input("Give me an output file:\n\t")
    # Open the output file in writing mode
    user_file_out = open(file_out_name, "w")

    # Print the list of image manipulation choices
    print("Modifications are:\n1. Negate\n2. Greyscale\n3. Remove Red\n4. Remove Blue\n5. Remove Green")

    # Go through a while loop until the user enters a valid response
    # Use that response to perform the desired image manipulation
    choose_mod = False
    while not choose_mod:

        # Ask the user to choose an image modification to perform
        user_image_manip = input("Enter the number of the desired modification\n\t")

        # Reject the user input if it is not valid and ask for another input
        if not str.isdigit(user_image_manip) or len(user_image_manip) > 1 or user_image_manip not in "12345":
            print("That was not a valid input.")
            choose_mod = False

        # If user input is valid, perform the chosen modification on the file
        else:
            choose_mod = True
            count = 0

            # Go through each line in user_file_in
            for line in user_file_in:

                # Write the first 3 lines of user_file_in into user_file_out
                if count < 3:
                    user_file_out.write(line)
                    count += 1

                # For all of the following lines, call the corresponding function to perform the modification
                else:
                    mod_line = ""
                    if user_image_manip == "1":
                        mod_line = negate(line)
                    elif user_image_manip == "2":
                        mod_line = grey_scale(line)
                    elif user_image_manip == "3":
                        mod_line = remove_color(line, "red")
                    elif user_image_manip == "4":
                        mod_line = remove_color(line, "blue")
                    elif user_image_manip == "5":
                        mod_line = remove_color(line, "green")
                    count += 1
                    
                    # Write the modified line into user_file_out
                    user_file_out.write(mod_line + "\n ")

    # Close files
    user_file_out.close()
    user_file_in.close()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
