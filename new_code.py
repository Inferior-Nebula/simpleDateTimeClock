# 4/14/25
# Making a pop-up window that shows the current date and time in a styled format

from datetime import datetime               # For getting the current date and time
import tkinter as tk                        # GUI framework for window creation
from tkinter import Toplevel                # Allows us to create pop-up windows

# Get the current date and time from the system
date = datetime.now()

# Format the date and time using strftime:
# %A = full weekday name, %B = full month name, %#d = day without leading 0 (use %-d on Mac/Linux)
# %Y = full year, %I = 12-hour, %M = minutes, %p = AM/PM
formatted_date = date.strftime("%A, %B %#d, %Y")  
formatted_time = date.strftime("%I:%M %p")

# Create a function that applies a fade-in effect to a given window
def fade_in(window, alpha=0):
    alpha = round(alpha + 0.05, 2)                 # Increase transparency level slightly
    if alpha <= 1.0:
        window.attributes("-alpha", alpha)         # Set new transparency level
        window.after(30, lambda: fade_in(window, alpha))  # Call again after 30ms to animate

# Create the main application window
root = tk.Tk()                         # Initialize the root window
root.title("Time Viewer")              # Set the window title bar

# Function to create and display the pop-up window
def open_popup():
    popup = Toplevel(root)             # Create a new window on top of the main one
    popup.title("🕒 Current Time")      # Set pop-up title
    popup.geometry("400x300")          # Set pop-up size (width x height)
    popup.configure(bg="#e6f2ff")      # Set background color to a soft blue
    popup.attributes("-alpha", 0.0)    # Start fully transparent
    fade_in(popup)                     # Begin the fade-in effect

    # Build the string to display, using emojis and formatted date/time
    message = f"📅 Today is:\n{formatted_date}\n\n🕰️ Current time:\n{formatted_time}"

    # Create and style a label to display the date/time message
    label = tk.Label(
        popup,
        text=message,
        font=("Helvetica", 16, "bold"),  # Use bold Helvetica font
        bg="#e6f2ff",                    # Same background color for seamless look
        fg="#333"                        # Dark gray text for readability
    )
    label.pack(pady=30)                # Add vertical padding

    # Create a button to close the pop-up window
    close_button = tk.Button(
        popup,
        text="Close",                   # Text on the button
        command=popup.destroy,          # Destroy (close) window when clicked
        font=("Arial", 12),             # Use Arial font for the button
        bg="#cce6ff",                   # Slightly different soft blue for contrast
        relief="raised"                 # Give the button a raised appearance
    )
    close_button.pack(pady=10)         # Add space below the button

# Create a button in the main window that opens the pop-up when clicked
open_button = tk.Button(
    root,
    text="See the Current Time",       # Button label
    command=open_popup,                # Function to call on click
    font=("Arial", 14),                # Font styling
    bg="#b3d9ff"                       # Blue button background
)
open_button.pack(pady=40)             # Center it vertically with padding

# Start the GUI event loop to keep the window open and responsive
root.mainloop()
