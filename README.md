# README

## Introduction
Hello, I am Misael Garay, a collector and hobbyist of figures. As a passionate collector, I often find myself shopping online for items to add to my collection. To simplify my purchasing decisions, I wanted a quick and easy way to calculate the final cost of an item I’m interested in buying. This project is a small tool I created to do just that.

The program calculates the total cost of an online purchase, including optional shipping fees and Texas sales tax, allowing for quick and accurate cost estimation.

---

## Features
- **User-Friendly Input**: Enter the listed price and optional shipping cost in a simple graphical interface.
- **Accurate Calculations**: Automatically includes Texas sales tax (8.25%) in the final cost.
- **Keyboard Shortcut**: Press Enter after entering the values to calculate the total instantly.
- **Reset Functionality**: Clear the input fields with a dedicated reset button.
- **Detailed Breakdown**: View a breakdown of listed price, shipping cost, taxable amount, sales tax, and final cost in an easy-to-read pop-up.

---

## Code Overview

### Language and Libraries
- **Python**: The program is written in Python for its simplicity and versatility.
- **Tkinter**: Used to create the graphical user interface (GUI).

### Key Components
1. **Constants**:
   - Texas sales tax rate is defined as a constant (`TEXAS_SALES_TAX_RATE = 0.0825`) for accuracy and easy updates.

2. **Functions**:
   - `calculate_final_cost`: Handles input validation, tax calculations, and displaying results in a pop-up.
   - `reset_fields`: Clears all input fields for new calculations.

3. **GUI Elements**:
   - Input fields for the listed price and shipping cost.
   - Buttons for calculating and resetting.
   - Keyboard shortcut (Enter key) for fast calculations.

4. **Error Handling**:
   - Displays an error message if invalid inputs are detected (e.g., non-numeric values).

### Execution
- Save the script as a `.py` file.
- Run it directly using Python.
- Use the GUI to input values and calculate the final cost.

---

## Usage
1. Launch the program.
2. Enter the item’s listed price in the first field.
3. (Optional) Enter the shipping cost in the second field.
4. Press Enter or click the "Calculate" button to see the total cost.
5. Review the detailed breakdown in the pop-up window.
6. Use the "Reset" button to clear the inputs and start a new calculation.

---

## Future Enhancements
- Add a feature to handle multiple tax rates for different states.
- Include currency conversion for international purchases.
- Save and load previous calculations for reference.

---

Thank you for using this tool! Feel free to reach out with suggestions or improvements.

