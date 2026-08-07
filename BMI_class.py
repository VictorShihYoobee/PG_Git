class BmiCalculator:
    def calculate_bmi(self, height, weight):
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = weight / (height ** 2)
        return bmi

    @staticmethod
    def print_bmi(bmi):
        print(f"Your BMI is: {bmi:.2f}")
        
def input_index():   
        height = input("Enter your height(M): ")
        
        weight = input("Enter your weight(KG): ")
        while not weight.isnumeric():
            print("Please input a number")
            weight = input("Enter your weight(KG): ")

        return float(height), float(weight)

    
bmi = BmiCalculator()
h, w = input_index()

num = bmi.calculate_bmi(h, w)
bmi.print_bmi(num)
