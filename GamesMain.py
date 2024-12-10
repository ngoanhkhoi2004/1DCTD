import tkinter as tk
import sys
import subprocess


# List of games and their respective launch functions
games = [
    ("Tank Game", lambda: subprocess.run([sys.executable, 'TankMain.py'])),
    ("Grade 5", lambda: subprocess.run([sys.executable, 'SmarterThanGrade5.py'])),
    ("Character Game", lambda: subprocess.run([sys.executable, 'ThirdGame.py'])),
]

current_selection = 0  # Keeps track of the currently selected menu item

# Function to update the arrow position
def update_menu():
    for i, label in enumerate(menu_labels):
        if i == current_selection:
            label.config(text=f"-> {games[i][0]}", fg="yellow")
        else:
            label.config(text=f"   {games[i][0]}", fg="white")

# Function to handle key presses
def navigate_menu(event):
    global current_selection
    if event.keysym == "Up":
        current_selection = (current_selection - 1) % len(games)
        update_menu()
    elif event.keysym == "Down":
        current_selection = (current_selection + 1) % len(games)
        update_menu()
    elif event.keysym == "Return":
        games[current_selection][1]()  # Call the function for the selected game

# Initialize the main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("700x600")
root.configure(bg="black")

# Title Label
title_label = tk.Label(root, text="Game Menu", font=("Arial", 28), fg="white", bg="black")
title_label.pack(pady=20)

# Create menu labels
menu_labels = []
for game in games:
    label = tk.Label(root, text=f"   {game[0]}", font=("Arial", 20), fg="white", bg="black", anchor="w")
    label.pack(pady=10)
    menu_labels.append(label)

# Update the initial menu to highlight the first option
update_menu()

# Bind keys for navigation
root.bind("<Up>", navigate_menu)
root.bind("<Down>", navigate_menu)
root.bind("<Return>", navigate_menu)

# Run the application
root.mainloop()
