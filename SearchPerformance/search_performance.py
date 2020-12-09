"""
    CS051P Lab Assignments: Search Performance

    Author: Hannah Mandell

    Date:   11 - 14 - 19

    The goal of this assignment is to implement a few basic search
    algorithms and measure their performance.  As such, it is also
    an introduction to algorithmic complexity.
"""
import random
import time
import matplotlib.pyplot as plt


def list_of_integers(size):
    """
    Returns a list of integers with length size
    :param size: (int)
    :return: (list) a list with the specified number of random integer values (between 1 and 2*size)
    """
    # create an empty list
    int_list = []

    # make a non-random integer list that is length size by:
    # for every number that is in the range from 0 to size
    for i in range(size):
        # add an integer that is in the range (1, 2*size) to int_list
        int_list.append(random.randint(1, 2*size))

    # return the now full list of random integers that is length size
    return int_list


def linear_search(alist, value):
    """
    Implements a linear search of an unsorted alist for a specified value
    :param alist: (list) a list of ints
    :param value: (int) the value we are searching for
    :return: (int) the index of value in alist or -1 if value is not in alist
    """
    # initialize the starting index as 0
    index = 0

    # loop through every element in alist
    for i in alist:
        # if the element is equal to value return the index of the element
        if i == value:
            return index
        # if the element is not equal to the value, add 1 to index and
        # move onto the next element in the for loop
        index += 1

    # return -1 if none of the elements in the list are equal to value
    return -1


def binary_search(alist, value):
    """
    Takes a list and a value and calls the helper function binary_search_helper
    :param alist: (list) a list of ints
    :param value: (int) the value we are searching for
    :return: (int) the index of value in alist or -1 if the value is not in alist
    """
    # call and return binary search on the given list and value
    return binary_search_helper(alist, value, 0, len(alist))


def binary_search_helper(alist, value, start, end):
    """
    Takes a list with start and end indexes and returns the index of value in alist or -1 if the value is not in alist
    :param alist: (list) a list of ints
    :param value: (int) the value we are searching for
    :param start: (int) starting index of a list
    :param end: (int) exclusive ending index of a list
    :return: (int) the index of value in alist or -1 if the value is not in alist
    """
    # define middle
    middle = (end + start) // 2

    # Base Case
    # if the list is empty because we have recursed through all the possible
    # indexes and have not found one that equals value, return -1
    if start - end == 0:
        return -1

    # Recursive Case
    # if the middle element in alist is equal to value, append its index
    if alist[middle] == value:
        return middle

    # if the middle element in alist is greater than value
    elif alist[middle] > value:
        # recurse the function for the first half of alist, not including the middle element
        return binary_search_helper(alist, value, start, middle)

    # if the middle element in alist is less than value
    elif alist[middle] < value:
        # recurse the function for the last half of alist, not including the middle element
        return binary_search_helper(alist, value, middle + 1, end)


def main_part1():
    # create a list of 500 non-random integers
    list1 = list_of_integers(500)
    # perform a linear search for a number in that list
    linear_search(list1, list1[220])
    # perform a linear search for a number not in that list
    linear_search(list1, -50) 
    # sort the list
    list1.sort()
    # perform a binary search for a number in that list
    binary_search(list1, list1[220])
    # perform a binary search for a number not in that list
    binary_search(list1, -50)


def sorted_comparison(min_size, max_size):
    """
    Create (and then sort) lists of different lengths (from min-max), for each:
        time the execution of a linear search for a number not in the list
        time the execution of a a binary search for the same number
    :param min_size: (int) minimum list size
    :param max_size: (int) maximum list size
    :return: (list) a list of (size, linear time, binary time) tuples
    """
    size = min_size
    sorted_tuple_data_list = []

    while size <= max_size:

        # create a list of non-random numbers with length size
        rand_list = list_of_integers(size)

        # sort that list from smallest to greatest
        rand_list.sort()

        # time the linear search of the sorted list for a value not in the list
        linear_start = time.time()
        linear_search(rand_list, 3*size)
        linear_end = time.time()
        linear_elapsed_time_in_seconds = linear_end - linear_start

        # time the binary search of the sorted list for a value not in the list
        binary_start = time.time()
        binary_search(rand_list, 3*size)
        binary_end = time.time()
        binary_elapsed_time_in_seconds = binary_end - binary_start

        # create a tuple that holds the values of size and the times it took for linear and binary searches
        time_data = (size, linear_elapsed_time_in_seconds, binary_elapsed_time_in_seconds)

        # append the tuple to a list
        sorted_tuple_data_list.append(time_data)

        # double size for the next iteration
        size = 2 * size
        
    return sorted_tuple_data_list  # return list of three-element-tuples


def unsorted_comparison(min_size, max_size):
    """
    Create (unsorted) lists of different lengths (from min-max), for each:
        time the execution of a linear search for a number not in the list
        time the execution of a sort followed by a binary search for same number
    :param min_size: (int) the min length of a list
    :param max_size: (int) the max length of a list
    :return: (list) a list of (size, linear time, binary time) tuples
    """
    # initialize size as min_size to start
    size = min_size
    # create an empty list to put the tuple data into
    unsorted_tuple_data_list = []

    # continue the while loop while size is less than or equal to the given max_size
    while size <= max_size:

        # create a list of non-random numbers with length size
        rand_list = list_of_integers(size)

        # time the linear search of the unsorted list for a value not in the list
        linear_start = time.time()
        linear_search(rand_list, 3*size)
        linear_end = time.time()
        linear_elapsed_time_in_seconds = linear_end - linear_start

        # time the sorting of the list and a binary search of the sorted list for a value not in the list
        binary_start = time.time()
        rand_list.sort()  # sort rand_list
        binary_search(rand_list, 3*size)
        binary_end = time.time()
        binary_elapsed_time_in_seconds = binary_end - binary_start

        # create a tuple that holds the values of size and the times it took for linear and binary searches
        time_data = (size, linear_elapsed_time_in_seconds, binary_elapsed_time_in_seconds)

        # append the tuple to a list
        unsorted_tuple_data_list.append(time_data)

        # double size for the next iteration
        size = 2 * size

    return unsorted_tuple_data_list  # return the list of three-element-tuples


def plot_comparison(data, title, outfile=None):
    """
    comparison graph for time vs list size
        for linear and binary searches
    :param (list) data: list of (n, linear, binary) tuples
    ;param (str) title: title of this graph
    """
    # plot the first data series (linear searches)
    xlist = [d[0] for d in data]
    ylist = [d[1]*1000 for d in data]   # S*1000 = ms
    plt.plot(xlist, ylist, 'r+')

    # plot the second data series (binary searches)
    ylist = [d[2]*1000 for d in data]   # S*1000 = ms
    plt.plot(xlist, ylist, 'go')

    # label the graph
    plt.xlabel("list length")
    plt.ylabel("execution time(ms)")
    plt.title(title)

    # create a legend for the two data series
    plt.legend(["linear search", "binary search"])

    # produce the output, either to the screen or a file
    if outfile is None:
        plt.show()
    else:
        print("Saving " + title + " in " + outfile)
        plt.savefig(outfile)
        plt.close()


def main():
    # 1. run and gather the results from sorted_comparison(2, 1045576)
    sorted_comp = sorted_comparison(2, 1045576)

    # 2. run and gather the results from unsorted_comparison(2, 1045576)
    unsorted_comp = unsorted_comparison(2, 1045576)

    # 3. plot comparisons of binary vs sorted/unsorted linear searches
    plot_comparison(sorted_comp, "Run Time of Sorted Searches")
    plot_comparison(unsorted_comp, "Run Time of Unsorted Searches")


if __name__ == "__main__":
    main()            # un-comment for part 2
    # main_part1()        # comment out for part 2
