from typing import List


def two_num_sum(arr: List[int], target: int):
    kv = {}

    for num in arr:
        req = target - num

        if req in kv:
            return [num, req]

        kv[num] = 0

    return []


def two_num_sum2(arr: List[int], target: int):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        left_value = arr[left]
        right_value = arr[right]
        curr_sum = left_value + right_value

        if curr_sum == target:
            return [left_value, right_value]

        if curr_sum < target:
            left += 1
        else:
            right -= 1

    return []


def main():
    print(two_num_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_num_sum2([3, 5, -4, 8, 11, 1, -1, 6], 10))
