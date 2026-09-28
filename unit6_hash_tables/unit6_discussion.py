"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program demonstrates how Python dictionaries behave
like hash tables by showing insert, lookup, update, delete,
and edge-case operations.
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE (Dictionary)
    # ===============================
    #
    # In Python, a dictionary *is* a hash table.
    # Keys are hashed internally, and the hash determines
    # where the key-value pair is stored in memory.
    #
    # Creating a dictionary simulates creating a hash table.

    print("\n=== INSERT OPERATIONS ===")

    hash_table = {}  # empty hash table

    # Insert key-value pairs
    hash_table["NH"] = 24
    hash_table["VT"] = 46
    hash_table["WI"] = 31
    hash_table["CA"] = 12
    hash_table["TX"] = 99

    print("Hash table after inserts:")
    print(hash_table)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    #
    # Lookup in a dictionary is O(1) average time.
    # Python hashes the key, jumps directly to the bucket,
    # and retrieves the value.

    print("\n=== LOOKUP OPERATIONS ===")

    print("Lookup NH:", hash_table["NH"])
    print("Lookup WI:", hash_table["WI"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    #
    # Updating a key simply overwrites the value stored
    # at that key's hash location.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", hash_table)
    hash_table["CA"] = 100  # update existing key
    print("After update (CA changed to 100):", hash_table)

    # ===============================
    # DELETE OPERATIONS
    # ===============================
    #
    # Deleting removes the key-value pair entirely.
    # The hash table frees that bucket for future use.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", hash_table)
    del hash_table["TX"]
    print("After deleting TX:", hash_table)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # 1. Lookup a missing key
    print("\nEdge Case 1: Lookup missing key 'FL'")
    try:
        print(hash_table["FL"])
    except KeyError:
        print("KeyError: 'FL' does not exist in the hash table.")

    # 2. Delete a missing key safely
    print("\nEdge Case 2: Safe deletion of missing key 'AZ'")
    removed_value = hash_table.pop("AZ", None)
    print("Result of deleting AZ:", removed_value)
    print("Dictionary unchanged:", hash_table)

    # 3. Update a missing key (creates a new entry)
    print("\nEdge Case 3: Updating missing key 'NY'")
    hash_table["NY"] = 55
    print("After adding NY:", hash_table)

    # 4. Using an empty dictionary
    print("\nEdge Case 4: Operations on an empty dictionary")
    empty_dict = {}
    print("Empty dictionary:", empty_dict)
    print("Trying to lookup a key in empty dictionary:")
    print("empty_dict.get('anything') returns:", empty_dict.get("anything"))


if __name__ == "__main__":
    main()
