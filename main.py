import json
from datetime import datetime

DATA_FOLDER = "StudentData"
DELETED_FOLDER = "DeletedStudents"

# Create folders if not exist
for folder in [DATA_FOLDER, DELETED_FOLDER]:
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_next_id():
    files = os.listdir(DATA_FOLDER)
    if not files:
        return 101
    ids = [int(f.split(".")[0]) for f in files]
    return max(ids) + 1

def validate_email(email):
    return "@" in email and "." in email


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_year(year):
    return year.isdigit() and 1 <= int(year) <= 4


# ----------------- Core Features -----------------

def get_next_id(students):
    if not students:
        return 101
    return max(student["id"] for student in students) + 1


def add_student():
    students = load_data()
    sid = get_next_id(students)

    print(f"Auto Generated Student ID: {sid}")

    name = input("Name: ")
    dept = input("Department: ")

    year = input("Year (1-4): ")
    if not validate_year(year):
        print("Invalid year!")
        return

    email = input("Email: ")
    if not validate_email(email):
        print("Invalid email!")
        return

    phone = input("Phone (10 digits): ")
    if not validate_phone(phone):
        print("Invalid phone!")
        return

    new_student = {
        "id": sid,
        "name": name,
        "dept": dept,
        "year": int(year),
        "email": email,
        "phone": phone,
        "status": "ACTIVE",
        "lastUpdated": str(datetime.now())
    }

    students.append(new_student)
    save_data(students)

    print("Student added successfully!")


def view_student():
    students = load_data()
    sid = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == sid:
            for key, value in student.items():
                print(f"{key}: {value}")
            return

    print("Student not found.")


def list_students():
    students = load_data()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(f'{student["id"]} - {student["name"]} ({student["dept"]})')


def search_by_name():
    students = load_data()
    keyword = input("Enter name to search: ").lower()

    found = False

    for student in students:
        if keyword in student["name"].lower():
            print(f'{student["id"]} - {student["name"]}')
            found = True

    if not found:
        print("No matching student found.")


def update_student():
    students = load_data()
    sid = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == sid:
            print("1. Name")
            print("2. Department")
            print("3. Year")
            print("4. Email")
            print("5. Phone")

            choice = input("Enter choice: ")

            field_map = {
                "1": "name",
                "2": "dept",
                "3": "year",
                "4": "email",
                "5": "phone"
            }

            if choice not in field_map:
                print("Invalid choice!")
                return

            new_value = input("Enter new value: ")

            if field_map[choice] == "year":
                if not validate_year(new_value):
                    print("Invalid year!")
                    return
                new_value = int(new_value)

            student[field_map[choice]] = new_value
            student["lastUpdated"] = str(datetime.now())

            save_data(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_data()
    sid = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == sid:
            student["status"] = "DELETED"
            student["lastUpdated"] = str(datetime.now())
            save_data(students)
            print("Student soft deleted.")
            return

    print("Student not found.")


# ----------------- Menu -----------------

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. List Students")
        print("4. Search by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            list_students()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


menu()