from typing import List
from algorithms.trees import BT


def branch_sum(tree: BT):
    arr = []
    branch_sum_helper(tree, 0, arr)
    return arr


def branch_sum_helper(tree: BT, cur_sum=0, arr: List[int] = []):
    if tree is None:
        return

    cur_sum += tree.value

    if tree.right is None and tree.left is None:
        arr.append(cur_sum)
        return

    branch_sum_helper(tree.left, cur_sum, arr)
    branch_sum_helper(tree.right, cur_sum, arr)


def main():
    tree = BT(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)

    print(branch_sum(tree))
