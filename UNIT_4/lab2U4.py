# Lab Exercise 2: Student Data Manager Using Files

FILE_NAME = "students.txt"

while True:
    print("\n===== Student Data Manager =====")
    print("1. Add New Student Record")
    print("2. Display All Student Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{roll_no}, {name}, {marks}\n")

        print("Student record added successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                records = file.readlines()

                if len(records) == 0:
                    print("No student records found.")
                else:
                    print("\n--- Student Records ---")
                    for record in records:
                        print(record.strip())

        except FileNotFoundError:
            print("No student records found. File does not exist.")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")