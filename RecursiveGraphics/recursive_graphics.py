"""
    CS051P Lab Assignments: Recursive Graphics

    Name: Hannah Mandell

    Date:   10 - 15 - 19

    The goal of this assignment is to familiarize you with recursion,
    including thinking and writing recursive functions.
"""
from turtle import *
from math import sqrt


def draw_triangle(length, color):
    """
    Draw equilateral triangle, from the current position.
    :param length: (int) side length in pixels
    :param color: (string) line color

    end up in original position and heading
    """
    # set color and drop the pen
    pencolor(color)
    pendown()

    # three sides, w/120 degree exterior angles
    # Note: this function demonstrates poor style (it uses repeated code)
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)

    # we should now be at our original position/heading


def draw_polygon(n, length):
    """
    Draw an <n>-sided polygon with each side of a length <length>
    :param n: (int) number of sides
    :param length: (int) side length in pixels
    :return: (None)
    """
    # drop the pen
    pendown()

    # draw each side of the n-sided polygon with 360/n degree exterior angles
    for count in range(n):
        forward(length)
        left(360/n)

    # we should now be at our original position/heading
    penup()


def stairs(x, y, length):
    """
    Draw recursive stairs starting at (x, y) and return the number of squares that were drawn
    :param x: (int) starting x-coordinate
    :param y: (int) starting y-coordinate
    :param length: (int) length of square size in pixels
    :return: (int) number of squares drawn
    """
    # Base Case
    if length <= 10:
        return 0

    # Recursive Case
    # start at the given coordinates
    setposition(x, y)
    # draw a square with side-length <length>
    draw_polygon(4, length)

    # recurse through the stairs function, drawing squares above and to the right of the square drawn in previous lines,
    # decreasing length by a factor of 2 each recursion
    stairs_above = stairs(x, y + length, length/2)
    stairs_right = stairs(x + length, y, length/2)
    return stairs_above + stairs_right + 1


def main_part1():
    """
    Draws the following: a dot at the origin; a triangle centered around the origin; polygons with 3, 4, 6, 12, and 32 sides;
    and a recursive staircase. Prints the number of squares in the recursive staircase
    :return: (None)
    """
    # draw a dot of size 5 in the center of the screen
    dot(5)

    # fancy geometry to calculate the starting point of an equilateral triangle at
    # the center of the screen
    # If you understand the math, great! If not, that's fine. Don't spend time 
    # worrying about it. This isn't a geometry class. 
    side_len = 60
    triangle_height = sqrt(side_len**2 - (side_len/2)**2) # use Pythagorean thm
    centroid_height = triangle_height/3  # centroid is 1/3 up the height
    y_init = -1 * centroid_height
    x_init = -1 * (side_len/2)

    # draw a single triangle of size 60 in the center of the screen
    penup()
    setposition(x_init,y_init)
    pendown()
    setheading(0)
    draw_triangle(60, "black")
    penup()

    # draw polygons with 3, 4, 6, 12, and 32 sides
    # try to make them not overlap!

    # draw a 3 sided polygon
    penup()
    setposition(0, 50)
    pendown()
    draw_polygon(3, 60)

    # draw a 4 sided polygon
    penup()
    setposition(0, 125)
    pendown()
    draw_polygon(4, 45)

    # draw a 6 sided polygon
    penup()
    setposition(0, 200)
    pendown()
    draw_polygon(6, 30)

    # draw a 12 sided polygon
    penup()
    setposition(100, 200)
    pendown()
    draw_polygon(12, 15)

    # draw a 32 sided polygon
    penup()
    setposition(100, 100)
    pendown()
    draw_polygon(32, 5.625)
    
    # draw a recursive staircase that looks like the (first) one on the handout
    print(stairs(-250, -250, 128))

    # hide turtle and preserve the display
    hideturtle()
    done()


def arms(x, y, size):
    """
    Draws 8 arms of length <size> originating from (x, y)
    :param x: (int) starting x-coordinate
    :param y: (int) starting y-coordinate
    :param size: (int) length of arm in pixels
    :return: (int) number of arms drawn
    """
    num_arms = 0

    # draw 8 snowflake arms originating from (x, y)
    for i in range(8):
        pencolor("black")
        setposition(x, y)
        pendown()
        forward(size)
        penup()
        setposition(x, y)
        left(45)
        num_arms += 1
    return num_arms


def red_dot(x, y):
    """
    Draws a red dot at (x, y)
    :param x: (int) x-coordinate
    :param y: (int) y-coordinate
    :return: red dot of size 5 pixels
    """
    setposition(x, y)
    pencolor("red")
    dot(5)
    penup()
    return


def snowflake(x, y, size):
    """
    Draws a recursive snowflake centered at the given position
    :param x: (int) x-value for center of snowflake
    :param y: (int) y-value for center of snowflake
    :param size: (int) length of arm in pixels
    :return: (int) total number of arms that were drawn
    """
    # Base Case
    # draw a red dot at (x, y) if <size> is less than 5
    if size < 5:
        red_dot(x, y)
        return 0

    # Recursive Case
    # draw snowflake arms
    main_arms = arms(x, y, size)
    # draw a recursive snowflake on the north arm, with size/3
    north_arms = snowflake(x, y + size, size/3)
    # draw a recursive snowflake on the east arm, with size/3
    east_arms = snowflake(x + size, y, size / 3)
    # draw a recursive snowflake on the south arm, with size/3
    south_arms = snowflake(x, y - size, size / 3)
    # draw a recursive snowflake on the west arm, with size/3
    west_arms = snowflake(x - size, y, size / 3)
    penup()

    # return the total number of arms drawn
    return main_arms + north_arms + east_arms + south_arms + west_arms


def main():
    """
    Draws a recursive snowflake and prints the number of arms (int) that were drawn in the recursion process
    :return: (None)
    """
    # draw a snowflake and print the number of arms that were drawn
    print(snowflake(0, 0, 100))

    # hide turtle and preserve the display
    hideturtle()
    done()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1