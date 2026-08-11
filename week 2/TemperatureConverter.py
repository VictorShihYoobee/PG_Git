"""
A simple temperature converter that converts between Celsius and Fahrenheit.
by Victor Shih
2026.08.11
"""
class TempConverter:
    """A class to convert temperatures between Celsius and Fahrenheit."""

    def __init__(self, raw_input):
        self.format_input(raw_input.strip().upper())

    def format_input(self, raw_input):
        """ 
        Formats the input temperature and determines the conversion direction based on the prefix ('C' or 'F').
        """
        if raw_input.startswith('F'):
            self.choice = 'F'
            self.temperature = float(raw_input[1:])
        elif raw_input.startswith('C'):
            self.choice = 'C'
            self.temperature = float(raw_input[1:])

    def to_celsius(self):
        """
        Converts the temperature from Fahrenheit to Celsius.
        """
        return (self.temperature - 32) * 5.0 / 9.0

    def to_fahrenheit(self):
        """
        Converts the temperature from Celsius to Fahrenheit.
        """
        return (self.temperature * 9.0 / 5.0) + 32

    def check_input(self):
        """
        Checks if the input temperature is valid. Must start with 'F' or 'C' and be followed by a number.
        """
        if self.temperature.startswith('F') or self.temperature.startswith('C'):
            try:
                temp_value = float(self.temperature[1:])
                self.temperature = temp_value
            except ValueError:
                print("Invalid input.Please enter the temperature with the correct 'C' or 'F' prefix.")
                exit()

if __name__ == "__main__":
    temp_input = input("Enter temperature start with 'C' or 'F', or 'exit' to quit: ")
    while not (temp_input.startswith('F') or temp_input.startswith('C')):
        if temp_input.lower() == 'exit':
            exit()
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        temp_input = input("Enter temperature start with 'C' or 'F', or 'exit' to quit: ")
    converter = TempConverter(temp_input)

    """
    Converts the temperature based on the user's choice and prints the result.
    """
    if converter.choice == 'C':
        print(f"{converter.temperature}°F is {converter.to_celsius():.2f}°C")
    elif converter.choice == 'F':
        print(f"{converter.temperature}°C is {converter.to_fahrenheit():.2f}°F")
    

