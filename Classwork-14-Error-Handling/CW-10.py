
# DATA
usuarios = {
    'keyrap': {'password': '150507', 'rol': 'alumno', 'nombre': 'Keyra Pool'},
    'arcadiod': {'password': '040804', 'rol': 'alumno', 'nombre': 'Arcadio Dardon'},
    'cristianc': {'password': '310702', 'rol': 'alumno', 'nombre': 'Cristian Cab'},
    'alejandroh': {'password': '300307', 'rol': 'alumno', 'nombre': 'Alejandro Hernandez'},
    'ivanr': {'password': '230402', 'rol': 'alumno', 'nombre': 'Ivan Rivas'},
    'yamilf': {'password': '1234', 'rol': 'alumno', 'nombre': 'Yamil Farah'},
    'jorgep': {'password': 'abcde', 'rol': 'maestro', 'nombre': 'Jorge Pedrozo'},
    'didierg': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Didier Gamboa'}
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
    'keyrap': {
        'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0,
        'Differential Calculus': 7.8, 'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'arcadiod': {
        'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4,
        'Differential Calculus': 6.2, 'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'cristianc': {
        'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5,
        'Differential Calculus': 7.0, 'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'alejandroh': {
        'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2,
        'Differential Calculus': 9.0, 'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'ivanr': {
        'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8,
        'Differential Calculus': 6.0, 'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'yamilf': {
        'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5,
        'Differential Calculus': 6.6, 'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# LOGIN
logged_in = False

while not logged_in:
    # INPUT
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    # PROCESS
    if username in usuarios and usuarios[username]["password"] == password:
        logged_in = True
        rol = usuarios[username]["rol"]
        nombre = usuarios[username]["nombre"]
        
        # OUTPUT
        print(f"\nBienvenido, {nombre} ({rol})")
    else:
        print("Credenciales incorrectas. Intenta de nuevo.\n")

# STUDENT MENU
if rol == "alumno":
    # PROCESS
    print(f"\nReport Card - {nombre}")
    print("=" * 40)
    pendientes = []

    for materia in subjects:
        nota = notes[username][materia]
        print(f"{materia}: {nota}")
        if nota < 7.0:
            pendientes.append(materia)

    # OUTPUT
    print("\nPending subjects:")
    if len(pendientes) == 0:
        print("None")
    else:
        for materia in pendientes:
            print("-", materia)

# TEACHER MENU
elif rol == "maestro":
    while True:
        # PROCESS
        print("\n===========================")
        print("Students")
        print("===========================")
        for usuario in usuarios:
            if usuarios[usuario]["rol"] == "alumno":
                print(f"User: {usuario} | Student: {usuarios[usuario]['nombre']}")

        # INPUT
        alumno = input("\nStudent to grade (username) or 'exit': ").strip()

        if alumno.lower() == "exit":
            break

        if alumno in notes:
            print("\n===========================")
            print("Subjects")
            print("===========================")
            for materia in subjects:
                print(materia)

            # INPUT
            materia = input("\nSubject to grade: ").strip()

            if materia.lower() == "exit":
                break

            if materia in subjects:
                # ERROR HANDLING FOR NUMERICAL INPUT
                try:
                    nueva_calificacion = float(input("New grade (0.0 - 10.0): "))
                    if not (0.0 <= nueva_calificacion <= 10.0):
                        print("Error: La calificación debe estar entre 0.0 y 10.0.")
                        continue
                except ValueError:
                    print("Error: Entrada inválida. Por favor ingresa un número decimal.")
                    continue

                actual = notes[alumno][materia]

                print("\nDo you confirm (yes/no)?")
                print(f"{materia}: {actual} ==> {nueva_calificacion}")
                confirmacion = input().lower().strip()

                if confirmacion == "yes":
                    # PROCESS
                    notes[alumno][materia] = nueva_calificacion
                    
                    # OUTPUT
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

    print("\nExiting teacher menu...")

# COORDINATOR MENU
elif rol == "coordinador":
    # OUTPUT
    print("\n===========================")
    print("Professors")
    print("===========================")
    for usuario in usuarios:
        if usuarios[usuario]["rol"] == "maestro":
            print(f"User: {usuario} | Professor: {usuarios[usuario]['nombre']}")

    print("\n===========================")
    print("Students")
    print("===========================")
    for usuario in usuarios:
        if usuarios[usuario]["rol"] == "alumno":
            print(f"User: {usuario} | Student: {usuarios[usuario]['nombre']}")

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

