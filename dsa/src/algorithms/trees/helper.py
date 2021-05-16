"""
                    10
                  /     \
                5        15
              /   \    /    \   # noqa
            2      5  13     22
          /          /   \
        1           ?    14
"""


def traverse(root):
    traverse_helper([root])


def traverse_helper(nodes):
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
