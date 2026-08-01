
def input_index():   
    height = input("Enter your height(CM): ")
    weight = input("Enter your weight(KG): ")

    return height, weight

def BMI(height, weight):
    bmi = int(weight) / ((int(height) / 100) ** 2)
    return bmi

if __name__ == "__main__":
    h, w =input_index()
    bmi = BMI(h, w)

    print(f"Your BMI is: {bmi:.2f}")
