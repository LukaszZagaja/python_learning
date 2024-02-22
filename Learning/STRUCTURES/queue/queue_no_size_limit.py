class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "Item has been added succesfully to the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in queue"
        else:
            return self.items.pop(0) # pop 0 deletes first element of the list
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
    
customQueue = Queue()
print(f"Queue is empty: {customQueue.isEmpty()}")
print(customQueue.enqueue(1))
customQueue.enqueue(2)
customQueue.enqueue(3)
print(f"\nQueue: {customQueue}")
customQueue.dequeue()
print(f'Queue after deleting: {customQueue}')
print(f"First element of queue is: {customQueue.peek()}")
