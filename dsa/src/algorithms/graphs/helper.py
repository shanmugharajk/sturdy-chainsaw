from typing import List

from .node import Node


def depth_first_search(node: Node, arr: List[int]):
    arr.append(node.value)

    for child in node.children:
        depth_first_search(child, arr)


def main():
    start_node = "A"
    nodes = [
        {"children": ["B", "C", "D"], "id": "A", "value": "A"},
        {"children": ["E", "F"], "id": "B", "value": "B"},
        {"children": [], "id": "C", "value": "C"},
        {"children": ["G", "H"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": ["I", "J"], "id": "F", "value": "F"},
        {"children": ["K"], "id": "G", "value": "G"},
        {"children": [], "id": "H", "value": "H"},
        {"children": [], "id": "I", "value": "I"},
        {"children": [], "id": "J", "value": "J"},
        {"children": [], "id": "K", "value": "K"},
    ]

    root = Node.graph(nodes, start_node)
    arr = []
    depth_first_search(root, arr)
    print(arr)
