from lst11.task3 import EX1_BST

class EX2_BST(EX1_BST):
    def __init__(self):
        super().__init__()

    def left_rotate(self, x):
        x, _ = self.search(x)
        y = x.right

        # Step 1
        x.right = y.left

        if y.left is not None:
            y.left.p = x

        # Step 2
        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        # Step 3
        y.left = x
        x.p = y

    def right_rotate(self, x):
        x, _ = self.search(x)
        y = x.left

        x.left = y.right
        if y.right is not None:
            y.right.p = x

        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y


        y.right = x
        x.p = y


if __name__ == '__main__':

    bst = EX2_BST()
    data = [20, 10, 3, 15, 25, 22, 30, 27, 26, 28, 37, 31, 40]
    for i in data:
        bst.insert(i)
    bst.print_tree()
    print()
    bst.left_rotate(25)

    bst.print_tree()
    print()
    bst.right_rotate(30)
    bst.right_rotate(20)
    bst.print_tree()
    # bst = EX2_BST()
    # data = [20, 9, 9, 4, 4, 7, 5, 14, 11, 12]
    # for i in data:
    #     bst.insert(i)
    # bst.print_tree()