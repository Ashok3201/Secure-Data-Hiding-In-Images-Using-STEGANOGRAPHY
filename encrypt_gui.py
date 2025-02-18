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

# Convert message to binary
def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

# Hide message in image
def hide_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    if not file_path:
        return

    message = entry_message.get()
    passcode = entry_passcode.get()

    if not message or not passcode:
        messagebox.showerror("Error", "Message and passcode cannot be empty!")
        return

    # Encrypt message using passcode
    cipher = generate_key(passcode)
    encrypted_message = cipher.encrypt(message.encode()).decode()

    # Convert encrypted message to binary
    binary_message = message_to_binary(encrypted_message) + '1111111111111110'  # End delimiter

    img = cv2.imread(file_path)
    data_index = 0
    binary_len = len(binary_message)

    for row in img:
        for pixel in row:
            for channel in range(3):
                if data_index < binary_len:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
                else:
                    break

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Message hidden successfully!")

# GUI Design
root = tk.Tk()
root.title("Encryption - Hide Secret Message")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text="Enter Secret Message:").grid(row=0, column=0, pady=5)
entry_message = tk.Entry(frame, width=50)
entry_message.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter Passcode:").grid(row=1, column=0, pady=5)
entry_passcode = tk.Entry(frame, width=50, show="*")  # Hide passcode input
entry_passcode.grid(row=1, column=1, pady=5)

hide_button = tk.Button(frame, text="Hide Message", command=hide_message, bg="lightblue")
hide_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
