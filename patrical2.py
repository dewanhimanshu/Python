class complex_number:
    __counter = 0
    def __init__(self,real,imag):
        #COnstructor of the class
        self.real = real
        self.imag = imag
        complex_number.__counter = complex_number.__counter + 1

    @classmethod
    def get_counter(cls):
        # Return the counter attributer of class
        return cls.__counter

    @property
    def real(self):
        #Getter for real attributer
        return self.__real

    @real.setter
    def real(self,value):
        #Setter of real attribute
        self.__real = value

    @property
    def imag(self):
        #Getter for imag attributer
        return self.__imag

    @imag.setter
    def imag(self,value):
        #Setter for imag attributer
        self.__imag = value

    
    def __add__(self,other):
        """[Addition of complex number]

        Args:
            other ([complex_number]): 

        Returns:
            [complex_number]
        """        
        real = self.real + other.real
        imag = self.imag + other.imag
        ans = complex_number(real,imag)
        return ans

    def __mul__(self,other):
        """[multiplication of 2 complex number]

        Args:
            other ([complex_number])

        Returns:
            [complex_number]: [returns product ]
        """        
        a_real = self.real
        a_img = self.imag
        b_real = other.real
        b_img = other.imag
        ans = complex_number(a_real * b_real - a_img * b_img,a_real * b_img + a_img * b_real)
        return ans

    def __str__(self):
        #Override the __str__ method
        return "{}+j*{}".format(self.real,self.imag)



n1_real = int(input("input real part of 1st number "))
n1_img = int(input("input imag part of 1st number "))
n1 = complex_number(n1_real,n1_img)

n2_real = int(input("input real part of 2nd number "))
n2_img = int(input("input imag part of 2nd number "))
n2 = complex_number(n2_real,n2_img)


while True:
    print("1.Multiplication")
    print("2.Addition")
    print("3.Value of counter")
    print("Any other input will end the program")
    ch = input("Enter choice")

    if ch == '1':
        n4 = n1 * n2
        print("Miltiplication is:")
        print(n4)

    elif ch == '2':
        n3 = n1 + n2
        print("add is:")
        print(n3)

    elif ch == '3':
        print("Value of counter is:")
        print(complex_number.get_counter())

    else:
        print("wrong choice so ending the program")
        break








    
        