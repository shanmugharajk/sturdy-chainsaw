from __future__ import annotations

from typing import List

from .helper import traverse


class BT:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"(BT) {self.value}"

    def insert(self, value):
        node = BT.find_node_to_insert([self])

        if node.left:
            node.right = BT(value)
        else:
            node.left = BT(value)

    @staticmethod
    def find_node_to_insert(nodes: List[BT] = []):
        visited = []

        for node in nodes:
            if node.left is None or node.right is None:
                return node

            if node.left:
                visited.append(node.left)

            if node.right:
                visited.append(node.right)

        if len(visited) > 0:
            return BT.find_node_to_insert(visited)


def main():
    tree = BT(1)

    for idx in range(2, 11):
        tree.insert(idx)

    traverse(tree)
