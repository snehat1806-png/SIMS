from student_manager import StudentManager

manager = StudentManager()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
      manager.add_student()

    elif choice == "2":
      manager.list_students()

    elif choice == "3":
      manager.search_student()

    elif choice == "4":
      print("Exiting...")
      break  

    else:
        print("Invalid choice!")