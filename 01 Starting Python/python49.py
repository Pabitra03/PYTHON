class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove an item from the top of the stack.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Get the number of items in the stack.
        """
        return len(self.stack)

    def peek(self):
        """
        Get the item at the top of the stack without removing it.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


# Example usage
stack = Stack()

# Push items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Print the size of the stack
print("Stack size:", stack.size())

# Peek at the top item
print("Top item:", stack.peek())

# Pop items off the stack
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())