"""
                    10
                  /     \
                5        15
              /   \    /    \   # noqa
            2      5  13     22
          /          /   \
        1           ?    14
"""


from __future__ import annotations


class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return f"BST: {self.value}"

    def insert(self, value):
        prev, node = self, self

        while node is not None:
            prev = node
            node = node.left if node.value > value else node.right

        if prev.value > value:
            prev.left = BST(value)
        else:
            prev.right = BST(value)

        return self

    def contains(self, value):
        curr = self

        while curr is not None:
            if curr.value == value:
                return True

            curr = curr.left if curr.value > value else curr.right

        return False

    def remove(self, value):
        parent, node = self.node(value)

        if node is None:
            return self

        child_info = node.child_info()

        # root or both children
        if self.value == value or child_info == "both":
            # root node and no child 👉 nothing to do.
            if child_info == "none":
                return self

            # no right node at all so just take left.left and assign it to node.left
            if node.right is None:
                node.value = node.left.value
                node.left = node.left.left
                return self

            # both children
            min_value = node.right.min_node()

            # duplicate node 👉 node = 5 and node.right = 5
            if node.right.value == min_value:
                node.value = min_value
                node.right = node.right.right
                return self

            # filter the immediate duplicate otherwise it will do infinite loop
            node.remove(min_value)
            node.value = min_value

            return self

        if child_info != "both":
            to_patch = node.left if child_info == "left" else node.right

            if parent.value > value:
                parent.left = to_patch
            else:
                parent.right = to_patch

            return self

        return self

    # utils
    def child_info(self):
        if self.right and self.left:
            return "both"
        if self.left:
            return "left"
        if self.right:
            return "right"
        return "none"

    def node(self, value):
        parent, node = self, self

        while node:
            if node.value == value:
                return [parent, node]

            parent = node
            node = node.left if node.value > value else node.right

        return [parent, node]

    def min_node(self):
        node = self

        while node.left:
            node = node.left

        return node.value
