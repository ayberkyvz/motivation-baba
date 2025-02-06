import tkinter as tk
import random
import webbrowser
from PIL import Image, ImageTk

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't stop when you're tired. Stop when you're done."
]

def display_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)
    quote_button.config(bg="#400128", fg="#A57A03", text="Not enough? Click for another inspiration")
    close_button.config(bg="#DAAB2D", fg="#020B13")  # Change the close button color and text color
    close_button.pack(pady=20)  # Show the close button

def close_app():
    root.destroy()

def open_url(event):
    webbrowser.open_new("https://www.ayberkyavuz.com/")

# Create the main window
root = tk.Tk()
root.title("Motivational Quotes")
root.geometry("1000x600")
root.configure(bg="#020B13")  # Set the background color of the main window

# Create a label to display the quote
quote_label = tk.Label(root, text="", wraplength=800, justify="center", font=("Helvetica", 20), bg="#020B13", fg="#A57A03")
quote_label.pack(pady=20)

# Create a button to generate a new quote
quote_button = tk.Button(root, text="Get Motivational Quote", command=display_quote, font=("Helvetica", 20), bg="#400128", fg="#A57A03", highlightbackground="#262626", highlightcolor="#262626", highlightthickness=2, relief="raised", padx=10, pady=5)
quote_button.pack(pady=20, anchor="center")

# Create a button to close the application (initially hidden)
close_button = tk.Button(root, text="Enough for today? Now click here and get back to work", command=close_app, font=("Helvetica", 20), bg="#DAAB2D", fg="#020B13", highlightbackground="#262626", highlightcolor="#262626", highlightthickness=2)

# Create a label for the credit text
credit_label = tk.Label(root, text="By Ayberk Yavuz, 2025", font=("Helvetica", 10), bg="#020B13", fg="#A57A03")
credit_label.pack(side="bottom", anchor="e", padx=10, pady=10)

# Load and resize the logo image
original_logo_image = Image.open("logo.png")  # Replace "logo.png" with the path to your image file
resized_logo_image = original_logo_image.resize((75, 75), Image.LANCZOS)  # Resize the image to 50x50 pixels
logo_image = ImageTk.PhotoImage(resized_logo_image)

# Create a label to display the logo at the bottom left
logo_label = tk.Label(root, image=logo_image, bg="#020B13")
logo_label.pack(side="bottom", anchor="w", padx=10, pady=10)
logo_label.bind("<Button-1>", open_url)  # Bind the left mouse button click event to the open_url function

# Run the application
root.mainloop()