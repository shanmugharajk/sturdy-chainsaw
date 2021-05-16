from algorithms.utils import BST, traverse


def find_closest_node(tree: BST, target: int):
    diff = abs(target - tree.value)
    closest = tree.value
    ptr = tree

    while ptr is not None:
        curr_diff = abs(target - ptr.value)
        diff = min(diff, curr_diff)

        closest = ptr.value if curr_diff <= diff else closest
        ptr = ptr.left if ptr.value > target else ptr.right

    return closest


def main():
    tree = BST(100)
    tree.insert(502)
    tree.insert(55000)
    tree.insert(1001)
    tree.insert(4500)
    tree.insert(204)
    tree.insert(205)
    tree.insert(207)
    tree.insert(208)
    tree.insert(206)
    tree.insert(203)
    tree.insert(5)
    tree.insert(15)
    tree.insert(22)
    tree.insert(57)
    tree.insert(60)
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(-51)
    tree.insert(-40)

    traverse(tree)

    print(find_closest_node(tree, 30000))
