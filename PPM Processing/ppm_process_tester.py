from ppm_process import *


def main():
    # test process
    print("*** testing process ***")
    assert process(["255 0 0", "0 255 0", "0 0 255"], 3, 1) == [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
    assert process(["255 100 50"], 1, 1) == [[255, 100, 50]]
    assert process([" 255      100 50"], 1, 1) == [[255, 100, 50]]
    assert process(["255 100 50", "", "30 35 40"], 1, 1) == [[255, 100, 50], [30, 35, 40]]
    assert process(["40 50", "60", "70 80 90"], 2, 1) == [[40, 50, 60], [70, 80, 90]]
    assert process(["50 75 100 125", "150 175 200 225 250"], 3, 1) == [[50, 75, 100], [125, 150, 175], [200, 225, 250]]
    assert type(process(["255 100 50"], 1, 1)) == list
    assert type(process(["255 100 50"], 1, 1)[0][0]) == int
    print("process passed")

    # test scale
    print("*** testing scale ***")
    assert scale([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 1) == [[1, 2, 3], [7, 8, 9]]
    assert scale([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 100, 3) == [[1, 2, 3]]
    assert scale([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 50) == [[1, 2, 3]]
    assert len(scale(read_ppm("files/pomona.ppm"), 2, 2)) == 240
    assert scale([[255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255],
     [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255],
     [255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255, 0],
     [0, 255, 255, 255, 0, 255, 0, 0, 0, 255, 0, 0],
     [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255],
     [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255]], 3, 1) == [[255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255],
     [0, 255, 255, 255, 0, 255, 0, 0, 0, 255, 0, 0]]
    print("scale passed")


if __name__ == "__main__":
    main()
