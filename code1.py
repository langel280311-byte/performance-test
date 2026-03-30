from functions import *

students = []

while True:
    print("\n--- MENU ---")
    print("1. Add students")
    print("2. Show students")
    print("3. Search students (ID)")
    print("4. Update students")
    print("5. Delete students")
    print("6. Exit")
    
    option = input("option: ").strip()

    if option == "1":
        name = input("name: ")
        if not name:
            print("the name cannot be empty.")
            continue
        try:
            id = int(input("ID: "))
            age = int(input("age: "))
        except ValueError:
            print("error: id and age must be numbers")
            continue
        try:
            course = input("course: ").strip()
            status = input("Indicate whether you are an active or inactive student: ").strip()
        except ValueError:
            print("Error: The student course or status cannot be empty.")
        
        if register_students(students, name, id, age, course, status):
            print(f"student {name}' added correctly")

    elif option == "2":
        show_students(students)
        
    elif option == "3":
        id = int(input("search: "))
        s = search_student(students, id)
        if s:
            print(f"Encontrado → {s['id']} | name: {s['name']} | age: {s['age']} | course: {s['course']} | status: {s['status']}")
        else:
            print("student not found.")
            
    elif option == "4":
        name = input("Update the name (press enter to skip): ").strip()
        id = input("student ID to update: ").strip()
        age = input("Update the age(press Enter to skip)): ").strip()
        course = input("Update the course (press Enter to skip)").strip()
        status = input("Update the status (press Enter to skip)").strip()
    
    elif option == "5":
        name = input("enter student name to delete").strip()
        remove_student(students, name)
    
    elif option == "6":
        print("goodbye")
        break
    
    else:
        print("invalid option")