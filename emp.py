class employee:
    def __init__(self,name,empid,designation,experience):
        """[THis is the constructor method]

        Args:
            name ([String]): [It will contane the name of employee ]
            empid ([int]): [Employee ID]
            designation ([String]): [Worker/ Supervisor/Manager]
            experience ([int]): [Number of years of experience]
        """
        self.name = name
        self.empid = empid
        self.designation = designation
        self.experience = experience
        self.salary = self.cal_sal()

    def cal_sal(self):
        BaseSalary = 0
        if self.designation.lower() == "worker":
            BaseSalary = 10000
        elif self.designation.lower() ==   "supervisor":
            BaseSalary = 15000
        else:
            BaseSalary = 20000
        AddSal = (self.experience / 100 ) *  BaseSalary
        HRA = 0.05 * BaseSalary
        return BaseSalary + AddSal + HRA

    #Getter and setter for attribute name
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    #Getter and setter for attribute empid
    def set_empid(self,empid):
        self.empid = empid
    def get_empid(self):
        return self.empid
    #Getter and setter for attribute designation
    def set_designation(self,designation):
        self.designation = designation
        self.salary = self.cal_sal() 
    def get_designation(self):
        return self.designation
    #Getter and setter for attribute Salary (Warning: This will override the salary calculated by formula ) 
    def set_salary(self,salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
    #Getter and setter for attribute Experience
    def set_experience(self,experience):
        self.experience = experience
    def get_experience(self):
        return self.experience
    
    def __str__(self):
        print("Printing Employee atributes ")
        self.show()
        return ""

    def show(self):
        '''
            THis object prints all the attributes of the employee 
        '''
        print("Name is:",self.name)
        print("Employee ID is:",self.empid)
        print("Designation is:",self.designation)
        print("Salary is:",self.salary)
        print("Experience is:",self.experience)

    
emp1 = employee("Himanshu",24,"Manager",1)
print(emp1)