"""
    CS051P Lab Assignments: PPM Processing

    Name: Hannah Mandell

    Date:   8 Nov 2019

    The goal of this assignment is to give you practice working with nested lists
    by writing a program that manipulates the entire image with multiple lines.
"""


def process(lines, rows, cols):
    """
    Takes the lines of a file and returns them with the desired amount of rows and columns
    :param lines: (lst) list of strings representing the body of an image
    :param rows: (int) number of rows
    :param cols: (int) number of columns
    :return: (list) list of lists with length row
    """
    image_list = []

    correct_numbers_in_row = 3 * cols  # calculate the correct number of numbers in each row

    # make a giant list of all the values in lines
    new_list = []
    for line in lines:  # go through each string in lines
        new_list.extend(line.split())  # put each string into new_list

    scan_line = []
    current_numbers_in_row = 0

    for item in new_list:  # go through each item in new_list
        scan_line.append(int(item))  # cast item as an int and append it to scan_list
        current_numbers_in_row += 1  # increase the count for the current amount of numbers in the row

        # when the scan_line has the correct amount of numbers in it, append it to image_list
        if current_numbers_in_row == correct_numbers_in_row:
            image_list.append(scan_line)
            scan_line = []  # reset the scan_line
            current_numbers_in_row = 0  # reset the count for current_numbers_in_row

    # return the modified arrangement of ppm values
    return image_list


def read_ppm(filename):
    """
    Takes a filename and returns the lists of lists returned by calling process(filename)
    :param filename: (str) name of a file
    :return: (lst) list of lists returned by process(filename)
    """
    # open the file
    file_in = open(filename, "r")

    read_list = []
    row_and_column = ""
    line_count = 0

    # go through each line in the file
    for line in file_in:
        if line_count == 1:  # save the row and column values in a variable
            row_and_column += line
        if line_count > 2:  # append the lines of ppm values to read_list
            read_list.append(line)
        line_count += 1

    row_and_column_lst = row_and_column.split()  # create a list of the row and column values

    file_in.close()  # close the file

    return process(read_list, int(row_and_column_lst[1]), int(row_and_column_lst[0]))


def write_ppm(image, filename):
    """
    Takes a list of lists of integers and a filename and writes a valid ppm file to an output file
    :param image: (list) a list of lists of ints
    :param filename: (str) name of a file
    """
    # calculate the number of rows and columns as integers
    rows = len(image)
    cols = len(image[0]) // 3

    # write the first 3 lines of the ppm file
    out_file = open(filename, "w")
    out_file.write("P3\n")
    out_file.write(str(cols) + " " + str(rows) + "\n")
    out_file.write("255\n")

    final_image_str = ""

    # go through each each row in the image
    for row in image:
        new_str = ""  # reset new_str each row
        for item in row:  # convert item to type str and add it to new_str
            str_item = str(item)
            new_str += str_item + " "
        final_image_str += new_str + "\n"  # add each new_str to its own line in final_image_str

    out_file.write(final_image_str)  # write the string of ppm values into out_file
    out_file.close()  # close file


def scale(image, row_scale, col_scale):
    """
    Takes an image and two scaling factors and returns a list of lists
    :param image: (list) a list of lists of ints (from process)
    :param row_scale: (int) row scale factor
    :param col_scale: (int) column scale factor
    :return: (list) a list of list of ints
    """

    new_scaled = []

    for index in range(0, len(image), int(row_scale)):  # go through each <row_scale>th list in image
        scaled = []  # reset scaled
        for item in range(0, len(image[index]), int(col_scale) * 3):  # add each <col_scale>th pixel to scaled
            scaled.append(image[index][item])
            scaled.append(image[index][item + 1])
            scaled.append(image[index][item + 2])
        new_scaled.append(scaled)  # append each scaled to new_scaled

    return new_scaled  # return a list of list of the scaled ppm values


def main():
    """
    1. Ask the user for an input file name.
    2. Ask the user for an output file name.
    3. Ask the user for a height scaling factor.
    4. Ask the user for a width scaling factor.
        (Note that you should enforce both scaling factors
        must be positive integers)
    5. The program will read from the input file and create a
    new file with the specified name that contains a copy of the
    input file scaled down by the specified factors.
    """

    filename_in = input("Please enter an input filename:\n\t")  # get an input file name from user
    filename_out = input("Please enter an output filename:\n\t")   # get an output file name from user

    height_scale = input("Enter a height scaling factor:\n\t")  # get a valid height scale from the user
    height_valid = False
    while not height_valid:
        # check if input is a positive integer, reject if not and ask again
        if not str.isdigit(height_scale) or int(height_scale) < 1:
            height_scale = input("Please enter a positive integer.\nEnter a height scaling factor:\n\t")
            height_valid = False
        else:
            height_valid = True

    width_scale = input("Enter a width scaling factor:\n\t")  # get a valid width scale from the user
    width_valid = False
    while not width_valid:
        # check if input is a positive integer, reject if not and ask again
        if not str.isdigit(width_scale) or int(width_scale) < 1:
            width_scale = input("Please enter a positive integer.\nEnter a width scaling factor:\n\t")
            width_valid = False
        else:
            width_valid = True

    image = read_ppm(filename_in)  # convert file_in into a list of lists
    final = scale(image, height_scale, width_scale)  # scale those lists based on the inputted height and width
    write_ppm(final, filename_out)  # write the scaled ppm values into file_out in ppm format

if __name__ == '__main__':
    main()
