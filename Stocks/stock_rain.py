"""
    CS051P Lab Assignments: Stock v.s. Rain

    Author: Hannah Mandell

    Date:   11 - 19 - 19

    The goal of this assignment is to familiarize you with data analysis
    and visualization. You'll practice handling files in csv format,
    create and manipulate Python dictionaries, and do some basic plotting
    using the matplotlib package.
"""
import matplotlib.pyplot as plt


def parse_rainfall(fname):
    """
    Takes a file of rainfall data and returns a dictionary of {str(date) : float(total precipitation for that date in Seattle)}
    :param fname: (str) name of a file containing Seattle rainfall data
    :return: (dict) a dictionary of floats that represent the total precipitation recorded for each date in Seattle
    """
    # open the file
    file_in = open(fname, "r")

    # create an empty dictionary to put the dates and rainfall data into
    rainfall_dict = {}

    # skip the first line because it is just the column titles
    file_in.readline()

    # for the rest of the lines in the file:
    for line in file_in:

        # turn the line into a list of data values
        data_lst = line.split(",")

        # if there is no data for a particular day, don't create an entry
        if '''"NA"''' in data_lst:
            continue

        # if there is rainfall data for a particular day:
        else:
            # create a dictionary entry for the date and its precipitation
            date = data_lst[0].strip('"')
            rainfall_dict[date] = float(data_lst[1])

        # clear data_lst so that it can be used in the next for loop iteration
        data_lst.clear()

    # return the dictionary of dates and precipitation
    return rainfall_dict


def parse_stock_helper(data_lst):
    """
    Takes a list of data and returns it with the date in the correct format
    :param data_lst: (list) list of data in the form of [month/day/last two digits of the year, open, high, low, close, volume, name]
    :return: (list) list of data in the form of [four digit year-month-day, open, high, low, close, volume, name]
    """
    new_data_lst = data_lst

    # create a list of the month, day, and year of the old date
    old_date = data_lst[0]
    old_date_lst = old_date.split("/")

    # reformat the month into a two-digit value if necessary
    month = old_date_lst[0]
    if len(month) < 2:
        month = "0" + month

    # reformat the day into a two-digit value if necessary
    day = old_date_lst[1]
    if len(day) < 2:
        day = "0" + day

    # reformat the year into a four digit value
    year = "20" + old_date_lst[2]

    # create the new_date string
    new_date = year + "-" + month + "-" + day

    # replace the old date with the reformatted date
    new_data_lst[0] = new_date
    # return the data list with the reformatted date
    return new_data_lst


def parse_stock(fname, sym):
    """
    Takes a file of stock data and returns a dictionary of {str(date) : float(change in stock price)}
    :param fname: (str) name of a file containing stock data
    :param sym: (str) a stock symbol
    :return: (dict) a dictionary of floats that represent the day's change in price, defined as Close minus Open
    """
    # open the file
    file_in = open(fname, "r")

    # create an empty dictionary to put the dates and stock data into
    stock_dict = {}

    # skip the first line because it is just the column titles
    file_in.readline()

    # go through each line in the file
    for line in file_in:

        # do nothing for the last line of the file because it's just whitespace
        if line == "\n":
            continue

        # turn the line into a list of data values and change the date into the correct format
        data_lst = parse_stock_helper(line.split(","))

        # if there is an empty data entry, don't create a dictionary entry
        if data_lst[1] == "" or data_lst[4] == "":
            continue

        # if all of the data for the date is available:
        else:

            # remove the whitespace from the symbol in the data
            symbol = data_lst[6].strip()

            # if the symbol matches the value given as sym
            if symbol == sym:

                # create a dictionary entry for the date and its stock price change
                open_price = float(data_lst[1])
                close_price = float(data_lst[4])
                stock_dict[data_lst[0]] = round((close_price - open_price), 2)

            # if sym is not present in the input data, do not include the line's data
            else:
                continue

        # clear data_lst so that it can be used in the next for loop iteration
        data_lst.clear()

    # return the dictionary of dates and stock price changes
    return stock_dict


def correlate_data(stock_dict, rain_dict):
    """
    Takes a stock_dict and a rain_dict and returns a list of data containing stock price change and rainfall for specific dates
    :param stock_dict: (dict) a dictionary mapping date strings to floats representing daily changes in stock prices
    :param rain_dict: (dict) a dictionary mapping date strings to floats representing rainfall daily totals
    :return: (list) a list where each item represents a [stock_price_change, rainfall] pair
    """
    # create an empty list to put the stock and rain data into
    correlate_data_lst = []

    # go through each date in stock_dict
    for date in stock_dict.keys():

        # if rain_dict has a key of the same exact date
        if date in rain_dict.keys():
            correlate_data_lst.append([stock_dict[date], rain_dict[date]])

    # return the list of tuples
    return correlate_data_lst


def scatter_plot(data, format, name, done):
    """
    Plots the data in <data>, showing rain on the x-axis and stock price change on the y-axis. Will only display
    the plot and the legend if <done> is True
    :param data: (list) a list where each entry is a list of [stock price change, rainfall]
    :param format: (str) a matplotlib format string
    :param name: (str) a string that tells whose data is being passed in
    :param done: (bool) True if and only if this is the last plot. Determines when to call plt.legend() and plt.show()
    """
    # put the corresponding x (rain) and y (stock) data into separate lists
    stock_values = []
    rain_values = []

    # go through each nested list in the data list
    for data_tuple in data:
        index = 0

        # go through the data set in the nested list
        for value in data_tuple:

            # append the stock data to the stock_value list
            if index == 0:
                stock_values.append(value)

            # append the rain data to the rain_value list
            else:
                rain_values.append(value)
            index += 1

    # plot the data
    plt.plot(rain_values, stock_values, format, label = name)

    # label the axis
    plt.xlabel("Rain (in.)")
    plt.ylabel("Stock Price Change ($)")

    # title the plot
    plt.title("The Effect of Seattle Rainfall on Price Change of Stocks")


    # if done is true, display the plot and legend
    if done:
        plt.legend()
        plt.show()


def main():

    # ask the user for a rainfall data file
    rain_file = input("Enter a rainfall data file:\n\t")

    # ask the user for a stock data file
    stock_file = input("Enter a stock data file:\n\t")

    # ask the user for a stock symbol for a tech company in Seattle
    seattle_sym = input("Enter a stock symbol for a technology company located in Seattle:\n\t")

    # make sure it is a valid input
    while seattle_sym != "MSFT" and seattle_sym != "AMZN":
        # if it is not valid, ask again
        seattle_sym = input("Invalid input.\nEnter a stock symbol for a technology company located in Seattle:\n\t")

    # ask the user for a stock symbol of a tech company not located near Seattle
    other_sym = input("Enter a stock symbol for another technology company not located near Seattle:\n\t")


    # plot (but do not display yet) the data for Seattle rainfall and change in the Seattle stock company
    # 1: data processing - call parse_rainfall and parse_stock on the Seattle company for data processing
    rainfall_data = parse_rainfall(rain_file)
    stock = seattle_sym
    stock_data = parse_stock(stock_file, stock)

    # 2: data analysis and visualization - call correlated_data and scatter_plot on the Seattle company
    data = correlate_data(stock_data, rainfall_data)
    scatter_plot(data, 'b.', stock, False)


    # plot the data for Seattle rainfall and change in the non-Seattle stock company
    # 1: data processing - call parse_rainfall and parse_stock on the non-Seattle company
    stock = other_sym
    stock_data = parse_stock(stock_file, stock)

    # 2: data analysis and visualization - call correlated_data and scatter_plot on the non-Seattle company
    data = correlate_data(stock_data, rainfall_data)

    # display both plots now
    scatter_plot(data, 'r+', stock, True)


if __name__ == '__main__':
    main()
