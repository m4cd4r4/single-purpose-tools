# Open .RTF files
# Requires the pyth, striprtf & tkinter library:
# "pip install pyth" etc

import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
from striprtf.striprtf import rtf_to_text

def read_rtf(file_path):
    try:
        with open(file_path, "r") as file:
            rtf_content = file.read()
        return rtf_to_text(rtf_content)
    except Exception as e:
        return f"Error reading RTF file: {e}"

def create_document_reader(content):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Document Reader")

    # Create a scrolled text widget
    text_area = ScrolledText(window, wrap=tk.WORD, width=80, height=30)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insert the content into the text widget
    text_area.insert(tk.INSERT, content)

    # Start the GUI event loop
    window.mainloop()

# Set up the Tkinter root window for file dialog
root = tk.Tk()
root.withdraw()  # Hide the root window

print("Opening file dialog...")
file_path = askopenfilename(parent=root, filetypes=[("RTF files", "*.rtf")])

# Destroy the root window after closing the dialog
root.destroy()

if file_path:
    print(f"File selected: {file_path}")
    content = read_rtf(file_path)
    if content:
        create_document_reader(content)
    else:
        print("No content to display.")
else:
    print("No file selected.")
