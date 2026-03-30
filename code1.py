from functions import *

students = []

while True:
    print("\n--- MENU ---")
    print("1. Add students")
    print("2. Show students")
    print("3. Search students (ID)")
    print("4. Update students")
    print("5. Delete students")
    print("6. Save CSV")
    print("7. Load CSV")
    print("8. Exit")
    


    option = input("option: ").strip()

    if option == "1":
        id = int(input("id: "))
        if not id:
            print("the id cannot be empty.")
            continue
        name = input("name: ").strip()
        if not name:
            print("The name cannot be empty.")
            continue
        try:
            age = int(input("age: "))
            course = input("course: ")
            status = input("Indicate whether you are an active or inactive student: ")
        except ValueError:
            print("Error: The student's age, course, or status cannot be empty.")
            continue
        
        if register_students(students):
            print(f"'{name}' student added successfully.")
            
    elif option == "2":
        show_students(students)
        
    elif option == "3":
        id = int(input("search: "))
        s = search_student(students, id)
        if s:
            print(f"Encontrado → {s['id']} | name: {s['name']} | age: {s['age']} | course: {s['course']} | status: {s['status']}")
        else:
            print("student not found.")
