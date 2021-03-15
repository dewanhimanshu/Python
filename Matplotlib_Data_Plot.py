'''
Question:

Programme for today’s lab classroom:

Given a list of data containing name of Students, marks in 5 subjects.

Ms. Goofy wants to analyse the data. 
Think and help Ms. Goofy

Note: You can view data from different perspectives. Attempt to give as many views as you can think.
'''

import matplotlib.pyplot as plt #Importing library module for plotting data.

# Defining class "Student" to hold student record with attribute student name and list of marks in 5 subjects. 
class Student:
    # Defining constructor of the class having parameters for all the attribute of the "Student" class.
    def __init__(self,name,marks_list): 
        self.setName(name) #Setting value of attribute "name" passed in constructor.
        self.setMarks(marks_list) #Setting value of attribute "marks_list" passed in constructor.
         
    def getName(self): #Getter function to return value of attribute "name".
        return self.name

    def getMarks(self): #Getter function to return value of attribute "marks_list".
        return self.marks
    
    def setName(self,name): #Setter function to set value of attribute "name".
        self.name=name
           
    def setMarks(self,marks): #Setter function to set value of attribute "marks_list".
        self.marks=marks
        
    def display(self): #Function to display details of object of class "Student".
            print("Name       : ", self.name) 
            print("Marks List : ", self.marks) 
            print("\n")


#Defining main function.
def main():
    
    # Assuming five subjects which are OOPS , CSA, DM , TC and  MTCS.
    
    n=int(input("Enter total number of students : ")) #Taking user input for total number of students.
    
    stu_List=[] #Defining an empty list that will store list of students records of class "Student" type.
    
    for i in range(n): #Loop for taking details of all student.
        print("\nEnter details of student ",i+1," :-- ") #Print message. 
        name=input("\tEnter Student Name : ") #Taking user input for Student Name.
        marks=[] #Defining an empty list to store marks of student in five subjects.
        subjects=('OOPS' , 'CSA' , 'DM' , 'TC' ,'MTCS') #Define a tuple of subjects marks will be taken input in this order only.
        for j in subjects : #Loop to enter marks in different subjects.
            print("\tEnter marks in subject ",j," : ",end='') #Print message.
            marks.append(int(input())) #Taking user input for marks in subject "j" and appending it to the list "marks".
        stu_obj = Student(name,marks) #Creating an object of class "Student".
        stu_List.append(stu_obj) #Appending created object of "Student" class to the list of students named "stu_List".
        
    ch='y'#choice variable for while loop
    while ch=='y' or ch=='Y':#begin while loop
        #printing menu options
        print("\n***** Menu *****")
        print("1-Want individual student records in form of line graph.")
        print("2-Want individual student pie chart analysis.")
        print("3-Want analysis subject wise.")
        c=int(input("\nEnter your choice : "))
        #exceuting according to choice entered by user
        if c==1:
            for i in stu_List:#looping on student list
                j=1#form printing subplots next to other
                plt.subplot(n,1,j)#for printing plots as subplots
                j=j+1
                xpoints = subjects#on x axis
                ypoints = i.getMarks()#on y axis
                plt.plot(xpoints, ypoints)#plotting
                plt.show()#for graph to get visible
        elif c==2:
            for i in stu_List:#looping on student list
                j=1
                plt.subplot(n,1,j)
                j=j+1
                xpoints = subjects
                ypoints = i.getMarks()
                plt.pie(ypoints,labels = xpoints)
                plt.show()
        elif c==3:
            oops=[]#extracting marks of all students in oops            
            csa=[]#extracting marks of all students in csa
            dm=[]#extracting marks of all students in dm
            tc=[]#extracting marks of all students in tc
            mtcsa=[]#extracting marks of all students in mtcsa
            names=[]#extracting names of students
            
            for i in stu_List:#looping on list of students
                m=i.getMarks()#taking marks
                names.append(i.getName())#appending name in name list
                oops.append(m[0])#appending marks in oops
                csa.append(m[1])#appending marks in csa
                dm.append(m[2])#appending marks in dm
                tc.append(m[3])#appending marks in tc
                mtcsa.append(m[4])#appending marks in mtcsa
            #now plotting all the marks for individual student for each subject 
            x = names
            y = oops
            plt.bar(x,y)
            plt.xlabel("Students")#label for x axis
            plt.ylabel("marks in oops")#label for y axis
            plt.show()#for making plot visible
            x = names
            y = csa
            plt.bar(x,y)
            plt.xlabel("Students")
            plt.ylabel("marks in csa")
            plt.show()
            x = names
            y = dm
            plt.bar(x,y)
            plt.xlabel("Students")
            plt.ylabel("marks in dm")
            plt.show()
            x = names
            y = tc
            plt.bar(x,y)
            plt.xlabel("Students")
            plt.ylabel("marks in tc")
            plt.show()
            x = names
            y = mtcsa
            plt.bar(x,y)
            plt.xlabel("Students")
            plt.ylabel("marks in mtcsa")
            plt.show()
                
        else:
            print("\nWrong choice Entered !!!")
        ch=input("\nDo u Want to continue? (Y/N) : ") #Input for while loop continuation till required.

# Calling main function
if __name__ == "__main__":
    main()


