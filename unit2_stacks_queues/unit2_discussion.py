"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

THEME:
  Stack  -> Building (and eating) a loaded taco, one topping
            at a time. You can only ever deal with the topping
            currently on TOP -- classic LIFO.
  Queue  -> A theme park ride line. First person in line gets
            on the ride first. No cutting. Classic FIFO.

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).
"""

from collections import deque


class Stack:
    """A taco, built one topping at a time. Eat from the top down."""

    def __init__(self):
        # A Python list is the taco itself. We only ever touch the
        # LAST element (index -1) -- the top layer -- because that's
        # the only topping physically accessible without a mess.
        self._items = []

    def push(self, value):
        # append() adds a new topping to the TOP of the taco.
        # Whatever goes on last is the first thing your fork hits --
        # that's LIFO (Last In, First Out) in action.
        self._items.append(value)

    def pop(self):
        # Eat (remove) the topmost layer of the taco and return it.
        # If there's no taco, you can't take a bite -- raise a clear
        # error instead of crashing mysteriously.
        if self.is_empty():
            raise IndexError("pop() called on an empty taco (stack)")
        return self._items.pop()

    def peek(self):
        # Look at what topping is currently on top without eating it.
        if self.is_empty():
            raise IndexError("peek() called on an empty taco (stack)")
        return self._items[-1]

    def is_empty(self):
        # No toppings left = no taco = empty stack.
        return len(self._items) == 0


class Queue:
    """A theme park ride line. First in line, first on the ride."""

    def __init__(self):
        # deque lets us add people to the BACK of the line and remove
        # them from the FRONT, both in O(1) time. A plain list would
        # make removing the front person O(n) -- everyone else would
        # have to shuffle forward one spot, which is exactly what
        # actual lines do NOT need code to simulate.
        self._items = deque()

    def enqueue(self, value):
        # A new guest joins the BACK of the line. No cutting allowed --
        # this enforces FIFO (First In, First Out).
        self._items.append(value)

    def dequeue(self):
        # The person at the FRONT of the line boards the ride and
        # leaves the queue. If the line is empty, there's no one to
        # board -- raise a clear error instead of a confusing crash.
        if self.is_empty():
            raise IndexError("dequeue() called on an empty line (queue)")
        return self._items.popleft()

    def front(self):
        # See who's next in line without pulling them out of it.
        if self.is_empty():
            raise IndexError("front() called on an empty line (queue)")
        return self._items[0]

    def is_empty(self):
        # Nobody in line = empty queue.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO: Building a Taco
    # ===============================
    print("\n=== STACK DEMO: Building a Taco ===")
    taco = Stack()

    print("Layering toppings onto the taco, in this order:")
    toppings = ["seasoned beef", "lettuce", "cheese", "salsa"]
    for topping in toppings:
        print(f"  adding -> {topping}")
        taco.push(topping)

    print(f"\nTop layer right now (peek): {taco.peek()}  <- first bite!")

    print("\nEating the taco one layer at a time.")
    print("Notice it comes off in REVERSE order of how it was built")
    print("(salsa, cheese, lettuce, beef) -- that's LIFO:")
    while not taco.is_empty():
        print(f"  ate -> {taco.pop()}")

    print("\nTaco's gone. Trying to take one more bite anyway...")
    try:
        taco.pop()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    print("Trying to peek at a taco that doesn't exist...")
    try:
        taco.peek()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    print("\nMaking a minimalist one-topping taco (just cheese)...")
    single_taco = Stack()
    single_taco.push("cheese")
    print(f"  is_empty() before eating: {single_taco.is_empty()}")
    single_taco.pop()
    print(f"  is_empty() after eating:  {single_taco.is_empty()}")

    # ===============================
    # QUEUE DEMO: The Roller Coaster Line
    # ===============================
    print("\n=== QUEUE DEMO: The Roller Coaster Line ===")
    ride_line = Queue()

    print("Guests joining the ride line, in this order:")
    guests = ["Alice", "Bo", "Chen", "Dana"]
    for guest in guests:
        print(f"  joins line -> {guest}")
        ride_line.enqueue(guest)

    print(f"\nWho's up next (front): {ride_line.front()}")

    print("\nBoarding guests one at a time.")
    print("They board in the SAME order they lined up")
    print("(Alice, Bo, Chen, Dana) -- that's FIFO, no cutting:")
    while not ride_line.is_empty():
        print(f"  boards ride -> {ride_line.dequeue()}")

    print("\nLine's empty. Trying to board one more guest anyway...")
    try:
        ride_line.dequeue()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    print("Checking who's front-of-line when nobody's there...")
    try:
        ride_line.front()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    print("\nA single guest (Eli) shows up alone and rides solo...")
    solo_line = Queue()
    solo_line.enqueue("Eli")
    print(f"  is_empty() before boarding: {solo_line.is_empty()}")
    solo_line.dequeue()
    print(f"  is_empty() after boarding:  {solo_line.is_empty()}")


if __name__ == "__main__":
    main()