import tkinter as tk
from subprocess import run  # Correct import statement
import os

def execute_flappy():
    folder_path = 'Flappy Bird'
    file_name = 'Flappy.exe'
    file_path = os.path.join('Flappy Bird', 'Flappy.exe')

    if os.path.exists(file_path):
        run(file_path)  # Correct usage of run
    else:
        print(f"The file {file_name} does not exist in the folder {folder_path}.")

# Create the main window
root = tk.Tk()
root.title("Flappy Bird Launcher")

# Create the button
button = tk.Button(root, text="Launch Flappy Bird", command=execute_flappy)
button.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()

print(os.getcwd())