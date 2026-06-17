# this is where we move on oop in python

# class employee:
#     def __init__(self , name, work, salary, payout,):
#         self.name = name
#         self.name = work
#         self.work = salary      
#         self.payout = payout
    


class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_stu):
        self.name = name
        self.max_stu = max_stu
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_stu:
            self.students.append(student)
            return True
        return False
    def get_avarage_grade(self):
        pass
