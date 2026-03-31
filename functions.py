def register_students(students, name, id, age, course, status):
    """Register the student on the list."""
    if not name.strip():
        print("The name cannot be empty.")
        return False
    if search_student(students, id):
        print("A student with that ID already exists.")
        return False
    students.append({
        "id": id,
        "name": name.strip(),
        "age": age,
        "course": course,
        "status": status
    })
    print("Successfully registered student.")
    return True

def search_student(students, id):
    """Searches and returns a student by ID."""
    for s in students:
        if s["id"] == id:
            return s
    return None

def show_students(students):
    """Shows the registered students."""
    if not students:
        print("There are no students.")
        return
    print(f"\n{'ID':<10} {'Name':>20} {'Age':>8} {'Course':>15} {'Status':>10}")
    print("-" * 65)
    for s in students:
        print(f"{s['id']:<10} {s['name']:>20} {s['age']:>8} {s['course']:>15} {s['status']:>10}")

def update_students(students, id, new_name=None, new_age=None, new_course=None, new_status=None):
    """Update name, age, course, and status by student ID."""
    s = search_student(students, id)
    if not s:
        print(f"No student found with ID {id}.")
        return False
    if new_name:
        s["name"] = new_name
    if new_age is not None:
        if new_age < 0:
            print("Age cannot be negative.")
            return False
        s["age"] = new_age
    if new_course:
        s["course"] = new_course
    if new_status:
        s["status"] = new_status
    print(f"Student with ID {id} updated successfully.")
    return True

def student_list(students):
    """Returns the student list."""
    if not students:
        return None
    return students

def remove_student(students, name):
    """Removes a student from the list by name."""
    for i, s in enumerate(students):
        if s["name"].lower() == name.strip().lower():
            students.pop(i)
            print(f"Student '{name}' removed.")
            return True
    print(f"No student found with the name '{name}'.")
    return False