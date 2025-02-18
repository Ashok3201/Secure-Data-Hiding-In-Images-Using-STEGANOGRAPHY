import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from cryptography.fernet import Fernet
import base64

# Function to generate a key from the passcode
def generate_key(passcode):
    key = base64.urlsafe_b64encode(passcode.ljust(32).encode()[:32])
    return Fernet(key)

# Convert binary to message
def binary_to_message(binary_str):
    byte_list = [binary_str[i: i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(b, 2)) for b in byte_list)

# Extract hidden message
def extract_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    if not file_path:
        return

    passcode = entry_passcode.get()
    if not passcode:
        messagebox.showerror("Error", "Passcode cannot be empty!")
        return

    img = cv2.imread(file_path)
    binary_data = ""

    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_data += format(pixel[channel], '08b')[-1]
                if binary_data.endswith('1111111111111110'):
                    binary_data = binary_data[:-16]
                    encrypted_message = binary_to_message(binary_data)

                    try:
                        cipher = generate_key(passcode)
                        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
                        messagebox.showinfo("Hidden Message", f"Extracted Message: {decrypted_message}")
                    except:
                        messagebox.showerror("Error", "Incorrect passcode or no hidden message found!")
                    return

    messagebox.showerror("Error", "No hidden message found!")

# GUI Design
root = tk.Tk()
root.title("Decryption - Extract Secret Message")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text="Enter Passcode:").grid(row=0, column=0, pady=5)
entry_passcode = tk.Entry(frame, width=50, show="*")  # Hide passcode input
entry_passcode.grid(row=0, column=1, pady=5)

extract_button = tk.Button(frame, text="Extract Message", command=extract_message, bg="lightgreen")
extract_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
