"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

This program demonstrates two fundamental search algorithms:
linear search and binary search. It also compares their behavior
on small and large datasets and explores important edge cases.
"""


def linear_search(lst, target):
    """
    Linear Search:
    - Checks each element one-by-one from left to right.
    - If the target is found, return its index.
    - If the loop finishes without finding it, return -1.

    Why O(n)?
    - In the worst case, linear search must inspect EVERY element.
    - As the list grows, the number of comparisons grows linearly.
    - Therefore, time complexity is O(n).
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Binary Search:
    - Assumes the list is already sorted.
    - Repeatedly checks the middle element.
    - If the middle is too small, search the right half.
    - If the middle is too large, search the left half.
    - Each iteration cuts the search space in HALF.

    Why O(log n)?
    - Because halving the search space repeatedly means the number
      of steps grows very slowly compared to the list size.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Target must be in the right half
            left = mid + 1
        else:
            # Target must be in the left half
            right = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    print("\n=== SMALL DATASET TEST ===")

    small = [3, 8, 12, 20, 25, 30]
    print("Small dataset:", small)

    # Value that exists
    target1 = 20
    print(f"\nSearching for existing value {target1}:")
    print("Linear Search Index:", linear_search(small, target1))
    print("Binary Search Index:", binary_search(small, target1))
    # Explanation:
    # Both algorithms find the value quickly because the list is small.

    # Value that does not exist
    target2 = 99
    print(f"\nSearching for NON-existing value {target2}:")
    print("Linear Search Index:", linear_search(small, target2))
    print("Binary Search Index:", binary_search(small, target2))
    # Explanation:
    # Linear search checks all elements.
    # Binary search quickly eliminates halves until nothing remains.

    # ===============================
    # LARGE DATASET
    # ===============================
    print("\n=== LARGE DATASET TEST ===")

    large = list(range(0, 1000000))  # 1 million sorted numbers
    print("Large dataset created (1,000,000 elements).")

    target3 = 987654
    print(f"\nSearching for value {target3} in large dataset:")

    print("Linear Search Index:", linear_search(large, target3))
    print("Binary Search Index:", binary_search(large, target3))

    # Explanation:
    # Linear search would require checking ~987,654 elements.
    # Binary search finds the value in about log2(1,000,000) ≈ 20 steps.
    # This demonstrates why binary search is dramatically faster
    # as datasets grow.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Empty list
    empty = []
    print("\nEdge Case: Empty List")
    print("Linear:", linear_search(empty, 10))
    print("Binary:", binary_search(empty, 10))
    # Explanation:
    # Both return -1 because there are no elements to inspect.

    # Single-element list
    single = [42]
    print("\nEdge Case: Single-element List")
    print("Linear:", linear_search(single, 42))
    print("Binary:", binary_search(single, 42))
    # Explanation:
    # Both find the value immediately because it is the only element.

    # Value at first position
    print("\nEdge Case: Value at FIRST position")
    print("Linear:", linear_search(small, small[0]))
    print("Binary:", binary_search(small, small[0]))

    # Value at last position
    print("\nEdge Case: Value at LAST position")
    print("Linear:", linear_search(small, small[-1]))
    print("Binary:", binary_search(small, small[-1]))


if __name__ == "__main__":
    main()
