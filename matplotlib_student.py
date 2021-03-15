import matplotlib.pyplot as plt 
    # Assuming five subjects which are OOPS , CSA, DM , TC and  MTCS.
class Student:
    def __init__(self,name,marks): 
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks
    def display(self): 
        print("Name       : ", self.name) 
        print("Marks List : ", self.marks) 
        print()



def main():
    n=int(input("Enter total number of students : ")) 
    student_list=[]
    subjects=['OOPS' , 'CSA' , 'DM' , 'TC' ,'MTCS']
    for i in range(n): 
        print("\nEnter details of student ",i+1," : ") 
        name=input("\tEnter Student Name : ")
        marks=[] 
        for j in subjects : 
            print("\tEnter marks in subject ",j," : ",end='')
            marks.append(int(input())) 
        stu_obj = Student(name,marks) 
        student_list.append(stu_obj) 
        
   
    while True:
        print("***** Menu *****")
        print("1-Want individual student records in form of line graph.")
        print("2-Want individual student pie chart analysis.")
        print("3-Want analysis subject wise.")
        print("4.Exit")
        c=int(input("\nEnter your choice : "))
        
        if c==1:
            for i in student_list:
                j=1
                plt.subplot(n,1,j)
                j=j+1
                xpoints = subjects
                ypoints = i.getMarks()
                plt.plot(xpoints, ypoints)
                plt.show()
        # elif c==2:
        #     for i in stu_List:#looping on student list
        #         j=1
        #         plt.subplot(n,1,j)
        #         j=j+1
        #         xpoints = subjects
        #         ypoints = i.getMarks()
        #         plt.pie(ypoints,labels = xpoints)
        #         plt.show()
        # elif c==3:
        #     oops=[]#extracting marks of all students in oops            
        #     csa=[]#extracting marks of all students in csa
        #     dm=[]#extracting marks of all students in dm
        #     tc=[]#extracting marks of all students in tc
        #     mtcsa=[]#extracting marks of all students in mtcsa
        #     names=[]#extracting names of students
            
        #     for i in stu_List:#looping on list of students
        #         m=i.getMarks()#taking marks
        #         names.append(i.getName())#appending name in name list
        #         oops.append(m[0])#appending marks in oops
        #         csa.append(m[1])#appending marks in csa
        #         dm.append(m[2])#appending marks in dm
        #         tc.append(m[3])#appending marks in tc
        #         mtcsa.append(m[4])#appending marks in mtcsa
        #     #now plotting all the marks for individual student for each subject 
        #     x = names
        #     y = oops
        #     plt.bar(x,y)
        #     plt.xlabel("Students")#label for x axis
        #     plt.ylabel("marks in oops")#label for y axis
        #     plt.show()#for making plot visible
        #     x = names
        #     y = csa
        #     plt.bar(x,y)
        #     plt.xlabel("Students")
        #     plt.ylabel("marks in csa")
        #     plt.show()
        #     x = names
        #     y = dm
        #     plt.bar(x,y)
        #     plt.xlabel("Students")
        #     plt.ylabel("marks in dm")
        #     plt.show()
        #     x = names
        #     y = tc
        #     plt.bar(x,y)
        #     plt.xlabel("Students")
        #     plt.ylabel("marks in tc")
        #     plt.show()
        #     x = names
        #     y = mtcsa
        #     plt.bar(x,y)
        #     plt.xlabel("Students")
        #     plt.ylabel("marks in mtcsa")
        #     plt.show()
                
        else:
            break
            


# Calling main function
if __name__ == "__main__":
    main()


