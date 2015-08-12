class Queue():
    def __init__(self,size):
        self.queue=[]
        self.size=size;
        self.head=-1
        self.tail=-1

    def isFull(self):
        if self.head-self.tail+1==self.size:
            print("Queue is Full")
            return True
        else:
            return False

    def isEmpty(self):
        if self.head==self.tail:
            return True
        else:
            print("Queue is Empty")

    def enQueue(self,cont):
        if self.isFull():
            print("Queue is Full")
        else:
            self.queue.append(cont)
            self.tail=self.tail+1

    def outQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            del self.queue[self.head]
            self.head= self.head+1