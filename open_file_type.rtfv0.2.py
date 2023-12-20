# Open .RTF files
# Requires the pyth, striprtf & tkinter library:
# "pip install pyth" etc

import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from striprtf.striprtf import rtf_to_text

def read_rtf(file_path):
    try:
        with open(file_path, "r") as file:
            rtf_content = file.read()
        print("RTF Content Read (raw):")
        print(rtf_content[:500])  # Print the first 500 characters of the raw RTF content
        text_content = rtf_to_text(rtf_content)
        print("Converted Text Content:")
        print(text_content[:500])  # Print the first 500 characters of the converted text
        return text_content
    except Exception as e:
        return f"Error reading RTF file: {e}"

def open_file(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."

    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.rtf':
        return read_rtf(file_path)
    else:
        return "Unsupported file format."

# Set up the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

print("Opening file dialog...")
file_path = askopenfilename(parent=root, filetypes=[("RTF files", "*.rtf")])

# Destroy the root window after closing the dialog
root.destroy()

if file_path:
    print(f"File selected: {file_path}")
    content = open_file(file_path)
    print("File content:")
    print(content)
else:
    print("No file selected.")

