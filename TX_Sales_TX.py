import tkinter as tk
from tkinter import messagebox

# Constants
TEXAS_SALES_TAX_RATE = 0.0825

# Function to calculate and display the final cost
def calculate_final_cost(event=None):  # Added `event=None` to handle key binding
    try:
        # Get user inputs
        listed_price = float(entry_price.get())
        shipping = float(entry_shipping.get()) if entry_shipping.get() else 0.0

        # Conditional logic for tax calculation
        if shipping > 0:
            taxable_amount = listed_price + shipping
        else:
            taxable_amount = listed_price

        # Calculate sales tax and final cost
        sales_tax = taxable_amount * TEXAS_SALES_TAX_RATE
        final_cost = taxable_amount + sales_tax

        # Create result message
        result_message = (
            f"Listed Price: ${listed_price:.2f}\n"
            f"Shipping Cost: ${shipping:.2f}\n"
            f"Taxable Amount: ${taxable_amount:.2f}\n"
            f"Sales Tax (8.25%): ${sales_tax:.2f}\n"
            f"Final Cost: ${final_cost:.2f}"
        )

        # Display results in a message box
        messagebox.showinfo("Final Cost Breakdown", result_message)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the listed price and shipping.")

# Function to reset the input fields
def reset_fields():
    entry_price.delete(0, tk.END)
    entry_shipping.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Online Price Calculator")

# Create and place widgets
tk.Label(root, text="Listed Price ($):").grid(row=0, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Shipping Cost ($):").grid(row=1, column=0, padx=10, pady=5)
entry_shipping = tk.Entry(root)
entry_shipping.grid(row=1, column=1, padx=10, pady=5)

# Bind the Enter key to the calculate_final_cost function
root.bind('<Return>', calculate_final_cost)

# Create buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate_final_cost)
calculate_button.grid(row=2, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
