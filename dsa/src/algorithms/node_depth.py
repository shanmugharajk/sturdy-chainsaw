from typing import List

from algorithms.trees import BT


def node_depth(tree: BT):
    return node_depth_helper([tree])


def node_depth_helper(nodes: List[BT], curr_depth=0, depth: int = -1):
    visited = []

    for node in nodes:
        curr_depth += depth + 1

        if node.right:
            visited.append(node.right)

        if node.left:
            visited.append(node.left)

    depth += 1

    if len(visited) > 0:
        return node_depth_helper(visited, curr_depth, depth)

    return curr_depth


def main():
    root = BT(1)

    for idx in range(2, 10):
        root.insert(idx)

    print(node_depth(root))
