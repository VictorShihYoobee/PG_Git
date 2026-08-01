
if __name__ == "__main__":
    print("Hello Python")
    num = input("Enter a number: ")

    while not num.isnumeric() :
        print("Please input a number")
        num = input("Enter a number: ")

    num1 = 0
    num2 = 1
    num_tmp = 0
    num = int(num)
    if num < 0:
        print("Please input a number greater than 1.")
    elif num == 1:
        print(num1, end=" ")
    elif num >= 2:
        print(num1, num2, end=" ")
        num = int(num) - 2
        #print(num)
        for i in range(num):
            num_tmp = num1 + num2
            num1 = num2
            num2 = num_tmp
            print(num_tmp, end=" ")