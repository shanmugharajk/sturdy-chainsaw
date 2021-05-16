from typing import List


def class_photos(red: List[int], blue: List[int]):
    red.sort()
    blue.sort()

    print(red)
    print(blue)

    trend = "red" if red[0] > blue[0] else "blue"

    for idx in range(len(red)):
        if trend == "red" and red[idx] <= blue[idx]:
            return False

        if trend == "blue" and red[idx] >= blue[idx]:
            return False

    return True


def main():
    red = [6, 9, 2, 4, 5, 1]
    blue = [5, 8, 1, 3, 4, 9]
    print(class_photos(red, blue))
