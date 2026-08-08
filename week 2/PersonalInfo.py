import random


class Person:
    """ 
    A class to represent a person with personal information.
    full_name: str - The full name of the person.
    age: int - The age of the person.
    address: str - The address of the person.
    student_id: str - The student ID of the person.
    """
    def __init__(self):
        self.full_name : str
        self.age : int
        self.address : str
        self.student_id : str

    def __init__(self, full_name, age, address, student_id):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.student_id = student_id

    def print_info(self):
        """
        Prints the personal information of the person.
        """
        print(f"Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Student ID: {self.student_id}")


def sort_people(people_list):
    """
    Bubble sorts a list of Person objects by their full name.
    """
    return sorted(people_list, key=lambda person: person.age)

def bubble_sort_people(people_list):
    """
    Bubble sorts a list of Person objects by their age.
    """
    n = len(people_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if people_list[j].age > people_list[j+1].age:
                people_list[j], people_list[j+1] = people_list[j+1], people_list[j]
    return people_list

def random_info():
    """
    Generates random personal information for a person.
    """
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis"]
    addresses = ["123 Main St", "456 Elm St", "789 Oak St", "101 Maple Ave", "202 Pine Rd"]
        
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 40)
    address = random.choice(addresses)
    student_id = f"S{random.randint(1000, 9999)}"
        
    return Person(full_name, age, address, student_id)  
        
if __name__ == "__main__":
    people = []

    num = input("Create 70 students or an unknown number of students? ( Y / N )... "
    "\n if you choose 70, the program will generate 70 random students. If you choose U, you can enter an unknown number of students manually.")

    if num == "Y":
        for i in range(70):
            """
            Generates random personal information for a person and adds it to the list.
            """
            person = random_info()
            people.append(person)
            person.print_info()
        print()

    cont = input("Add new person information ( Y/N )... ")

    while cont.lower() == 'y':
        """
        Prompts the user to enter personal information for a new person.
        """
        full_name = input("Enter full name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        student_id = input("Enter student ID: ")

        person = Person(full_name, age, address, student_id)
        people.append(person)
        person.print_info()
        print()

        cont = input("Add new person information ( Y/N )... ")
    persons_sorted = bubble_sort_people(people)

    """
    Sorts the list of Person objects by age and prints the sorted information."""
    print("\nSorted Person Information:")
    for person in persons_sorted:
        person.print_info()
        print()