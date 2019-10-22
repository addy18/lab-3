# FOR RED BLACK TREE CLASS
BLACK = "BLACK"
RED = "RED"
# FOR COUNT_ANAGRAMS METHOD
count = 0


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.color = RED


class AvlTree:
    def __init__(self):
        self.root = None

    def avl_insert(self, node1):
        node = Node(node1)
        if self.root is None:
            self.root = node
            node.parent = None
            return
        curr = self.root
        while curr is not None:
            if node.key < curr.key:
                if curr.left is None:
                    curr.left = node
                    node.parent = curr
                    curr = None
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    node.parent = curr
                    curr = None
                else:
                    curr = curr.right
        node = node.parent
        while node is not None:
            self.avl_rebalance(node)
            node = node.parent

    def avl_rebalance(self, node):
        self.avl_height(node)
        if self.avl_get_balance(node) is -2:
            if self.avl_get_balance(node.right) is 1:
                self.avl_rotate_right(node.right)
            return self.avl_rotate_left(node)
        elif self.avl_get_balance(node) is 2:
            if self.avl_get_balance(node.left) is -1:
                self.avl_rotate_left(node.left)
            return self.avl_rotate_right(node)
        return node

    def avl_rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.avl_replace(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.avl_set(node.left, "right", node)
        self.avl_set(node, "left", left_right_child)

    def avl_rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.avl_replace(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.avl_set(node.right, "left", node)
        self.avl_set(node, "right", right_left_child)

    def avl_set(self, parent, which_child, child):
        if which_child is not "left" and which_child is not "right":
            return False
        if which_child is "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        self.avl_height(parent)
        return True

    def avl_replace(self, parent, curr_child, new_child):
        if parent.left is curr_child:
            return self.avl_set(parent, "left", new_child)
        elif parent.right is curr_child:
            return self.avl_set(parent, "right", new_child)
        return False

    def avl_get_balance(self, node):
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        return left_height - right_height

    def avl_height(self, node):
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        node.height = max(left_height, right_height) + 1

    def avl_search(self, data):
        curr = self.root
        while curr is not None:
            if data > curr.key:
                curr = curr.right
            elif data < curr.key:
                curr = curr.left
            else:
                return True
        return False

    def avl_print(self, node):
        if node is None:
            return
        self.avl_print(node.left)
        print(node.key)
        self.avl_print(node.right)
        return


class RedBlackTree:
    def __init__(self):
        self.root = None

    def rb_insert(self, node1):
        node = Node(node1)
        self.bst_insert(node)
        node.color = RED
        self.rb_tree_balance(node)
        return

    def bst_insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            curr = self.root
            while curr is not None:
                if node.key < curr.key:
                    if curr.left is None:
                        curr.left = node
                        node.parent = curr
                        curr = None
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        node.parent = curr
                        curr = None
                    else:
                        curr = curr.right
        return

    def rb_get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def rb_get_uncle(self, node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def rb_tree_balance(self, node):
        if node.parent is None:
            node.color = BLACK
            return
        if node.parent.color == BLACK:
            return
        parent = node.parent
        grandparent = self.rb_get_grandparent(node)
        uncle = self.rb_get_uncle(node)
        if uncle is not None and uncle.color == RED:
            parent.color = uncle.color = BLACK
            grandparent.color = RED
            self.rb_tree_balance(grandparent)
            return
        if node == parent.right and parent == grandparent.left:
            self.rb_rotate_left(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandparent.right:
            self.rb_rotate_right(parent)
            node = parent
            parent = node.parent
        parent.color = BLACK
        grandparent.color = RED
        if node == parent.left:
            self.rb_rotate_right(grandparent)
        else:
            self.rb_rotate_left(grandparent)

    def rb_rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.rb_replace(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.rb_set(node.right, "left", node)
        self.rb_set(node, "right", right_left_child)

    def rb_rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.rb_replace(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.rb_set(node.left, "right", node)
        self.rb_set(node, "left", left_right_child)

    def rb_replace(self, parent, curr_child, new_child):
        if parent.left is curr_child:
            return self.rb_set(parent, "left", new_child)
        elif parent.right is curr_child:
            return self.rb_set(parent, "right", new_child)
        return False

    def rb_set(self, parent, which_child, child):
        if which_child is not "left" and which_child is not "right":
            return False
        if which_child is "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True

    def rb_search(self, data):
        curr = self.root
        while curr is not None:
            if data > curr.key:
                curr = curr.right
            elif data < curr.key:
                curr = curr.left
            else:
                return True
        return False

    def rb_print(self, node):
        if node is None:
            return
        print(node.key, node.color)
        self.rb_print(node.left)
        # print(node.key, node.color)
        self.rb_print(node.right)
        return

# READS FILES AND PUTS THEM IN APPROPRIATE CLASSES
def avl_readfile():
    file = open("word.txt", "r")
    avl = AvlTree()
    for x in file.readlines():
        avl.avl_insert(x.replace("\n", ""))
    return avl


def rb_readfile():
    file = open("word.txt", "r")
    rb = RedBlackTree()
    for x in file.readlines():
        rb.rb_insert(x.replace("\n", ""))
    return rb

# PRINTS ANAGRAMMA OF ENGLISH WORDS ONLY
def print_anagrams_avl(word, english_words, prefix=""):
    if len(word) <= 1:
        st = prefix + word
        if english_words.avl_search(st):
            print(st)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]     # letters before cur
            after = word[i + 1:]    # letters after cur

            if cur not in before:   # Check if permutations of cur have not been generated
                print_anagrams_avl(before + after, english_words, prefix + cur)


def print_anagrams_rbt(word, english_words, prefix=""):
    if len(word) <= 1:
        st = prefix + word
        if english_words.rb_search(st):
            print(st)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]     # letters before cur
            after = word[i + 1:]    # letters after cur

            if cur not in before:   # Check if permutations of cur have not been generated
                print_anagrams_rbt(before + after, english_words, prefix + cur)

# COUNTING NUMBER OF ANAGRAMS FROM A SPECIFIC WORDS
def rb_count_anagrams(word, english_words, prefix=""):
    global count
    # count = 0
    if len(word) <= 1:
        st = prefix + word
        if english_words.rb_search(st):
            count = count + 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated
                rb_count_anagrams(before + after, english_words, prefix + cur)
    return count


def avl_count_anagrams(word, english_words, prefix=""):
    global count
    # count = 0
    if len(word) <= 1:
        st = prefix + word
        if english_words.avl_search(st):
            count = count + 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated
                avl_count_anagrams(before + after, english_words, prefix + cur)
    return count

# GATHERS THE WORD WITH THE MOST ANAGRAMS
def avl_powerful_word(english_words):
    global count
    file = open("word.txt", "r")
    big = 0
    word = ""
    count = 0
    for line in file.readlines():
        a = str(line.replace("\n", ""))
        q = avl_count_anagrams(a, english_words)
        if q > big:
            word = a
            big = q
        # global count
        count = 0
    print("most powerful word ever: ", word, " with ", big, " anagrams")
    return 0


def rb_powerful_word(english_words):
    global count
    file = open("word.txt", "r")
    big = 0
    word = ""
    count = 0
    for line in file.readlines():
        a = str(line.replace("\n", ""))
        q = rb_count_anagrams(a, english_words)
        if q > big:
            word = a
            big = q
        # global count
        count = 0
    print("most powerful word ever: ", word, " with ", big, " anagrams")
    return 0


def main():
    print("select an option: ")
    choice = int(input("1. AVL Tree \n2. Red-Black Tree\n"))

    if choice is 1:
        print("what word do you want to use")
        word = input()
        english_words = avl_readfile()
        #PRINTS THE TREE FULLY
        # print("AVL")
        # print("------------------")
        # english_words.avl_print(english_words.root)
        print("\nanagrams for ", word, ": ")
        print("------------------")
        print_anagrams_avl(word, english_words)
        print("\n-------------\n", word, " has this many anagrams: ", avl_count_anagrams(word, english_words))
        avl_powerful_word(english_words)

    elif choice is 2:
        print("what word do you want to use")
        word = input()
        english_words = rb_readfile()
        # print("RED-BLACK")
        # print("------------------")
        # english_words.rb_print(english_words.root)
        print("\nanagrams for ", word, ": ")
        print("------------------")
        print_anagrams_rbt(word, english_words)
        print("\n----------------\n", word, " has this many anagrams: ", rb_count_anagrams(word, english_words))
        rb_powerful_word(english_words)

    else:
        print("invalid input")


if __name__ == "__main__":

    main()
