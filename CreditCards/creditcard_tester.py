from creditcard_part1 import last_digit, decimal_right_shift, sum_digits
from creditcard import verify, generate


def main():
    # test last_digit
    print("*** testing last_digit function ***")
    assert type(last_digit(123)) == int
    assert last_digit(1) == 1
    assert last_digit(47) == 7
    assert last_digit(1234567890) == 0
    print("last_digit passed")

    # test decimal_right_shift
    print("*** testing decimal_right_shift ***")
    assert type(decimal_right_shift(15)) == int
    assert decimal_right_shift(1) == 0
    assert decimal_right_shift(47) == 4
    assert decimal_right_shift(1234567890) == 123456789
    print("decimal_right_shift passed")

    # test sum_digits
    print("*** testing sum_digits ***")
    assert type(sum_digits(471)) == int
    assert sum_digits(000) == 0
    assert sum_digits(123) == 6
    assert sum_digits(909) == 18
    print("sum_digits passed")

    print("PART 1: ALL TESTS PASSED")

    # test verify
    print("*** testing verify function***")
    assert type(verify(1111111111112)) == bool
    assert verify(2000000000001) == False
    assert verify(1111111111112) == True
    assert verify(9813428854407) == True
    assert verify(1111111111111) == False
    assert verify(1234567890123) == False
    assert verify(5678900731496) == True
    assert verify(7898768410243) == True
    print("verify passed")

    # test generate
    print("*** testing generate function ***")
    assert type(generate(111111)) == int
    assert verify(generate(123456)) == True
    assert verify(generate(830129)) == True
    assert verify(generate(567890)) == True
    assert verify(generate(0o10101)) == True
    print("generate passed")

    print("PART 2: ALL TESTS PASSED")


if __name__ == "__main__":
    main()
