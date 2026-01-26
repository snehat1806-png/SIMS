import os
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

# ---------- Core Features ----------

def add_student():
    sid = str(get_next_id())
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

    filename = f"{DATA_FOLDER}/{sid}.txt"
    with open(filename, "w") as f:
        f.write(f"ID:{sid}\n")
        f.write(f"Name:{name}\n")
        f.write(f"Dept:{dept}\n")
        f.write(f"Year:{year}\n")
        f.write(f"Email:{email}\n")
        f.write(f"Phone:{phone}\n")
        f.write("Status:ACTIVE\n")
        f.write(f"LastUpdated:{datetime.now()}\n")

    print("Student added successfully!")

def view_student():
    sid = input("Enter Student ID: ")
    filename = f"{DATA_FOLDER}/{sid}.txt"

    if not os.path.exists(filename):
        print("Student not found!")
        return

    print("\n----- STUDENT PROFILE -----")
    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split(":", 1)
            print(f"{key:<12}: {value}")
    print("---------------------------")

def list_students():
    files = os.listdir(DATA_FOLDER)
    if not files:
        print("No students found.")
        return

    print("\n--- ALL STUDENTS ---")
    for f in files:
        with open(f"{DATA_FOLDER}/{f}", "r") as file:
            lines = file.readlines()
            sid = lines[0].split(":")[1].strip()
            name = lines[1].split(":")[1].strip()
            dept = lines[2].split(":")[1].strip()
            print(f"{sid} - {name} ({dept})")

def search_by_name():
    keyword = input("Enter name to search: ").lower()
    found = False

    for f in os.listdir(DATA_FOLDER):
        with open(f"{DATA_FOLDER}/{f}", "r") as file:
            lines = file.readlines()
            name = lines[1].split(":")[1].strip().lower()
            if keyword in name:
                sid = lines[0].split(":")[1].strip()
                print(f"Found: {sid} - {lines[1].split(':')[1].strip()}")
                found = True

    if not found:
        print("No matching student found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    src = f"{DATA_FOLDER}/{sid}.txt"
    dest = f"{DELETED_FOLDER}/{sid}.txt"

    if os.path.exists(src):
        os.rename(src, dest)
        print("Student moved to DeletedStudents (Soft Delete).")
    else:
        print("Student not found!")

# ---------- Menu ----------

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Student Profile")
        print("3. List All Students")
        print("4. Search Student by Name")
        print("5. Delete Student (Soft Delete)")
        print("6. Exit")

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
            delete_student()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

menu()
