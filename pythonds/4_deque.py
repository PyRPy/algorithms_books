# 4_deque.py
class Deque:
    def __init__(self):
        self.items = [] 

    def isEmpty(self):
        return self.items == [] 

    def addFront(self, item):
        self.items.append(item) 
    
    def addRear(self, item):
        self.items.insert(0, item) 

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0) 

    def size(self):
        return len(self.items) 

d = Deque() 
print(d.isEmpty()) 
print('add 4 from rear')
d.addRear(4) 
print('add dog from rear')
d.addRear('dog')

print(d.items)

print('add cat from front')
d.addFront('cat')
d.addFront(True)

print(d.items)
print('remove from rear')
print(d.removeRear())
print('remove from front')
print(d.removeFront())
print('what\'s left')
print(d.items)




    