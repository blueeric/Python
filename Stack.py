class Stack():
    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.head=-1

    def isEmpty(self):
        if self.head==-1:
            return True
        else:
            return False

    def isFull(self):
        if self.head+1==self.size:
            return True
        else:
            return False

    def enStack(self,con):
        if self.isFull():
            print("Stack is full")
        else:
            self.stack.append(con)
            self.head=self.head+1

    def outStack(self,con):
        if self.isEmpty():
            print("Stack is empty");
        else:
            self.stack.remove(con)
            #self.stack.pop()  #delete the last one
            self.head=self.head-1;