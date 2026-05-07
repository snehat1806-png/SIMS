import json
import re
from student import Student

FILE_NAME = "students.json"


class StudentManager:

    def load_data(self):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []

    def save_data(self, data):
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def get_next_id(self, students):
        if not students:
            return 101
        return max(student["id"] for student in students) + 1
    def validate_email(self, email):
      pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
      return re.fullmatch(pattern, email) is not None
    
    def list_students(self):
       students = self.load_data()

       if not students:
          print("No students found.")
          return

       print("\n===== STUDENT LIST =====")

       for student in students:
         print(
            f'ID: {student["id"]} | '
            f'Name: {student["name"]} | '
            f'Department: {student["dept"]}'
        )
    def search_student(self):
      students = self.load_data()

      keyword = input("Enter student name to search: ").lower()

      found = False

      for student in students:
           if keyword in student["name"].lower():
            print(
                f'ID: {student["id"]} | '
                f'Name: {student["name"]} | '
                f'Department: {student["dept"]}'
            )
            found = True

      if not found:
        print("No matching student found.")

    def add_student(self):
        students = self.load_data()

        sid = self.get_next_id(students)

        print(f"Auto Generated Student ID: {sid}")

        name = input("Name: ")
        dept = input("Department: ")
        year = int(input("Year: "))
        email = input("Email: ")

        if not self.validate_email(email):
         print("Invalid email format!")
         return
        phone = input("Phone: ")

        student = Student(
            sid,
            name,
            dept,
            year,
            email,
            phone
        )

        students.append(student.to_dict())

        self.save_data(students)

        print("Student added successfully!")