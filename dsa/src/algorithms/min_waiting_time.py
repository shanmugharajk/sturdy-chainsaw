from typing import List


def min_waiting_time(queries: List[int]):
    queries.sort()

    prev, wait_time = 0, 0

    for num in queries:
        wait_time += prev
        prev += num

    return wait_time


def main():
    print(min_waiting_time([3, 2, 1, 2, 6]))
