import json
import pickle
import random


class Node:
    def __init__(self, key):
        self.p = None
        self.key = key
        self.left = None
        self.right = None



class BST:
    def __init__(self, param):
        self.root = None
        self.param = param

    def insert(self, v):
        z = Node(v)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key[self.param] < x.key[self.param]:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key[self.param] < y.key[self.param]:
            y.left = z
        else:
            y.right = z

    def delete(self, z):
        z, _ = self.search(z)
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.tree_successor(z)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.p = y.p

        if y.p is None:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        if y != z:
            z.key, y.key = y.key, z.key

        return y

    def tree_successor(self, x):
        if x.right is not None:
            return self.tree_minimum(x.right)

        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p

        return y

    def tree_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def search(self, k, path=''):
        if self.root is None:
            print('Root is None!')
            return
        return self._search_recursive(self.root, k, path)

    def _search_recursive(self, x, k, path):  # O(h)
        if k == x.key[self.param]:
            return x, path
        if k < x.key[self.param]:
            path += 'L'
            return self._search_recursive(x.left, k, path)
        else:
            path += 'R'
            return self._search_recursive(x.right, k, path)

    def print_tree(self):
        if self.root is None:
            print('Root is None!')
            return
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node, val="key", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(node, val=val, left=left, right=right)
        for line in lines:
            print(line)

    def save_tree(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.root, file)
        print("Tree saved successfully.")

    def load_tree(self, file_name):
        with open(file_name, 'rb') as file:
            self.root = pickle.load(file)


if __name__ == '__main__':

    bst = BST('PRICE')
    # data = [7, 6, 10, 3, 8, 12, 4, 9, 5]
    # for i in data:
    #     bst.insert(i)

    N = 10
    price = random.sample(range(N * 3), N)
    for i in range(N):
        robot = {"TYPE": random.choice(["AGV", "AFV", "ASV", "AUV"]), "PRICE": price[i],
                 "RANGE": random.randint(0, 100), "CAMERA": random.randint(0, 1)}
        bst.insert(robot)

    print('Original tree')
    bst.print_tree()
    print('')
    bst.save_tree('bst-robots.pickle')

    bst2 = BST('PRICE')
    bst2.load_tree('bst-robots.pickle')

    bst2.print_tree()

    # print(bst.search(10))
    # print(f'Case 1 delete 5 - no child')
    # bst.delete(5)
    # bst.print_tree()
    # print('')
    # bst.insert(5)
    #
    # print('Case 2 delete 3 - one child')
    # bst.delete(3)
    # bst.print_tree()
    # print('')
    #
    # print('Case 3 delete 7 - two child')
    # bst.delete(7)
    # bst.print_tree()

