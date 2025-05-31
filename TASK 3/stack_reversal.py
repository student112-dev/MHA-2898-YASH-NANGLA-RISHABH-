class Stack:
    def __init__(self):
        self.stack_items = []

    def is_empty(self):
        return len(self.stack_items) == 0

    def push(self, item):
        self.stack_items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack_items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack_items[-1]
        return None

    def size(self):
        return len(self.stack_items)
    

# Reversing a String Using Stack
def reverse_string(input_str):
    s = Stack()
    for char in input_str:
        s.push(char)
    
    reversed_str = ""
    while not s.is_empty():
        reversed_str += s.pop()
    return reversed_str

# Test
original = "YashNangla"
reversed_result = reverse_string(original)
print("Original String:", original)
print("Reversed String:", reversed_result)
