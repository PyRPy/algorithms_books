# 4_queue_hot_potato.py
from pythonds.basic import Queue 

def hotPotato(namelist, num):
    simqueue = Queue() 
    for name in namelist:
        simqueue.enqueue(name) 

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) 
        
        simqueue.dequeue() 

    return simqueue.dequeue() 

nameList = ["Bill", "david", "susan", "jane", "ken", "brad"]
num = 7
print(hotPotato(nameList, num))