import unittest


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


def bst_max(top):
    if not (top.data or top.left or top.right):
        raise ValueError("Empty tree")
    current_node = top
    while current_node:
        if not current_node.right:
            return current_node
        current_node = current_node.right


def bst_min(top):
    if not (top.data or top.left or top.right):
        raise ValueError("Empty tree")
    current_node = top
    while current_node:
        if not current_node.left:
            return current_node
        current_node = current_node.left


class TestMinAndMax(unittest.TestCase):

    def test_min_on_empty_tree(self):
        self.assertRaises(ValueError, lambda: bst_min(Node()))

    def test_max_on_one_element_tree(self):
        self.assertEqual(69, bst_max(Node(data=69)).data)

    def test_min(self):
        test_node = Node(data=2)
        test_node.insert(1)
        test_node.insert(3)
        test_node.insert(0)
        self.assertEqual(0, bst_min(test_node).data)

    def test_max(self):
        test_node = Node(data=3)
        test_node.insert(4)
        test_node.insert(1)
        test_node.insert(2)
        test_node.insert(6)
        test_node.insert(5)
        self.assertEqual(6, bst_max(test_node).data)


if __name__ == '__main__':
    unittest.main()
