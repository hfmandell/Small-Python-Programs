from ppm_modify import *


def main():
    # test negate
    print("*** testing negate ***")
    assert negate("1 2 3 200 100 150") == "254 253 252 55 155 105"
    assert negate("0 001 250 255") == "255 254 5 0"
    assert negate("111 111 101") == "144 144 154"
    assert negate("020 010 008") == "235 245 247"
    print("negate passed")

    # test grey_scale
    print("*** testing grey_scale ***")
    # TODO: add test cases to thoroughly test this function
    assert grey_scale("10 10 10") == "17 17 17"
    assert grey_scale("10 10 10 15 18 230") == "17 17 17 231 231 231"
    assert grey_scale("001 001 005 60 65 70 80 85 90") == "5 5 5 112 112 112 147 147 147"
    assert grey_scale("255 254 249") == "255 255 255"
    print("grey_scale passed")

    # test remove
    print("*** testing remove ***")
    # TODO: add test cases to thoroughly test this function
    assert remove_color("100 150 200", "red") == "0 150 200"
    assert remove_color("0 0 0", "red") == "0 0 0"
    assert remove_color("220 90 10", "green") == "220 0 10"
    assert remove_color("70 255 133", "green") == "70 0 133"
    assert remove_color("120 208 30", "blue") == "120 208 0"
    assert remove_color("33 43 53 63 73 83", "green") == "33 0 53 63 0 83"
    print("remove passed")


if __name__ == "__main__":
    main()
