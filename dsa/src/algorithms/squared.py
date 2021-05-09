from typing import List


def gr(val1, val2):
    return abs(val1) > abs(val2)


def squared(arr: List[int]):
    res = []
    le, ri = 0, len(arr) - 1

    while le <= ri:
        if gr(arr[le], arr[ri]):
            res.append(arr[le] * arr[le])
            le += 1
        else:
            res.append(arr[ri] * arr[ri])
            ri -= 1

    res.reverse()
    return res


def main():
    # arr = [81, 16,  9, 1, 4, 9, 16, 25]
    # print(squared([-9, -4, -3, 1, 2, 3, 4, 5]))
    print(squared([1, 2, 3, 5, 6, 8, 9]))
