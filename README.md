# Secure Data Hiding in Images Using Steganography
A Python-based project that hides encrypted messages inside images using steganography and cryptography.

## 📌 Project Overview
This project hides secret messages inside images using steganography and encryption.  
It ensures secure communication by making the message invisible inside an image.

## 🔧 Technologies Used
- **Python**
- **Tkinter** (GUI)
- **OpenCV** (Image Processing)
- **Cryptography.Fernet** (AES-based Encryption)
- **NumPy** (Data Handling)

## 📸 Screenshots
### 🔐 Encryption Process
1. Enter a **Secret Message** and **Passcode**.
2. Choose an **Image** to hide the message.
3. Save the **Encrypted Image**.

### 🔓 Decryption Process
1. Enter the **Passcode**.
2. Select the **Encrypted Image**.
3. Reveal the **Hidden Message**.

## 📂 How to Run the Project
1. **Install dependencies**:
   ```sh
   pip install opencv-python cryptography numpy tkinter
2. **Run the Encryption GUI**:
  ```sh
  python encrypt_gui.py

3. **Run the Decryption GUI**:
  ```sh
  python decrypt_gui.py

🎯 Features
✔ AES-based encryption for added security
✔ Steganography using Least Significant Bit (LSB) method
✔ Passcode protection – only authorized users can decrypt messages
✔ User-friendly GUI for both encryption and decryption
✔ Image quality remains unchanged after hiding the message

🔮 Future Enhancements
🚀 Support for more image formats (JPG, GIF, etc.)
🚀 Stronger encryption methods (AES-256, RSA, etc.)
🚀 Steganography in audio/video files
🚀 Mobile app version for Android/iOS
🚀 Cloud-based secure storage for encrypted images
