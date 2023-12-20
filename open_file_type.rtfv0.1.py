# Open .RTF files
# Requires the pyth library:
# "pip install pyth"

import os
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

def read_rtf(file_path):
    with open(file_path, "rb") as file:
        doc = Rtf15Reader.read(file)
    return PlaintextWriter.write(doc).getvalue()

def open_file(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."

    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.rtf':
        return read_rtf(file_path)
    else:
        return "Unsupported file format."

# Example usage
file_path = r'C:\Users\[REST-OF-FILEPATH].rtf'   # Change this to the path of your file
content = open_file(file_path)
print(content)
