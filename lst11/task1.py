import json


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None



    def insert(self, data, path=None):
        if path is None:
            if self.root is not None:
                print("Error: Root node already exists.")
                return
            self.root = Node(data)
            return

        if self.root is None:
            print("Error: No path available. Tree is empty.")
            return

        current = self.root
        for i, direction in enumerate(path):
            if direction == 'L':
                if current.left is None and i == len(path) - 1:
                    current.left = Node(data)
                    return
                elif current.left is None:
                    print(f"Error: No path available {path}. Left child does not exist.")
                    return
                current = current.left
            elif direction == 'P':
                if current.right is None and i == len(path) - 1:
                    current.right = Node(data)
                    return
                elif current.right is None:
                    print(f"Error: No path available: {path}. Right child does not exist.")
                    return
                current = current.right

        print(f"Error: Place {path} is already taken.")
        return


    def remove(self, path=None):
        if path is None:
            if self.root is None:
                print("Error: The tree is empty.")
            else:
                self.root = None
                print("Root node removed successfully.")
        elif len(path) == 0:
            print("Error: Invalid path length.")
        else:
            node = self.root
            parent = None

            for direction in path:
                if direction == "L":
                    if node.left is None:
                        print(f"Error: No path available {path}. Left child does not exist.")
                        return
                    parent = node
                    node = node.left
                elif direction == "P":
                    if node.right is None:
                        print(f"Error: No path available {path}. Right child does not exist.")
                        return
                    parent = node
                    node = node.right
                else:
                    print("Error: Invalid path.")
                    return

            if parent is not None:
                if node is parent.left:
                    parent.left = None
                else:
                    parent.right = None
                print(f"Node '{node.key}' removed successfully.")
            else:
                print("Error: Invalid path.")

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

        lines, *_ = display(node, val, left, right)
        for line in lines:
            print(line)
    def save_tree(self, filename):
        data = self.serialize_tree()
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Tree saved successfully.")

    def load_tree(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self.deserialize_tree(data)

    def serialize_tree(self):
        if self.root is None:
            return None
        queue = [self.root]
        serialized_data = []
        while queue:
            node = queue.pop(0)
            serialized_node = {'key': node.key, 'left': None, 'right': None}
            if node.left:
                serialized_node['left'] = node.left.key
                queue.append(node.left)
            if node.right:
                serialized_node['right'] = node.right.key
                queue.append(node.right)
            serialized_data.append(serialized_node)
        return serialized_data

    def deserialize_tree(self, data):
        if data is None:
            self.root = None
            return
        node_map = {}
        for item in data:
            node = Node(item['key'])
            node_map[item['key']] = node
        for item in data:
            node = node_map[item['key']]
            if item['left']:
                node.left = node_map[item['left']]
            if item['right']:
                node.right = node_map[item['right']]
        self.root = node_map[data[0]['key']]

    def inorder(self):

        traversal_list = []
        self._inorder_recursive(self.root, traversal_list)
        print("Inorder List:", traversal_list)
        print()

    def _inorder_recursive(self, node, traversal_list):
        """Odwiedzenie węzła następuje pomiędzy (in) odwiedzaniem poddrzew"""

        if node is not None:
            self._inorder_recursive(node.left, traversal_list)
            traversal_list.append(node.key)
            # self.print_tree(node)
            self._inorder_recursive(node.right, traversal_list)

            print()
    def preorder(self):
        traversal_list = []
        self._preorder_recursive(self.root, traversal_list)
        print("Preorder List:", traversal_list)
        print()

    def _preorder_recursive(self, node, traversal_list):
        """Odwiedzenie wierzchołka następuję przed (pre) odwiedzeniem poddrzew"""
        if node is not None:

            traversal_list.append(node.key)
            self._preorder_recursive(node.left, traversal_list)
            self._preorder_recursive(node.right, traversal_list)

            print()

    def postorder(self):
        traversal_list = []
        self._postorder_recursive(self.root, traversal_list)
        print("Postorder List:", traversal_list)
        print()

    def _postorder_recursive(self, node, traversal_list):
        """Odwiedzenie węzła następuje po (post) odwiedzeniu poddrzew"""
        if node is not None:
            self._postorder_recursive(node.left, traversal_list)
            self._postorder_recursive(node.right, traversal_list)
            traversal_list.append(node.key)

            print()
# tree = BinaryTree()
# tree.insert(15)
# tree.insert(25, "P")
# tree.insert(40, "PP")
# tree.insert(30, "PPL")
# tree.insert(35, "PPLP")
# tree.insert(31, "PPLPL")
# tree.insert(36, "PPLPP")
# tree.insert(22, "PPLL")
# tree.insert(27, "PPLLP")
# tree.insert(26, "PPLLPL")
# tree.insert(17, "PL")
# tree.insert(18, "PLP")
# tree.insert(16, "PLL")
# tree.insert(1, "L")
# tree.insert(2, "LL")
# tree.insert(3, "LLP")
# tree.insert(4, "LLPL")
# tree.insert(5, "LLPLL")
# tree.insert(6, "LLPP")


# tree.print_tree()
# tree.remove("PPL")
# tree.remove()
# tree.remove("L")
# print()
# tree.print_tree()
# tree.save_tree("tree.json")
# print()
# tree2 = BinaryTree()
# tree2.load_tree("tree.json")
# tree2.print_tree()
# tree2.remove('PP')
# tree2.print_tree()



tree = BinaryTree()
tree.insert(20)
tree.insert(14, "P")
tree.insert(12, "PP")
tree.insert(11, "PL")
tree.insert(9, "L")
tree.insert(9, "LL")
tree.insert(4, "LLP")
tree.insert(4, "LLL")
tree.insert(7, "LP")
tree.insert(5, "LPL")

tree.print_tree()
tree.inorder()
tree.preorder()
tree.postorder()