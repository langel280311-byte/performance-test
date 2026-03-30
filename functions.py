
def register_students(students, id, name, age, course, status):
    """register the student on the list."""
    name = input("Enter student's name: ")
    print("Successfully registered student\n")
    if not name.strip():
        print("The name cannot be empty")
        return False
    if search_student(students, name):
        print("a student with that name alreday exits")
        return False
    students.appened({
        "id":id,
        "name": name.strip(),
        "age":course,
        "status":status   
    })
    print("sucecesfully registered student /n")


def search_student(students, name):
    """searches and returns the student's name."""
    for s in students:
        if s["name"].lower() == name.strip().lower():
            return s
    return None

def show_students(students):
    """shows the registered students."""
    if not students:
        print("there are no students.")
        return
    print(f"\n{'id':<10} {'name':>20} {'age':>8} {'course':>15} {'status':>10}")
    print("-" * 65)
    for s in students:
        print(f"{s['id']:<10} {s['name']:>20} {s['age']:>8} {s['course']:>15} {s['status']:>10}")
        
def update_students(students, name, new_age=None, new_course=None, new_status=None):
    """Update age, course, and status."""
    s = search_student(students, name)
    if not s:
        print(f"not student fount with the name {name}")
        return False
    if new_age is not None and new_age < 0:
        print("Age cannot be a negative thing.")
        s["age"]= new_age
    if new_course is not None:
        s["course"]= new_course
    if new_status is not None:
        s["status"]= new_status
    print(f"students {name} update succesfully")
    

def student_list(students):
    """returns the student list."""
    if not students:
        return None
    return students

def remove_student(students, name):
    """Elimina un producto del inventario por nombre."""
    for i, s in enumerate(students):
        if s["name"].lower() == name.strip().lower():
            students.pop(i)
            print(f"student {name} removed")
            return True
        print(f"not students found with the name {name}")
    return False 