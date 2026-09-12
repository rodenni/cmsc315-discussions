"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # A node just needs to remember its own value and point to
        # its left and right children. Both children start empty
        # (None) since a brand-new node has no children yet.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty tree simply has no root node yet.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        This is the public-facing method. It delegates the real work
        to the recursive helper, then reassigns self.root to whatever
        that helper returns. That reassignment matters even when the
        tree already has a root: each level of the recursion returns
        the (possibly-updated) subtree it was given, so the chain of
        return values is what actually reconnects the new node into
        the tree.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursive BST insertion.

        Base case: we've walked off the tree (node is None), which
        means we found the correct empty spot -- create a new node
        here and return it so the caller above can attach it.

        Recursive case: compare value against the current node.
        - Smaller -> it belongs somewhere in the left subtree, so
          recurse left and reattach whatever comes back.
        - Larger  -> same idea, but for the right subtree.
        - Equal   -> treat as a duplicate and ignore it, since a
          classic BST doesn't need duplicate values to stay valid.
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # else: value == node.value, duplicate -- do nothing

        return node

    def search(self, value):
        """
        Search for a value in the BST.

        BST search beats plain linear search because the ordering
        property lets us discard an entire subtree at every step
        instead of checking every element one by one. On a roughly
        balanced tree with n values, that gives O(log n) average-case
        search time instead of O(n).
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # Base case 1: fell off the tree without finding it.
        if node is None:
            return False

        # Base case 2: found it.
        if value == node.value:
            return True

        # Recursive case: only look in the half of the tree that
        # could possibly contain the value.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an in-order
        traversal (left, node, right).
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        In-order traversal: visit left subtree, then the current
        node, then the right subtree.

        Because every node's left subtree holds only smaller values
        and its right subtree holds only larger values, visiting in
        this left-node-right order naturally produces values in
        ascending sorted order -- no extra sorting step needed.
        """
        if node is None:
            return

        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    # Each insert compares the new value against the tree built so
    # far and immediately narrows down to one branch, so the tree
    # never has to "look at" the values on the other side.
    print("\n=== TREE CONSTRUCTION ===")
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    tree = BST()
    for v in values_to_insert:
        tree.insert(v)
    print(f"Inserted values: {values_to_insert}")
    # 50 is the root. 30 and 20/40 land in the left subtree because
    # they're all smaller than 50. 70 and 60/80 land in the right
    # subtree because they're all larger than 50 -- each insert only
    # ever compares against the nodes on its own path down the tree.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    result = tree.inorder()
    print(f"In-order traversal: {result}")
    # The output comes out sorted (20, 30, 40, 50, 60, 70, 80) purely
    # as a side effect of the BST's left-smaller/right-larger
    # property combined with the left-node-right visiting order.

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    for v in [40, 80]:
        print(f"Search {v}: {tree.search(v)}  (expected True, value exists)")
    for v in [15, 100]:
        print(f"Search {v}: {tree.search(v)}  (expected False, value not inserted)")
    # 40 and 80 are both in values_to_insert, so search walks straight
    # down the correct branch and finds them. 15 and 100 are outside
    # the range of anything inserted, so search runs off the edge of
    # the tree (hits None) and correctly reports False.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    empty_tree = BST()
    print(f"Search on empty tree: {empty_tree.search(10)}  (expected False)")
    print(f"In-order traversal of empty tree: {empty_tree.inorder()}  (expected [])")
    # An empty tree has root = None, so _search_recursive and
    # _inorder_recursive both hit their None base case immediately
    # without crashing -- they just report "not found" / "no values".

    single_node_tree = BST()
    single_node_tree.insert(99)
    print(f"Single-node tree in-order: {single_node_tree.inorder()}  (expected [99])")
    # With only a root and no children, both recursive calls into
    # left and right immediately return without adding anything, so
    # the traversal correctly reports just the one value.

    duplicate_tree = BST()
    duplicate_tree.insert(25)
    duplicate_tree.insert(25)
    print(f"Tree after inserting 25 twice: {duplicate_tree.inorder()}  (expected [25])")
    # _insert_recursive treats value == node.value as a duplicate and
    # does nothing, so the second insert of 25 has no effect on the
    # tree's structure or contents.


if __name__ == "__main__":
    main()