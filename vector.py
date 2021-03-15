class vector:

    def __init__(self,a):
        """[THis is constructor of class ]

        Args:
            a ([List]): [Its the vector ]
        """        
        self.a = a

        

    def add(self,v2):
        """[THis function add the 2 vectors ]

        Args:
            v2 ([Vector]): [The vector to be added to v1]

        Returns:
            [list]: [It contains result of addition]
        """        
        n = len(self.a)
        m = len(v2.a)
        c = []
        if n != m:
            print("Incompatible Types")
            return

        for i in range(n):
            c.append(self.a[i]+v2.a[i])

        return c
    def sub(self,v2):
        """[THis function subtract the 2 vectors ]

        Args:
            v2 ([Vector]): [The vector to be subtracted to v1]

        Returns:
            [list]: [It contains result of subtraction]
        """ 
        n = len(self.a)
        m = len(v2.a)
        c = []
        if n != m:
            print("Incompatible Types")
            return

        for i in range(n):
            c.append(self.a[i]-v2.a[i])

        return c

    def mul(self,v2):
        """[THis function multiply the 2 vectors ]

        Args:
            v2 ([Vector]): [The vector to be multipled to v1]

        Returns:
            [list]: [It contains result of multiplication]
        """ 
        n = len(self.a)
        m = len(v2.a)
        c = []
        if n != m:
            print("Incompatible Types")
            return

        for i in range(n):
            c.append(self.a[i]*v2.a[i])

        return c




v1 = vector(eval(input("Enter the vector one in square brackets")))
v2 = vector(eval(input("Enter the vector two in square brackets")))  

print("Addition of vector:")
print(v1.add(v2))

print("Subtraction of vector:")
print(v1.sub(v2))

print("Multiplication(Hamarad Product wise) of vector:")
print(v1.mul(v2))








