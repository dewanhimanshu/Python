class queue:
    def __init__(self,max_size=100):
        """[Constructor]

        Args:
            size (int): [Max size of queue]. Defaults to 100.
        """        
        self.lst = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        """[Adds element to the queue in FIFO order]

        Args:
            data ([Object]): [Object to be added]
        """        
        if self.size == self.max_size:
            print("Overflow")
        else:
            rear = (self.front + self.size)%self.max_size
            
            self.lst[rear] = data
            self.size = self.size + 1 
        

    def dequeue(self):
        """[Removes element from queue in FIFO order]

        Returns:
            [Object]: [Element thats is removed]
        """        
        if self.size == 0:
            print("Underflow error")
        else:
            val = self.lst[self.front]
            self.front = (self.front + 1)%self.max_size
            self.size = self.size - 1
            return val

    def get_size(self):
        """[Returns number of elements in array]

        Returns:
            [int]: [number of elements in array]
        """        
        return self.size

    def peek(self):
        """[Return the first elemnt in queue]

        Returns:
            [Object]: [first elemnt]
        """        
        if self.size == 0:
            print("Underflow error")
            
        else:
            return self.lst[self.front]
    
    def display(self):
        """[It displays the whole queue]
        """ 
        print(self.size)       
        for i in range(0,self.size):
            idx = (self.front+i)%self.max_size
            print(self.lst[idx],end=" ")
        print()

    def is_empty(self):
        return self.size==0
    def is_full(self):
        return self.size == self.max_size

s = eval(input("Enter the size of queue you want"))
q = queue(s)
while(True):

    print("Menu driven program")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch = input("ENter your choice:")
    if ch == '1':
        data = eval(input("ENter data:"))
        q.enqueue(data)
    elif ch == '2':
        print(q.dequeue())
    elif ch == '3':
        print(q.peek())
    elif ch == '4':
        q.display()
    else:
        break





