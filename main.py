import conversions
    
def display_title():
    """Display the program title."""
    print("Temperature Converter Program")

def display_menu():
    """Display the conversion options."""
    print("\nMenu:")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

def main():
    """Main function to run the program."""
    display_title()

    while True:
        display_menu()
        choice = int(input("\nEnter your choice (1-3): "))

        if choice == 1:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = conversions.fahrenheit_to_celsius(f)
            print(f"{f}°F is {c}°C.")
        elif choice == 2:
            c = float(input("Enter temperature in Celsius: "))
            f = conversions.celsius_to_fahrenheit(c)
            print(f"{c}°C is {f}°F.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
