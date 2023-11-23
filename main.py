def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            source_unit = input("Enter the source unit (C for Celsius, F for Fahrenheit): ").upper()
            target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").upper()

            if source_unit == 'C' and target_unit == 'F':
                result = celsius_to_fahrenheit(value)
                print(f"{value} Celsius is equal to {result} Fahrenheit.")
            elif source_unit == 'F' and target_unit == 'C':
                result = fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is equal to {result} Celsius.")
            else:
                print("Invalid source or target unit. Please enter 'C' or 'F'.")

            break  # exit the loop if the input is valid and the conversion is done

        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    temperature_converter()
