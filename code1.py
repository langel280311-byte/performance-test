from functions import *

students = []

while True:
    print("\n--- MENU ---")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student (ID)")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    option = input("Option: ").strip()

    if option == "1":
        name = input("Name: ").strip()
        if not name:
            print("The name cannot be empty.")
            continue
        try:
            id = int(input("ID: "))
            age = int(input("Age: "))
        except ValueError:
            print("Error: ID and age must be numbers.")
            continue
        course = input("Course: ").strip()
        status = input("Status (active/inactive): ").strip()

        register_students(students, name, id, age, course, status)

    elif option == "2":
        show_students(students)

    elif option == "3":
        try:
            id = int(input("Enter ID to search: "))
        except ValueError:
            print("Error: ID must be a number.")
            continue
        s = search_student(students, id)
        if s:
            print(f"Found → ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']} | Status: {s['status']}")
        else:
            print("Student not found.")

    elif option == "4":
        try:
            id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Error: ID must be a number.")
            continue
        new_name   = input("New name (press Enter to skip): ").strip() or None
        new_age_str = input("New age (press Enter to skip): ").strip()
        new_age    = int(new_age_str) if new_age_str else None
        new_course = input("New course (press Enter to skip): ").strip() or None
        new_status = input("New status (press Enter to skip): ").strip() or None

        update_students(students, id, new_name, new_age, new_course, new_status)

    elif option == "5":
        name = input("Enter student name to delete: ").strip()
        remove_student(students, name)

    elif option == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")