from typing import List


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    @staticmethod
    def get_nodes(nums: List[str]):
        return list(map(lambda num: Node(num), nums))

    @staticmethod
    def graph(nodes, start_node):
        root = Node(start_node)

        cache = {}
        cache[root.value] = root

        for node in nodes:
            childrens = Node.get_nodes(node["children"])

            for child in childrens:
                cache[child.value] = child

            cache[node["value"]].children = childrens

        return root
