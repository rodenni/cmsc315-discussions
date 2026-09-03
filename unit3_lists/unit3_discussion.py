"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # list.insert() shifts every element from `index` onward one position
    # to the right to make room for the new value. Under the hood, Python
    # lists are backed by a contiguous array, so this shift is a real
    # memory operation, not just a logical relabeling.
    lst.insert(index, value)

    # Performance depends on WHERE the insertion happens:
    # - Inserting at the END (index == len(lst)) is O(1) on average,
    #   since no existing elements need to move (barring occasional
    #   internal array resizing).
    # - Inserting at the BEGINNING or MIDDLE is O(n) in the worst case,
    #   because every element after the insertion point must shift
    #   right by one position.
    return lst


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    """
    # Validate the index BEFORE attempting the removal. Without this
    # check, an out-of-range index would raise an IndexError and crash
    # the program. Validating first lets us fail gracefully instead.
    if index < 0 or index >= len(lst):
        return None

    # list.pop(index) removes the element and returns it in one step.
    # Like insertion, deletion from the middle or beginning requires
    # shifting all subsequent elements left by one position to close
    # the gap (O(n)); deleting the last element is O(1) since nothing
    # needs to shift.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    Search for a value within the list.
    """
    # This is a LINEAR search: we check each element one at a time,
    # starting from index 0, until we either find a match or reach
    # the end of the list. Python lists are not sorted or indexed by
    # value, so there's no way to "jump" to where a value might be —
    # every element must be examined in the worst case, making this
    # an O(n) operation.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    numbers = [10, 20, 30, 40, 50]
    print(f"Original list: {numbers}")

    # Insert at the beginning (index 0) -- forces every existing
    # element to shift right by one (O(n)).
    insert_at(numbers, 0, 5)
    print(f"After inserting 5 at the beginning: {numbers}")

    # Insert in the middle -- still requires shifting all elements
    # after the insertion point (O(n)).
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 25)
    print(f"After inserting 25 in the middle (index {middle_index}): {numbers}")

    # Insert at the end -- no shifting required, so this is the
    # cheapest insertion (O(1) on average).
    insert_at(numbers, len(numbers), 60)
    print(f"After inserting 60 at the end: {numbers}")

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # Delete from the beginning -- every remaining element shifts
    # left by one to fill the gap (O(n)).
    removed = delete_at(numbers, 0)
    print(f"Removed value at index 0: {removed} -> List is now: {numbers}")

    # Delete from the middle -- also requires shifting (O(n)).
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print(f"Removed value at index {middle_index}: {removed} -> List is now: {numbers}")

    # Delete from the end -- no shifting needed, so this is the
    # cheapest deletion (O(1)).
    last_index = len(numbers) - 1
    removed = delete_at(numbers, last_index)
    print(f"Removed value at index {last_index}: {removed} -> List is now: {numbers}")

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists in the list.
    target = numbers[len(numbers) // 2]
    index_found = search_value(numbers, target)
    print(f"Searching for {target} (exists): found at index {index_found}")

    # Search for a value that does NOT exist in the list.
    missing_value = 9999
    index_found = search_value(numbers, missing_value)
    print(f"Searching for {missing_value} (does not exist): result = {index_found}")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: Delete using an invalid index.
    # This tests that delete_at() safely returns None instead of
    # crashing the program with an IndexError.
    invalid_index = 100
    result = delete_at(numbers, invalid_index)
    print(f"Attempting to delete at invalid index {invalid_index}: result = {result} "
          f"(list unchanged: {numbers})")

    # Edge case 2: Insert into an empty list.
    # This tests that insertion works correctly even when there are
    # no existing elements to shift.
    empty_list = []
    insert_at(empty_list, 0, 100)
    print(f"Inserting 100 into an empty list: {empty_list}")

    # Bonus edge case: Search for a value in an empty list.
    # There's nothing to scan, so the loop in search_value() never
    # executes and -1 is returned immediately.
    search_result = search_value([], 42)
    print(f"Searching for 42 in an empty list: result = {search_result}")


if __name__ == "__main__":
    main()