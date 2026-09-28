"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program simulates an auto parts lookup system using
Python dictionaries to behave like a hash table. Each part
number acts as a unique key, and the part description acts
as the value.
----------------------------------------------------
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE (Auto Parts Inventory)
    # ===============================
    #
    # A Python dictionary behaves like a hash table because:
    # - Each key (part number) is hashed internally.
    # - The hash determines where the key-value pair is stored.
    # - Lookups, inserts, updates, and deletions are O(1) average time.
    #
    # Here we create an auto parts inventory using part numbers
    # as keys and part descriptions as values.

    print("\n=== INSERT OPERATIONS ===")

    auto_parts = {}  # empty hash table (inventory)

    # Insert at least 5 auto parts
    auto_parts["A123"] = "Alternator - Honda Civic 2010"
    auto_parts["B204"] = "Brake Pads - Ford F-150"
    auto_parts["C331"] = "Clutch Kit - Subaru WRX"
    auto_parts["F555"] = "Fuel Pump - Toyota Camry"
    auto_parts["S777"] = "Starter Motor - Chevy Silverado"

    print("Auto Parts Inventory After Inserts:")
    for part, desc in auto_parts.items():
        print(f"{part}: {desc}")

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    #
    # Lookup works by hashing the key and jumping directly
    # to the correct bucket. This makes finding parts fast.
    #
    # We will retrieve two existing part numbers.

    print("\n=== LOOKUP OPERATIONS ===")

    print("Looking up part A123:", auto_parts["A123"])
    print("Looking up part S777:", auto_parts["S777"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    #
    # Updating a key simply overwrites the value stored at
    # that key's hashed location. This simulates updating
    # part information in an inventory system.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", auto_parts["B204"])
    auto_parts["B204"] = "Brake Pads - Ford F-150 (Heavy Duty)"
    print("After update:", auto_parts["B204"])

    # ===============================
    # DELETE OPERATIONS
    # ===============================
    #
    # Deleting a key-value pair removes the part from the
    # inventory entirely. The bucket becomes available for
    # future inserts.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", auto_parts)
    del auto_parts["F555"]  # remove fuel pump
    print("After deleting F555:", auto_parts)

    # ===============================
    # EDGE CASES
    # ===============================
    #
    # Demonstrate:
    # - Lookup missing key
    # - Safe delete missing key
    # - Update missing key (creates new entry)
    # - Empty dictionary behavior

    print("\n=== EDGE CASES ===")

    # 1. Lookup missing part
    print("\nAttempting lookup of missing part 'X999':")
    if "X999" in auto_parts:
        print(auto_parts["X999"])
    else:
        print("Part X999 not found (KeyError avoided).")

    # 2. Safe delete missing part
    print("\nAttempting safe delete of missing part 'ZZZ':")
    removed = auto_parts.pop("ZZZ", None)
    print("Result of deleting ZZZ:", removed)

    # 3. Update missing key (creates new part)
    print("\nAdding new part 'T888' (missing key update):")
    auto_parts["T888"] = "Timing Belt - Nissan Altima"
    print("Updated Inventory:", auto_parts)

    # 4. Empty dictionary scenario
    print("\nTesting operations on an empty dictionary:")
    empty_inventory = {}
    print("Lookup in empty dictionary:", empty_inventory.get("A123"))


if __name__ == "__main__":
    main()

