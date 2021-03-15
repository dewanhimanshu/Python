class student:
    def __init__(self,name,rollno):
        """[THis the constructor ]

        Args:
            name ([String]): [NAme of student]
            rollno ([String]): [Roll Number of student ]
        """        
        self.name = name
        self.rollno = rollno

    def __str__(self):
        """[Overiding the str method]

        Returns:
            [string]
        """        
        print("Name is:",self.name)
        print("Roll no:",self.rollno)
        return ""

    


class stack:

    def __init__(self,max_size = 100):
        """[This is the constructor]
        """        
        self.st = []
        self.top = -1
        self.max_size = max_size 

    def push(self,element):
        """[This function pushes the elmenet on the stack]

        Args:
            element ([type]): [description]
        """        
        if self.top == self.max_size:
            print("Stack is full now")
            return

        self.top = self.top + 1
        self.st.insert(self.top,element)
        

    def pop(self):
        """[THis function pops/removes the element from stack]

        Returns:
            [element]: [Element that is popped out or none is stack in empty]
        """        
        if(self.top == -1):
            print("Stack is Empty")
            return 
        
        element = self.st.pop()
        self.top = self.top - 1
        return element
    
    def peek(self):
        """[This element returns the element at top of stack]

        Returns:
            [element]
        """        
        if self.top == -1:
            return
        
        return self.st[self.top]

    def get_size(self):
        """[THis function returns the size of stack]

        Returns:
            [int]: [Number of elments in stack]
        """        
        return self.top + 1
    
    def is_full(self):
        return self.top == self.max_size
    
    def is_empty(self):
        return self.top == -1



# st = stack()

# while(True):
#     print("Menu Driven Program")
#     print("1.Create new student and push it in stack")
#     print("2.Remove one student from stack")
#     print("3.Break")
#     ch = eval(input("Enter the input:"))

#     if ch == 1:
#         name = input("Name of student:")
#         rollno = input("Roll no of student:")
#         s = student(name,rollno)
#         if st.is_full() == False :
#             st.push(s)
#             print(st.peek())
#         else:
#             print("STack is full")
    
#     elif ch == 2:
#         if st.is_empty():
#             print("Stack is empty")
#         print(st.peek())
#         st.pop()

#     else:
#         print("Thank you .. Quiting the program")
#         break





