# INPUT
users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
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

# PROCESS
while True:

    try:

        logged = False
        current_user = ""

        while logged == False:

            user = input("User: ")

            if user == "exit":
                exit()

            password = input("Password: ")

            if password == "exit":
                exit()

            if user in users:
                if users[user]['password'] == password:
                    logged = True
                    current_user = user
                else:
                    print("\nIncorrect password. Try again.\n")
            else:
                print("\nWrong User/Password. Try again.\n")

        user_role = users[current_user]['rol']

        print(f"\nWelcome, {users[current_user]['name']} ({user_role})")

        if user_role == 'student':

            print(f"\nReport card for {users[current_user]['name']}")

            aprobadas = set()
            pendientes = set()

            for subject_name in subjects:

                grade = notes[current_user][subject_name]
                print(f"{subject_name}: {grade}")

                if grade >= 7.0:
                    aprobadas.add(subject_name)
                else:
                    pendientes.add(subject_name)

            print(f"\nPassed subjects: {aprobadas}")
            print(f"Pending subjects: {pendientes}")

            option = input("\nexit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

        elif user_role == 'professor':

            print("\nStudent list:")

            for student_key in users:
                if users[student_key]['rol'] == 'student':
                    print(f"- {student_key} ({users[student_key]['name']})")

            student_to_grade = input("\nStudent (username): ")

            if student_to_grade == "exit":
                exit()

            while student_to_grade not in notes:
                print("\nStudent not found.")
                student_to_grade = input("Student (username): ")

                if student_to_grade == "exit":
                    exit()

            print("\nAvailable subjects:")

            for subject_name in subjects:
                print(f"- {subject_name}")

            subject_to_grade = input("\nSubject to modify: ")

            if subject_to_grade == "exit":
                exit()

            while subject_to_grade not in subjects:
                print("\nSubject not found.")
                subject_to_grade = input("Subject to modify: ")

                if subject_to_grade == "exit":
                    exit()

            confirmation = "no"

            while confirmation != "yes":

                new_grade = input("New grade: ")

                if new_grade == "exit":
                    exit()

                try:
                    new_grade = float(new_grade)
                except ValueError:
                    print("\nInvalid grade. Please enter a number.")
                    continue

                while new_grade < 0 or new_grade > 10:

                    print("\nGrade must be between 0 and 10.")

                    new_grade = input("New grade: ")

                    if new_grade == "exit":
                        exit()

                    try:
                        new_grade = float(new_grade)
                    except ValueError:
                        print("\nInvalid grade. Please enter a number.")
                        new_grade = -1
                        
                old_grade = notes[student_to_grade][subject_to_grade]

                print(f"\n{subject_to_grade}: {old_grade} ==> {new_grade}")

                confirmation = input("Are you sure you want to modify it? (yes/no): ")

                if confirmation == "exit":
                    exit()

                if confirmation == "yes":
                    notes[student_to_grade][subject_to_grade] = new_grade
                    print("\nGrade updated.")
                else:
                    print("\nModification cancelled.")

            option = input("\nexit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

        elif user_role == 'coordinator':

            print("\nTeacher list:")

            for prof_key in users:
                if users[prof_key]['rol'] == 'professor':
                    print(f"- {users[prof_key]['name']}")

            print("\nSubject list:")

            for subj in subjects:
                print(f"- {subj}")

            print("\nStudents and their grades:")

            for stu_key in notes:

                print(f"\n{users[stu_key]['name']}:")

                for subj in subjects:
                    print(f"  {subj}: {notes[stu_key][subj]}")

            option = input("\nexit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

    except KeyError:
        print("\nA required key was not found. Returning to login.")
        continue

    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user.")
        exit()

    except Exception as e:
        print(f"\nUnexpected error: {e}")
        continue
