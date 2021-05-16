from algorithms.linked_lists import SinglyLinkedList, singly_linked_list, traverse


def remove_duplicates(lst: SinglyLinkedList):
    cur, ptr = lst, lst.next

    while ptr:
        if cur.value != ptr.value:
            cur.next = ptr
            cur = ptr

        ptr = ptr.next

    cur.next = None

    return lst


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

    res = remove_duplicates(lst)
    traverse(res)
