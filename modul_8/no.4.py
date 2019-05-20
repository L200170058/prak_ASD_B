#no.4

class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]

class PriorityQueue(object):
    def __init__(self):
        self.qlist=[]
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self,data,priority):
        entry= _PriorityQEntry(data,priority)
        self.qlist.append(entry)
    def dequeue(self):
        try: 
            max = 0
            for i in range(len(self.qlist)): 
                if self.qlist[i] > self.qlist[max]: 
                    max = i 
            item = self.qlist[max] 
            del self.qlist[max] 
            return item 
        except IndexError: 
            print() 
            exit() 
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]
    
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item=data
        self.priority=priority

Q=Queue()
Q.enqueue(4)
Q.enqueue(6)
Q.enqueue(8)
Q.getFrontMost()

S=PriorityQueue()
S.enqueue("jeruk",4)
S.enqueue("Tomat",2)
S.enqueue("Mangga",0)
S.enqueue("Duku",5)
S.enqueue("Pepaya",2)

