class TreeElement:
    def __init__(self, key_and_value):
        self.key = key_and_value[0]
        self.value = key_and_value[1]
        self.left = 0
        self.right = 0


class BinaryTree:
    def __init__(self):
        self.peek = 0
        self.pop_value = None

    def add(self, root, key_and_value):
        while True:
            if key_and_value[0] < root.key:
                if root.left != 0:
                    root = root.left
                else:
                    root.left = TreeElement(key_and_value)
                    break
            else:
                if root.right != 0:
                    root = root.right
                else:
                    root.right = TreeElement(key_and_value)
                    break

    def find(self, key):
        cur_elem = self.peek
        while True:
            if cur_elem.key == key:
                return cur_elem.value
            else:
                if cur_elem.key < key:
                    if cur_elem.right == 0:
                        return None
                    cur_elem = cur_elem.right
                else:
                    if cur_elem.left == 0:
                        return None
                    cur_elem = cur_elem.left

    def delete(self, root, key):
        if root == 0:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            self.pop_value = root.value
            left_tree = root.left
            right_tree = root.right
            if right_tree == 0:
                return left_tree
            min = self.find_min(right_tree)
            min.right = self.remove_min(right_tree)
            min.left = left_tree
            return min
        return root

    def find_min(self, root):
        if root.left == 0:
            return root
        else:
            return self.find_min(root.left)

    def remove_min(self, root):
        if root.left == 0:
            return root.right
        root.left = self.remove_min(root.left)
        return root


class BalancedTreeElement:
    def __init__(self, key_and_value):
        self.key = key_and_value[0]
        self.value = key_and_value[1]
        self.left = 0
        self.right = 0
        self.height = 1


class BalancedTree:
    def __init__(self):
        self.peek = 0
        self.pop_value = None

    def add(self, root, key_and_value):
        if root == 0:
            return BalancedTreeElement(key_and_value)
        else:
            if key_and_value[0] < root.key:
                root.left = self.add(root.left, key_and_value)
            else:
                root.right = self.add(root.right, key_and_value)
        return self.balance(root)

    def balance(self, root):
        self.fix_height(root)
        if self.balance_value(root) == 2:
            if self.balance_value(root.right) < 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        if self.balance_value(root) == -2:
            if self.balance_value(root.left) > 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        return root

    def balance_value(self, root):
        return self.height(root.right) - self.height(root.left)

    def rotate_right(self, root):
        left_tree = root.left
        root.left = left_tree.right
        left_tree.right = root
        self.fix_height(root)
        self.fix_height(left_tree)
        if root.key == self.peek.key:
            self.peek = left_tree
        return left_tree

    def rotate_left(self, root):
        right_tree = root.right
        root.right = right_tree.left
        right_tree.left = root
        self.fix_height(root)
        self.fix_height(right_tree)
        if root.key == self.peek.key:
            self.peek = right_tree
        return right_tree

    def fix_height(self, root):
        h1 = self.height(root.left)
        h2 = self.height(root.right)
        root.height = max(h1, h2) + 1

    def height(self, root):
        if root == 0:
            return 0
        return root.height

    def find(self, key):
        cur_elem = self.peek
        while True:
            if cur_elem.key == key:
                return cur_elem.value
            else:
                if cur_elem.key < key:
                    if cur_elem.right == 0:
                        return None
                    cur_elem = cur_elem.right
                else:
                    if cur_elem.left == 0:
                        return None
                    cur_elem = cur_elem.left

    def delete(self, root, key):
        if root == 0:
            return 0
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            self.pop_value = root.value
            left_tree = root.left
            right_tree = root.right
            if right_tree == 0:
                return left_tree
            min = self.find_min(right_tree)
            min.right = self.remove_min(right_tree)
            min.left = left_tree
            if root.key == self.peek.key:
                self.peek = min
            return self.balance(min)
        return self.balance(root)

    def find_min(self, root):
        if root.left == 0:
            return root
        else:
            return self.find_min(root.left)

    def remove_min(self, root):
        if root.left == 0:
            return root.right
        root.left = self.remove_min(root.left)
        return self.balance(root)

