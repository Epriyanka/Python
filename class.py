class student:
     name=""
     mark=0
     def __init__(self,name,mark):
      self.name=name
      self.mark=mark
      print("constructor called")
     def display(self):
         print("Student name is {0} \n student mark is {1}".format(self.name,self.mark))# self inherits the object name{0} and {1} are object array
         print("student name is:  ",self.name "\n Student mark is ",self.mark)
#obj=student()
#obj.name="abc"
#obj.mark=40
#obj.display()
#constructor
std=student('x',78)
std1=student('rekha',187)
std.display()
std1.display()
