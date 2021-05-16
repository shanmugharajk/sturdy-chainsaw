from typing import Any, List

from .singly_linked_list import SinglyLinkedList


def singly_linked_list(nodes: List[Any]):
    kv = {}

    for node in nodes:
        kv[node["id"]] = node

    ptr = lst = SinglyLinkedList(nodes[0]["value"])

    for node in nodes:
        if node["next"]:
            ptr.next = SinglyLinkedList(kv[node["next"]]["value"])
            ptr = ptr.next

    return lst


def traverse(lst: SinglyLinkedList):
    while lst:
        pointer = "->" if lst.next else ""
        print(f"{lst.value} {pointer}", end=" ")
        lst = lst.next

    print()


def main():
    nodes = [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ]

    lst = singly_linked_list(nodes)
    traverse(lst)
