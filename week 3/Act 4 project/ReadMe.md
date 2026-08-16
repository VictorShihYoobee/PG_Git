
Sure! Here is a README file for the project, explaining the structure, functionality, and how to use the application.

---

# Student Management System

## Overview

The Student Management System is a Python-based application that allows users to manage student records, including adding, viewing, searching, and deleting students. It uses SQLite as the underlying database to store student, lecturer, subject, lecture, and enrollment information.

## Requirements

- Python 3.x
- SQLite 3.x


## Database Setup

The database schema and sample data are managed through the `database.py` file. When you run the application, it will create the necessary tables and populate them with sample data.

## Application Structure

- `Act4_ERDmain.py`: The main entry point of the application, providing a text-based menu for interacting with the student management system.
- `user_manager.py`: Contains functions to manage student records, including adding, viewing, searching, and deleting students.
- `database.py`: Manages the database connection, schema creation, and data population.

## Usage

To run the application, execute the `Act4_ERDmain.py` file.

```bash
python Act4_ERDmain.py
```

### Menu Options

- **1. Add Student**: Adds a new student to the database.
- **2. View All Students**: Displays all student records.
- **3. Search Student by Name**: Searches for students by their first name.
- **4. Delete Student by NID**: Deletes a student record by NID.
- **5. Show Student Count per Course**: Displays the number of students enrolled in each course.
- **6. Show Students with Multiple Courses**: Displays students who are enrolled in more than one course.
- **0. Exit**: Exits the application.

### Example Interactions

1. **Add a Student**

    ```bash
    Select an option (1-6): 1
    Enter NID: STU006
    Enter name: John Doe
    Enter email: john.doe@example.com
    Enter birth date (YYYY-MM-DD): 2002-07-15
    Enter phone number: 026666666
    User added successfully.
    ```

2. **View All Students**

    ```bash
    Select an option (1-6): 2
    (1, 'STU001', 'Daniel', 'Banggawan', '2002-05-14', 'daniel@student.ac.nz', '021111111')
    (2, 'STU002', 'Choonho', 'Lee', '2000-08-22', 'choonho@student.ac.nz', '022222222')
    (3, 'STU003', 'Chaw', 'Theingi', '2001-11-03', 'chaw@student.ac.nz', '023333333')
    (4, 'STU004', 'Sukhjeet', 'Singh', '1999-03-19', 'sukhjeet@student.ac.nz', '024444444')
    (5, 'STU005', 'Smriti', 'Bhandari', '2001-01-30', 'smriti@student.ac.nz', '025555555')
    ```

3. **Search for a Student**

    ```bash
    Select an option (1-6): 3
    Enter name to search: Daniel
    (1, 'STU001', 'Daniel', 'Banggawan', '2002-05-14', 'daniel@student.ac.nz', '021111111')
    ```

4. **Delete a Student**

    ```bash
    Select an option (1-6): 4
    Enter student NID to delete: STU001
    🗑️ Student deleted.
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

This README file provides a comprehensive overview of the project, its components, and how to use it. You can customize it further based on your specific needs.