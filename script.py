# Simple Classroom Attendance System for Bright Minds Academy

students = [
    "Ali", "Sarah", "James", "Fatima", "Omar",
    "Lucy", "David", "Mia", "Ahmed", "Emma"
]

# False = absent, True = present
present_status = [False] * len(students)

while True:
    # Display the menu
    print("\n--- Bright Minds Academy - Attendance System ---")
    print("1. View Present Students")
    print("2. Mark Student as Present")
    print("3. Mark Student as Absent")
    print("4. Exit")
    print("------------------------------------------------")

    # Get user choice
    choice = input("Enter your choice (1-4): ").strip()

    # Option 1: View Present Students
    if choice == '1':
        print("\nStudents Marked Present:")
        any_present = False

        for i in range(len(students)):
            if present_status[i]:
                print(f"- {students[i]}")
                any_present = True

        if not any_present:
            print("No students are marked present yet.")

        print("\nFull Summary:")
        for i in range(len(students)):
            status_text = "Present ✅" if present_status[i] else "Absent ❌"
            print(f"{students[i]}: {status_text}")

    # Option 2: Mark Student as Present
    elif choice == '2':
        name = input("Enter the student's name to mark present: ").strip().title()

        if name in students:
            index = students.index(name)
            if not present_status[index]:
                present_status[index] = True
                print(f"Attendance marked: {name} is now PRESENT.")
            else:
                print(f"{name} is already marked present.")
        else:
            print("Student not found. Please enter a valid registered student name.")

    # Option 3: Mark Student as Absent (undo present)
    elif choice == '3':
        name = input("Enter the student's name to mark absent: ").strip().title()

        if name in students:
            index = students.index(name)
            if present_status[index]:
                present_status[index] = False
                print(f"{name} is now marked ABSENT.")
            else:
                print(f"{name} was already marked absent.")
        else:
            print("Student not found. Please enter a valid registered student name.")

    # Option 4: Exit
    elif choice == '4':
        print("Closing attendance system. Have a great day!")
        break

    # Invalid option
    else:
        print("Invalid choice. Please select a valid option (1-4).")
