from typing import List

from .bst import BST


"""
                    10
                  /     \
                5        15
              /   \    /    \   # noqa
            2      5  13     22
          /          /   \
        1           ?    14
"""


def traverse(root: BST):
    traverse_helper([root])


def traverse_helper(nodes: List[BST]):
    visited = []

    for node in nodes:
        print(node.value, end=" ")

        if node.left:
            visited.append(node.left)

        if node.right:
            visited.append(node.right)

    print()

    if len(visited) > 0:
        traverse_helper(visited)


def main():
    root = BST(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(5)
    root.insert(13)
    root.insert(22)
    root.insert(1)
    root.insert(12)
    root.insert(14)

    traverse(root)
