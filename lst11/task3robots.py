from lst11.task2robots import Node, BST

class EX1_BST(BST):
    def __init__(self , param):
        super().__init__(param)

    def print_tree(self, target_node=None):
        if self.root is None:
            print('Root is None!')
            return
        self._print_tree_recursive(self.root, target_node=target_node)

    def inorder(self):

        print("Inorder Traversal:")
        traversal_list = []
        self._inorder_recursive(self.root, traversal_list)
        print("Inorder List:", traversal_list)
        print()

    def _inorder_recursive(self, node, traversal_list):
        """Odwiedzenie węzła następuje pomiędzy (in) odwiedzaniem poddrzew"""

        if node is not None:
            self._inorder_recursive(node.left, traversal_list)
            traversal_list.append(node.key)
            self.print_tree(node)
            self._inorder_recursive(node.right, traversal_list)

            print()


    def preorder(self):
        print("Preorder Traversal:")
        traversal_list = []
        self._preorder_recursive(self.root, traversal_list)
        print("Preorder List:", traversal_list)
        print()

    def _preorder_recursive(self, node, traversal_list):
        """Odwiedzenie wierzchołka następuję przed (pre) odwiedzeniem poddrzew"""
        if node is not None:

            self.print_tree(node)
            traversal_list.append(node.key)
            self._preorder_recursive(node.left, traversal_list)
            self._preorder_recursive(node.right, traversal_list)

            print()

    def postorder(self):
        print("Postorder Traversal:")
        traversal_list = []
        self._postorder_recursive(self.root, traversal_list)
        print("Postorder List:", traversal_list)
        print()

    def _postorder_recursive(self, node, traversal_list):
        """Odwiedzenie węzła następuje po (post) odwiedzeniu poddrzew"""
        if node is not None:
            self._postorder_recursive(node.left, traversal_list)
            self._postorder_recursive(node.right, traversal_list)
            self.print_tree(node)
            traversal_list.append(node.key)

            print()


    def _print_tree_recursive(self, node, val="key", left="left", right="right", target_node=None):
        def display(root, val=val, left=left, right=right, target_node=target_node):
            """Returns a list of strings, width, height, and the horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s%s' % (('* ' if root == target_node else ''), getattr(root, val))
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only the left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s%s' % (('* ' if root == target_node else ''), getattr(root, val))
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only the right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s%s' % (('* ' if root == target_node else ''), getattr(root, val))
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s%s' % (('* ' if root == target_node else ''), getattr(root, val))
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


if __name__ == '__main__':

    bst = EX1_BST('PRICE')
    bst.load_tree('bst-robots.pickle')
    bst.inorder()
    bst.preorder()
    bst.postorder()