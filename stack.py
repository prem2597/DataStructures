class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

# Test cases
def test_stack():
    s = Stack()
    assert s.is_empty() == True, "Stack should be empty initially"
    s.push(1)
    s.push(2)
    assert s.peek() == 2, "Peek should return 2"
    assert s.pop() == 2, "Pop should return 2"
    assert s.pop() == 1, "Pop should return 1"
    assert s.is_empty() == True, "Stack should be empty after pops"
    print("All test cases passed!")

def main():
    print(">>> test_stack()")
    test_stack()

if __name__ == "__main__":
    main()