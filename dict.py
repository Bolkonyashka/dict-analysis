from additionalClasses import TreeElement, BalancedTreeElement, BinaryTree, BalancedTree
from queue import Queue


class BFDict:
    def __init__(self):
        self.data = []

    def add(self, *keys):
        for i in keys:
            self.data.append((i[0], i[1]))

    def get(self, key):
        for i in range(0, len(self.data)):
            if self.data[i][0] == key:
                return self.data[i][1]
        return None

    def items(self):
        return self.data

    def keys(self):
        res = []
        for i in self.data:
            res.append(i[0])
        return res

    def values(self):
        res = []
        for i in self.data:
            res.append(i[1])
        return res

    def pop(self, key):
        for i in range(0, len(self.data)):
            if self.data[i][0] == key:
                res = self.data[i][1]
                self.data.pop(i)
                return res
        return None


class BSDict:
    def __init__(self):
        self.data = []

    def add(self, *keys):
        for i in keys:
            self.data.append((i[0], i[1]))

    def get(self, key):
        self.data.sort()
        lft = 0
        rgt = len(self.data) - 1
        while lft < rgt:
            mdl = int((lft + rgt) / 2)
            if key <= self.data[mdl][0]:
                rgt = mdl
            else:
                lft = mdl + 1
        if self.data[rgt][0] == key:
            return self.data[rgt][1]
        return None

    def items(self):
        return self.data

    def keys(self):
        res = []
        for i in self.data:
            res.append(i[0])
        return res

    def values(self):
        res = []
        for i in self.data:
            res.append(i[1])
        return res

    def pop(self, key):
        self.data.sort()
        lft = 0
        rgt = len(self.data) - 1
        while lft < rgt:
            mdl = int((lft + rgt) / 2)
            if key <= self.data[mdl][0]:
                rgt = mdl
            else:
                lft = mdl + 1
        if self.data[rgt][0] == key:
            res = self.data[rgt][1]
            self.data.pop(rgt)
            return res
        return None


class BTDict:
    def __init__(self):
        self.size = 0
        self.tree = BinaryTree()

    def add(self, *keys):
        for i in keys:
            if self.size == 0:
                self.tree.peek = TreeElement(i)
            else:
                self.tree.add(self.tree.peek, i)
            self.size += 1

    def get(self, key):
        if self.size == 0:
            return None
        return self.tree.find(key)

    def items(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append((a.key, a.value))
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def keys(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append(a.key)
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def values(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append(a.value)
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def pop(self, key):
        if self.size == 0:
            return None
        self.size -= 1
        self.tree.pop_value = None
        res = self.tree.delete(self.tree.peek, key).value
        return self.tree.pop_value


class BBTDict:
    def __init__(self):
        self.size = 0
        self.tree = BalancedTree()

    def add(self, *keys):
        for i in keys:
            if self.size == 0:
                self.tree.peek = BalancedTreeElement(i)
            else:
                self.tree.add(self.tree.peek, i)
            self.size += 1

    def get(self, key):
        return self.tree.find(key)

    def items(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append((a.key, a.value))
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def keys(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append(a.key)
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def values(self):
        q = Queue()
        q.put(self.tree.peek)
        res = []
        while not q.empty():
            a = q.get()
            res.append(a.value)
            if a.right != 0:
                q.put(a.right)
            if a.left != 0:
                q.put(a.left)
        return res

    def pop(self, key):
        if self.size == 0:
            return None
        self.size -= 1
        self.tree.pop_value = None
        res = self.tree.delete(self.tree.peek, key).value
        return self.tree.pop_value


class HDict:
    def __init__(self):
        self.hash_table = []
        for i in range(0, 8):
            self.hash_table.append([])
        self.table_size = 8
        self.size = 0

    def table_extension(self):
        self.table_size *= 2
        new_table = []
        for i in range(0, self.table_size):
            new_table.append([])
        for j in self.hash_table:
            if len(j) != 0:
                for k in j:
                    item_ind = k[0] & (self.table_size - 1)
                    new_table[item_ind].append((k[0], k[1], k[2]))
        self.hash_table = new_table

    def add(self, *keys):
        for i in keys:
            if self.size > (2 / 3) * self.table_size:
                self.table_extension()
            key_hash = hash(i[0])
            item_ind = key_hash & (self.table_size - 1)
            self.hash_table[item_ind].append((key_hash, i[0], i[1]))
            self.size += 1

    def get(self, key):
        if self.size == 0:
            return None
        key_hash = hash(key)
        item_ind = key_hash & (self.table_size - 1)
        res = self.hash_table[item_ind]
        if len(res) == 0:
            return None
        for i in res:
            if i[0] == key_hash and i[1] == key:
                return i[2]
        return None

    def items(self):
        if self.size == 0:
            return None
        res = []
        for j in self.hash_table:
            if len(j) != 0:
                for k in j:
                    res.append((k[1], k[2]))
        return res

    def keys(self):
        if self.size == 0:
            return None
        res = []
        for j in self.hash_table:
            if len(j) != 0:
                for k in j:
                    res.append(k[1])
        return res

    def values(self):
        if self.size == 0:
            return None
        res = []
        for j in self.hash_table:
            if len(j) != 0:
                for k in j:
                    res.append(k[2])
        return res

    def pop(self, key):
        if self.size == 0:
            return None
        key_hash = hash(key)
        item_ind = key_hash & (self.table_size - 1)
        res = self.hash_table[item_ind]
        if len(res) == 0:
            return None
        counter = 0
        for i in res:
            if i[0] == key_hash and i[1] == key:
                res_val = i[2]
                res.pop(counter)
                self.size -= 1
                return res_val
            counter += 1
        return None

'''
dct = BSDict()
dct.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8), ("fhjkrh", 9), ("yjyj", 10))
print(dct.get("yjyj"))
print("------------------------")

dct2 = BFDict()
dct2.add(("Roma", 1), ("Fofo", 2), ("ffdf", 3), ("fdfsfg", 5), ("fhgrfhrh", 6), ("gjhjrh", 7), ("hlkh", 8), ("fhjkrh", 9), ("yjyj", 10))
print(dct2.get("yjyj"))
print(dct.pop("hlkh"))
print(dct2.pop("hlkh"))
print("------------------------")

dct3 = BTDict()
dct3.add((8, 8), (3, 3), (1, 1), (6, 6), (4, 4), (7, 7), (10, 10), (14, 14), (13, 13))
print(dct3.get(7))
print(dct3.pop(10))
print(dct3.tree.peek.right.right.value)
res = dct3.items()
print(res[0])
print("------------------------")

dct4 = BBTDict()
dct4.add((8, 8), (3, 3), (1, 1), (6, 6), (4, 4), (7, 7), (10, 10), (14, 14), (13, 13))
print(dct4.tree.peek.value)
print(dct4.pop(6))
print(dct4.pop(7))
print(dct4.tree.peek.value)
print(dct4.items())
print("------------------------")

dct5 = HDict()
dct5.add(("ковер", 8), ("пол", 3), ("шкаф", 1), ("диван", 6), ("кровать", 4), ("стол", 7), ("стул", 10), ("Сковородка", 11), ("раковина", 12))
print(dct5.get("пол"))
print(0)
print(dct5.pop("Сковородка"))
print(0)'''
