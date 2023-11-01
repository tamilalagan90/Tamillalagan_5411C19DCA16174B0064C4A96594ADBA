'''Program to sort student details based on CGPA and display in descending order.'''
class Student:
  def __init__ (self, name, roll_number, cgpa):
    self.name= name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student:student.cgpa,reverse=True)
    return sorted_students

students=[
  Student("Aafrin", "22BCS01", 8.2),
  Student("Rebecca","22BCS33", 8.2),
  Student("Ashika", "22BCS04", 8.3),
  Student("Bavitra", "22BCS05", 8.2),
  Student("Shana", "22BCS03", 7.6),
  Student("Atifa", "22BCS02", 8.5),
  ]

sorted_students= sort_students(students)

for student in sorted_students:
    print("Name:{}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))