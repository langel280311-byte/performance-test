students = []

def register_students(students, name, id):
    """register the student on the list."""
    name = input("Enter student's name: ")
    students[name] = {}
    print("Successfully registered student\n")
    if not name:
        print("The name cannot be empty")
        return False
    
def show_students(students):
    """shows the registered students."""
    if not students:
        print("there are no students.")
        return
    print(f"\n{'id':<20} {'name':>10} {'age':>10} {'course':>10} {'status':>10}")
    print("-" * 42)
    for s in students:
        print(f"{s['id']:<20} {s['name']:>10} {s['age']:>10} {s['course']:>10} {s['status']:>10}")
        
def update_students(students, name, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente."""
    if nuevo_precio is not None and nuevo_precio < 0:
        print("El precio no puede ser negativo.")
        return False
    if nueva_cantidad is not None and nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return False
    s = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None:
            p["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            p["cantidad"] = nueva_cantidad
        return True
    return False
    
def search_student(students, name):
    """searches and returns the student's name."""
    for s in students:
        if s["name"].lower() == name.strip().lower():
            return s
    return None

def student_list(students):
    """returns the student list."""
    if not students:
        return None

def remove_student(students, name):
    """Elimina un producto del inventario por nombre."""
    for i, s in enumerate(students):
        if s["name"].lower() == name.strip().lower():
            students.pop(i)
            return True
    return False 