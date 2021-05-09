from typing import List


def non_constructible_change(coins: List[int]):
    # [1, 1, 2, 3, 5, 7, 22]
    # [  0,    1,    2,    3,    4,    5,    6,    7 ....]
    #          |
    #    |  min coin
    # initial

    coins.sort()
    min_change = 0

    for coin in coins:
        req = min_change + 1

        if coin <= req:
            min_change += coin
        else:
            return req

    return min_change + 1


def main():
    print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))
    print(non_constructible_change([1] * 10))
