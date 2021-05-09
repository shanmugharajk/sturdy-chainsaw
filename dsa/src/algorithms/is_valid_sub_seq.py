from typing import List


def is_valid_sub_seq(array: List[int], sequence: List[int]):
    seq_ptr = 0

    for num in array:
        if sequence[seq_ptr] == num:
            seq_ptr += 1

        if seq_ptr == len(sequence):
            break

    return seq_ptr == len(sequence)


def main():
    print(is_valid_sub_seq([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
