class Node:
    def __init__(self, value):
        """
        Initializes a node with a value and pointers to left and right children, which are initially None.
        :param value: The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initializes an empty binary tree with no root node.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary tree. If the tree is empty, the new value becomes the root.
        Otherwise, it delegates the insertion to the helper method _insert.
        :param value: The value to be inserted.
        """
        if self.root is None:
            self.root = Node(value)  # Create the root node if the tree is empty.
        else:
            self._insert(self.root, value)  # Call the helper method for insertion.

    def _insert(self, current, value):
        """
        Helper method for inserting a value into the binary tree.
        Places the value in the left or right subtree based on comparison.
        :param current: The current node being examined.
        :param value: The value to be inserted.
        """
        if value < current.value:
            # If the value is less than the current node's value, go to the left subtree.
            if current.left is None:
                current.left = Node(value)  # Create a new node if the left child is empty.
            else:
                self._insert(current.left, value)  # Recur on the left child.
        else:
            # If the value is greater than or equal to the current node's value, go to the right subtree.
            if current.right is None:
                current.right = Node(value)  # Create a new node if the right child is empty.
            else:
                self._insert(current.right, value)  # Recur on the right child.

    def search(self, value):
        """
        Searches for a value in the binary tree.
        :param value: The value to search for.
        :return: True if the value is found, False otherwise.
        """
        return self._search(self.root, value)  # Start the search from the root.

    def _search(self, current, value):
        """
        Helper method for searching a value in the binary tree.
        :param current: The current node being examined.
        :param value: The value to search for.
        :return: True if the value is found, False otherwise.
        """
        if current is None:
            return False  # Reached a leaf node, value not found.
        if current.value == value:
            return True  # Value found.
        elif value < current.value:
            return self._search(current.left, value)  # Search in the left subtree.
        else:
            return self._search(current.right, value)  # Search in the right subtree.

    def in_order_traversal(self):
        """
        Performs an in-order traversal of the tree (left, root, right) and returns the values in a list.
        :return: List of values in in-order traversal order.
        """
        result = []
        self._in_order_traversal(self.root, result)  # Start traversal from the root.
        return result

    def _in_order_traversal(self, current, result):
        """
        Helper method for in-order traversal.
        :param current: The current node being examined.
        :param result: The list collecting the traversal result.
        """
        if current:
            self._in_order_traversal(current.left, result)  # Recur on the left subtree.
            result.append(current.value)  # Visit the root node.
            self._in_order_traversal(current.right, result)  # Recur on the right subtree.

    def pre_order_traversal(self):
        """
        Performs a pre-order traversal of the tree (root, left, right) and returns the values in a list.
        :return: List of values in pre-order traversal order.
        """
        result = []
        self._pre_order_traversal(self.root, result)  # Start traversal from the root.
        return result

    def _pre_order_traversal(self, current, result):
        """
        Helper method for pre-order traversal.
        :param current: The current node being examined.
        :param result: The list collecting the traversal result.
        """
        if current:
            result.append(current.value)  # Visit the root node.
            self._pre_order_traversal(current.left, result)  # Recur on the left subtree.
            self._pre_order_traversal(current.right, result)  # Recur on the right subtree.

    def post_order_traversal(self):
        """
        Performs a post-order traversal of the tree (left, right, root) and returns the values in a list.
        :return: List of values in post-order traversal order.
        """
        result = []
        self._post_order_traversal(self.root, result)  # Start traversal from the root.
        return result

    def _post_order_traversal(self, current, result):
        """
        Helper method for post-order traversal.
        :param current: The current node being examined.
        :param result: The list collecting the traversal result.
        """
        if current:
            self._post_order_traversal(current.left, result)  # Recur on the left subtree.
            self._post_order_traversal(current.right, result)  # Recur on the right subtree.
            result.append(current.value)  # Visit the root node.

# Example Usage
bt = BinaryTree()
bt.insert(10)  # Insert 10 as the root node.
bt.insert(5)   # Insert 5 into the left subtree.
bt.insert(15)  # Insert 15 into the right subtree.
bt.insert(2)   # Insert 2 into the left subtree of 5.
bt.insert(7)   # Insert 7 into the right subtree of 5.

# Perform various operations and display their results.
print("In-order Traversal:", bt.in_order_traversal())  # Output: [2, 5, 7, 10, 15]
print("Pre-order Traversal:", bt.pre_order_traversal())  # Output: [10, 5, 2, 7, 15]
print("Post-order Traversal:", bt.post_order_traversal())  # Output: [2, 7, 5, 15, 10]
print("Search 7:", bt.search(7))  # Output: True (7 is in the tree)
print("Search 20:", bt.search(20))  # Output: False (20 is not in the tree)
