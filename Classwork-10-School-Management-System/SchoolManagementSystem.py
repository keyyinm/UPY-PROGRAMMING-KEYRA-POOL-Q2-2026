# School Management System

# DATA

users = {
    'jperez': {'password': '1234', 'rol': 'student', 'name': 'Juan Pérez'},
    'dromo': {'password': '1234', 'rol': 'student', 'name': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'student', 'name': 'Mauricio Juárez'},
    'mlopez': {'password': '1234', 'rol': 'student', 'name': 'María López'},
    'euc': {'password': '1234', 'rol': 'student', 'name': 'Ernesto Uc'},
    'cbalam': {'password': '1234', 'rol': 'student', 'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# LOGIN

logged_in = False

while not logged_in:

    # INPUT
    username = input("Usuario: ")
    password = input("Contraseña: ")

    # PROCESS
    if username in users and users[username]["password"] == password:
        logged_in = True
        rol = users[username]["rol"]
        nombre = users[username]["name"]

        # OUTPUT
        print(f"\nBienvenido, {nombre} ({rol})")

    else:
        print("Credenciales incorrectas. Intenta de nuevo.")

# STUDENT MENU

if rol == "student":

    print(f"\nReport Card - {nombre}")
    print("=" * 40)

    pendientes = []

    for materia in subjects:
        nota = notes[username][materia]
        print(f"{materia}: {nota}")

        if nota < 7.0:
            pendientes.append(materia)

    print("\nPending subjects:")

    if len(pendientes) == 0:
        print("None")
    else:
        for materia in pendientes:
            print("-", materia)

# PROFESSOR MENU

elif rol == "professor":

    while True:

        print("\n===========================")
        print("Students")
        print("===========================")

        for usuario in users:
            if users[usuario]["rol"] == "student":
                print(f"User: {usuario} | Student: {users[usuario]['name']}")

        alumno = input("\nStudent to grade (username): ")

        if alumno.lower() == "exit":
            break

        if alumno in notes:

            print("\n===========================")
            print("Subjects")
            print("===========================")

            for materia in subjects:
                print(materia)

            materia = input("\nSubject to grade: ")

            if materia.lower() == "exit":
                break

            if materia in subjects:

                nueva_calificacion = float(input("New grade: "))

                actual = notes[alumno][materia]

                print("\nDo you confirm (yes/no)?")
                print(f"{materia}: {actual} ==> {nueva_calificacion}")

                confirmacion = input().lower()

                if confirmacion == "yes":

                    notes[alumno][materia] = nueva_calificacion

                    print("\nGrade updated!")

                    print("\n===========================")
                    print("Updated Record")
                    print("===========================")

                    for materia_actual in subjects:
                        print(f"{materia_actual}: {notes[alumno][materia_actual]}")

                else:
                    print("\nGrade not updated.")

            else:
                print("\nInvalid subject.")

        else:
            print("\nInvalid student.")

    print("\nExiting professor menu...")

# COORDINATOR MENU

elif rol == "coordinator":

    print("\n===========================")
    print("Professors")
    print("===========================")

    for usuario in users:
        if users[usuario]["rol"] == "professor":
            print(f"User: {usuario} | Professor: {users[usuario]['name']}")

    print("\n===========================")
    print("Students")
    print("===========================")

    for usuario in users:
        if users[usuario]["rol"] == "student":
            print(f"User: {usuario} | Student: {users[usuario]['name']}")

    print("\n===========================")
    print("Records")
    print("===========================")

    encabezado = "SUBJECTS".ljust(35)

    for alumno in notes:
        encabezado += alumno.ljust(12)

    print(encabezado)
    print("-" * len(encabezado))

    for materia in subjects:

        fila = materia[:33].ljust(35)

        for alumno in notes:
            fila += str(notes[alumno][materia]).ljust(12)

        print(fila)
