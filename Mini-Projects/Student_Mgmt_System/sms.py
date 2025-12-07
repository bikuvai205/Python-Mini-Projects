import csv
import os

class Students:
  def __init__(self):
    self.student_list = []

  def load_file(self,filename="students.csv"):
    if not os.path.exists(filename):
      with open(filename,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","name","age","grade"])
      return
    
    with open(filename,newline="") as f:
      reader = csv.DictReader(f)
      self.student_list=[]
      for row in reader:
            student = {
                "id": int(row["id"]),
                "name": row["name"],
                "age": int(row["age"]),
                "grade": row["grade"]
            }
            self.student_list.append(student)

  def save_to_file(self, filename="students.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "grade"])
        writer.writeheader()
        for student in self.student_list:
            writer.writerow(student)


  def add_student(self,id,name,age,grade):
    
    student = {"id":id,"name":name,"age":age,"grade":grade}
    self.student_list.append(student)
    print("students added")
    self.save_to_file()
  
  def display_students(self):
    if self.student_list == []:
      print("Student not found...")
      return
    else:
      print("ID\tName\tAge\tGrade")
      for i in self.student_list:
        print(f"{i['id']}\t{i['name']}\t{i['age']}\t{i['grade']}")
    

  def update_student(self,id,new_name,new_age,new_grade):
    for items in self.student_list:
      if items["id"] == id:
        items.update({"name":new_name,"age":new_age,"grade":new_grade})
        print("Student updated:")
        self.save_to_file()
        return
      
    print("Student not found")

  def delete_student(self , id):
    for items in self.student_list:
      if items["id"] == id:
        self.student_list.remove(items)
        print("Student deleted")
        self.save_to_file()
        return
      
    print("Student not found")
      
       
sms = Students()


print('''-----------Welcome to Student Management System------------
-----> Choose the following option to perform the action
      1.Add student Record
      2.Edit the Current Record
      3.Delete the Record
      4.View the Record
      5.Exit
      ''')
while(True):
  choice  = int(input("Enter the option 1-5:\n"))

  if choice == 1:
    id = int(input("Enter the id:"))
    name = input("Enter the name:")
    age = int(input("Enter the age:"))
    grade = input("Enter the grade:")
    sms.add_student(id,name,age,grade)

  elif choice == 2:
   id = int(input("Enter the id to be edited:"))
   name = input("Enter the new name:")
   age = int(input("Enter the new age:"))
   grade = input("Enter the new grade:")
   sms.update_student(id,name,age,grade)

  elif choice == 3:
   id = int(input("Enter the id to be deleted:"))
   sms.delete_student(id)

  elif choice == 4:
    sms.display_students()

  elif choice == 5:
    print("Exiting...!")
    break
  
  else:
    print("Invalid option! Please enter 1-5")


  