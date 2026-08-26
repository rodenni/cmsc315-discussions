"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # A Python list works great as the backing store for a stack.
        # We only ever touch the END of the list (index -1), and
        # list.append()/list.pop() on the end are both O(1) operations.
        self._items = []

    def push(self, value):
        # append() adds to the END of the list, which we treat as the
        # "top" of the stack. Because pop() also removes from the end,
        # the LAST value pushed is always the FIRST one popped — that's
        # exactly the LIFO (Last In, First Out) behavior a stack needs.
        self._items.append(value)

    def pop(self):
        # Removes and returns the top (most recently added) value.
        # Edge case: popping an empty stack should NOT crash with an
        # unhandled IndexError — we raise a clear, descriptive error
        # instead so the caller understands exactly what went wrong.
        if self.is_empty():
            raise IndexError("pop() called on an empty stack")
        return self._items.pop()

    def peek(self):
        # Returns the top value WITHOUT removing it — useful when you
        # need to check what's next without committing to removing it.
        if self.is_empty():
            raise IndexError("peek() called on an empty stack")
        return self._items[-1]

    def is_empty(self):
        # A stack is empty when its underlying list has no elements.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # deque (double-ended queue) is optimized for adding/removing
        # from BOTH ends in O(1) time. A plain list would force us to
        # use pop(0) to remove from the front, which is O(n) because
        # every remaining element has to shift left. deque avoids that.
        self._items = deque()

    def enqueue(self, value):
        # append() adds to the RIGHT (back) of the deque. Combined with
        # popleft() removing from the LEFT (front), the value that's
        # been waiting longest is always the first one out — FIFO
        # (First In, First Out) behavior.
        self._items.append(value)

    def dequeue(self):
        # Removes and returns the value at the front of the queue.
        # Edge case: like the stack, dequeuing an empty queue raises
        # a clear error instead of letting a confusing exception bubble up.
        if self.is_empty():
            raise IndexError("dequeue() called on an empty queue")
        return self._items.popleft()

    def front(self):
        # Returns the front value WITHOUT removing it.
        if self.is_empty():
            raise IndexError("front() called on an empty queue")
        return self._items[0]

    def is_empty(self):
        # A queue is empty when its underlying deque has no elements.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    stack = Stack()

    # 1 & 2: create stack, push 4 values
    print("Pushing 1, 2, 3, 4 onto the stack...")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(f"Current top of stack (peek): {stack.peek()}")

    # 3 & 4: demonstrate LIFO by popping everything off
    print("\nPopping all values off — should come out in REVERSE order")
    print("(4, 3, 2, 1) because a stack is Last In, First Out:")
    while not stack.is_empty():
        print(f"  popped -> {stack.pop()}")

    # 5: pop on an empty stack
    print("\nStack is now empty. Attempting to pop again...")
    try:
        stack.pop()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    # 6: peek on an empty stack
    print("Attempting to peek at an empty stack...")
    try:
        stack.peek()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    # 7: single-item stack, remove it, verify empty
    print("\nCreating a stack with a single item (99), then removing it...")
    single_stack = Stack()
    single_stack.push(99)
    print(f"  is_empty() before pop: {single_stack.is_empty()}")
    single_stack.pop()
    print(f"  is_empty() after pop:  {single_stack.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    # 1 & 2: create queue, enqueue 4 values
    print("Enqueuing 'A', 'B', 'C', 'D' into the queue...")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    print(f"Current front of queue: {queue.front()}")

    # 3 & 4: demonstrate FIFO by dequeuing everything
    print("\nDequeuing all values — should come out in the SAME order")
    print("(A, B, C, D) because a queue is First In, First Out:")
    while not queue.is_empty():
        print(f"  dequeued -> {queue.dequeue()}")

    # 5: dequeue on an empty queue
    print("\nQueue is now empty. Attempting to dequeue again...")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    # 6: front on an empty queue
    print("Attempting to view front of an empty queue...")
    try:
        queue.front()
    except IndexError as e:
        print(f"  Caught expected error: {e}")

    # 7: single-item queue, remove it, verify empty
    print("\nCreating a queue with a single item ('Z'), then removing it...")
    single_queue = Queue()
    single_queue.enqueue("Z")
    print(f"  is_empty() before dequeue: {single_queue.is_empty()}")
    single_queue.dequeue()
    print(f"  is_empty() after dequeue:  {single_queue.is_empty()}")


if __name__ == "__main__":
    main()