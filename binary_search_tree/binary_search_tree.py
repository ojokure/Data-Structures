# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class NodeTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.tree = NodeTree(value)

    # Insert the given value into the tree
    def insert(self, value):
        # if self.tree.value is None:
        #     self.tree.value = value
        #     return
        # else:
        current_node = self
        while current_node:
            # check if our current node value is greater than the value to insert
            if current_node.value > value:
                # go left
                if current_node.left:
                    # if there's a left child set that to the tree(current_node) and repeat
                    current_node = current_node.left
                else:
                    # else our node leaf is home
                    current_node.left = BinarySearchTree(value)
                    return
            else:
                # go right
                if current_node.right:
                  # if there's a right child set that to the tree(current_node) and repeat
                    current_node = current_node.right
                else:
                    # else our node leaf is home
                    current_node.right = BinarySearchTree(value)
                    return
        return

    def contains(self, target):

        current_node = self

        contains_target = False

        if current_node.value == target:
            contains_target = True
            return contains_target

        # else:
        while current_node:
            if current_node.value > target:
                # go left
                if current_node.left:
                    current_node = current_node.left
                    break

            else:

                if current_node.value == target:
                    contains_target = True
                    break

                if current_node.right:
                    current_node = current_node.right
                    break

        return contains_target

    # def get_max(self):
    #     current_node = self
    #     def get_max_helper(current_node):
    #         if current_node.right is None:
    #             return current_node.value
    #         return get_max_helper(current_node.right)
    #     return get_max_helper(current_node)

    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right

        return current_node.value

    def for_each(self, cb):
        current_node = self
        cb(current_node.value)

        def for_each_helper(current_node, cb):
            if current_node is None:
                return
            else:
                cb(current_node.value)
                for_each_helper(current_node.right, cb)
                for_each_helper(current_node.left, cb)
                return
        return for_each_helper(current_node, cb)

    # DAY 2 Project - ----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    # def in_order_print(self, node, array):
    #     array = []
    #     if not node:
    #         return array
    #     else:
    #         array = self.pre_order_dft(node.left, array)
    #         array.append(node.value)
    #         array = self.pre_order_dft(node.right, array)
    #     return array

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # def bft_print(self, node):
    #     pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # def dft_print(self, node):
    #     pass

    # STRETCH Goals - ------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    # def pre_order_dft(self, node, array):
    #     array = []
    #     if not node:
    #         return array
    #     else:
    #         array.append(node.value)
    #         array = self.pre_order_dft(node.left, array)
    #         array = self.pre_order_dft(node.right, array)
    #     return array

    # print(pre_order_dft)

    # Print Post-order recursive DFT

    # def post_order_dft(self, node, array):
    #     array = []
    #     if not node:
    #         return array
    #     else:
    #         array = self.post_order_dft(node.left, array)
    #         array = self.post_order_dft(node.right, array)
    #         array.append(node.value)
    #     return array

    # print(post_order_dft)
