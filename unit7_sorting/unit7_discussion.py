"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

The goal is to demonstrate understanding of algorithm behavior,
efficiency, and implementation details.
"""


def bubble_sort(lst):
    """
    Bubble Sort repeatedly compares adjacent values and swaps them
    when they are out of order. With each pass, the largest remaining
    value "bubbles up" toward the end of the list.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    """

    # Create a copy so the original list is not modified
    result = lst.copy()

    # Bubble Sort uses repeated passes through the list
    # On each pass, adjacent values are compared
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(result) - 1):

            # Compare adjacent values
            if result[i] > result[i + 1]:

                # Swap values when they are out of order
                temp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = temp

                swapped = True

    return result


def merge_sort(lst):
    """
    Merge Sort uses recursion and divide-and-conquer:
    - Split the list into halves
    - Recursively sort each half
    - Merge the sorted halves together

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    """

    # Base case: A list of length 0 or 1 is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge step for Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    """

    result = []
    i = j = 0

    # Compare values from both lists and build sorted output
    while i < len(left) and j < len(right):

        # Compare current values from each list
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining values from the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append any remaining values from the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")

    dataset1 = [42, 7, 19, 88, 31, 55, 12]
    print("Original list:", dataset1)

    bubble_sorted1 = bubble_sort(dataset1)
    merge_sorted1 = merge_sort(dataset1)

    print("Bubble Sort result:", bubble_sorted1)
    print("Merge Sort result:", merge_sorted1)

    # ===============================
    # DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")

    dataset2 = [99, 3, 3, 72, 14, 0, 56, 56]
    print("Original list:", dataset2)

    bubble_sorted2 = bubble_sort(dataset2)
    merge_sorted2 = merge_sort(dataset2)

    print("Bubble Sort result:", bubble_sorted2)
    print("Merge Sort result:", merge_sorted2)

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Empty list
    empty = []
    print("Empty list Bubble Sort:", bubble_sort(empty))
    print("Empty list Merge Sort:", merge_sort(empty))
    print("Explanation: Both algorithms return an empty list because there is nothing to sort.")

    # Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready sorted list Bubble Sort:", bubble_sort(sorted_list))
    print("Already sorted list Merge Sort:", merge_sort(sorted_list))
    print("Explanation: Bubble Sort finishes quickly because no swaps occur. Merge Sort still divides and merges.")

    # Reverse-sorted list
    reverse_list = [9, 7, 5, 3, 1]
    print("\nReverse-sorted list Bubble Sort:", bubble_sort(reverse_list))
    print("Reverse-sorted list Merge Sort:", merge_sort(reverse_list))
    print("Explanation: Bubble Sort performs many swaps; Merge Sort handles it efficiently due to divide-and-conquer.")

    # Duplicate values
    duplicates = [4, 4, 2, 2, 9, 9]
    print("\nDuplicate values Bubble Sort:", bubble_sort(duplicates))
    print("Duplicate values Merge Sort:", merge_sort(duplicates))
    print("Explanation: Both algorithms correctly maintain duplicates while sorting.")


if __name__ == "__main__":
    main()
