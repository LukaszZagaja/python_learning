class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)
      
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been inserted"
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            return self.list[len(self.list)-1] # this deletes last element in the stack
        
    def delete(self):
        self.list = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(f'Popped element is: {customStack.pop()}')
print(customStack)
print(f'Last element of Stack is: {customStack.peek()}')
