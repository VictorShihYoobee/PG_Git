from database import create_table
from user_manager import *

def menu():
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by NID")
    print("5. Show Student Count per Course")
    print("6. Show Students with Multiple Courses")
    print("0. Exit")

def main():
    create_table()
    populate_database()  # Ensure the database is populated with sample data
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            nid = input("Enter NID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            B_date = input("Enter birth date (YYYY-MM-DD): ")
            Phone_number = input("Enter phone number: ")
            
            add_user(nid, name, email, B_date, Phone_number)
        elif choice == '2':
            users = view_students()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_student(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter student NID to delete: "))
            delete_student(user_id)
        elif choice == '5':
            counts = show_student_count_per_course()
            for count in counts:
                print(count)
        elif choice == '6':
            students = show_students_with_multiple_courses()
            for student in students:
                print(student)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
