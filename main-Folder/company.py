class company:
    def __init__(self, name , age , department , Attendance_status ,  Present_or_No , salary ): 
        self.name = name
        self.age = age
        self.department = department
        self. Attendance_status =  Attendance_status
        self.Present_or_No =  Present_or_No
        self.salary = salary
        
    # def He_is_Present_or_No(self):
    #     if self.Present_or_No == True:
    #         print("He is Present....")
    #     else:
    #         print('He is No Absent....')
            
    # def is_good (self):
    #     if self.rating >=9.5:
    #       return True
    #     else:
    #      return   False
    def bonus (self):
        if self.age  >= 40:
            self.salary +=500
            print ("Salary increased To : " + str(self.salary))
        else:
            print ("No Bonus Added , Salary Is Still " + str(self.salary))           
                    
# 1 - الإسم           
# 2 - العمر
# 3 - القسم
# 4 - حاله حضوره
# 5 - حاضر ام لا