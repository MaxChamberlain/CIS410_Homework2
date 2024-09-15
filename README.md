# Temperature Converter Program

## Overview

This Python program allows users to convert temperatures between Fahrenheit and Celsius. The program is designed to be modular, with separate functions for displaying the title, the menu, and performing the temperature conversions.

### Conversion Formulas:
- Celsius to Fahrenheit: `F = (C * 9 / 5) + 32`
- Fahrenheit to Celsius: `C = (F – 32) * 5 / 9`

## Features

- Convert temperatures from Fahrenheit to Celsius.
- Convert temperatures from Celsius to Fahrenheit.
- Displays results as rounded integers.
- User-friendly menu that allows repeated use.
- Clean, modular code with separate functions for conversions, displaying the title, and handling input/output.
- The program exits when the user chooses the option.

## How to Use

1. Run the `temperature_converter.py` file.
2. Choose an option from the menu:
   - Press `1` to convert Fahrenheit to Celsius.
   - Press `2` to convert Celsius to Fahrenheit.
   - Press `3` to exit the program.
3. Enter the temperature you want to convert.
4. The program will display the converted temperature and return to the menu for further use.

## Code Structure

- `conversions.py`: Contains functions for temperature conversions.
  - `fahrenheit_to_celsius(f)`: Converts Fahrenheit to Celsius.
  - `celsius_to_fahrenheit(c)`: Converts Celsius to Fahrenheit.
  
- `temperature_converter.py`: Main script.
  - `display_title()`: Displays the title of the program.
  - `display_menu()`: Displays the menu options.
  - `main()`: Handles user input and invokes the appropriate conversion functions.

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python installed on your machine.
2. Clone or download this repository.
3. Run the program from the command line or terminal:
   ```bash
   python temperature_converter.py
