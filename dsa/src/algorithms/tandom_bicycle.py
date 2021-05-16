from typing import List


def tandom_bicycle(red: List[int], blue: List[int], fastest: bool):
    red.sort()
    blue.sort()

    if fastest:
        blue = list(reversed(blue))

    speed = 0

    for idx in range(len(red)):
        speed += max(red[idx], blue[idx])

    return speed


def main():
    red = [5, 5, 3, 9, 2]
    blue = [3, 6, 7, 2, 1]
    print(tandom_bicycle(red, blue, True))
