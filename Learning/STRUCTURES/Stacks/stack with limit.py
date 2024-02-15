class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull():
            #print('The stack if full.')
            return 'The stack if full.'
        else: 
            self.list.append(value)
            return 'The element has been added'
    
    def pop(self):
        if self.isEmpty():
            return 'There is not any element in the Stack'
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None # None is neither True nor False

customStack = Stack(4)
print(f'Is empty: {customStack.isEmpty()}')
print(f'Is full: {customStack.isFull()}')
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5) # this wont be added because it excels max size
customStack.push(10) # this wont be added because it excels max size
print(customStack)

