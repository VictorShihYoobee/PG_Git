from Person import Person

class Staff(Person):
    """inheritant Person and add new attribute: tax_num"""
    def __init__(self, id, name, tax_num):
        super().__init__(id, name)
        self.tax_num = tax_num

class General(Staff):
    """"general staff has rate_of_pay"""
    def __init__(self, id, name, tax_num, rate_of_pay):
        super().__init__(id, name, tax_num)
        self.rate = rate_of_pay
    
    def display_pay_rate(self):
        print(f"General Staff: {self.name} (ID: {self.id})")
        print(f"Pay Rate: ${self.rate:.2f}/hr\n")

class Academic(Staff):
    """academic staff has a list of publications"""
    def __init__(self, id, name, tax_num, publications):
        super().__init__(id, name, tax_num) 
        self.publications = publications

    def get_publications(self):
        #count the publications
        return len(self.publications)
    
if __name__ == "__main__":
    #1. general
    general = General(2,"gen", "111", 1000)
    general.display_pay_rate()
    
    #2. academic
    lecturer = Academic(1, "lect", "123", publications = ["p1", "p2"])
    print("Numbers of publications: ", lecturer.get_publications())

    
