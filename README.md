# Secure Data Hiding in Images Using Steganography
A Python-based project that hides encrypted messages inside images using steganography and cryptography.

## 📌 Project Overview
This project hides secret messages inside images using steganography and encryption.  
It ensures secure communication by making the message invisible inside an image.

## 🎯 Features
- AES-based encryption for added security.
- Steganography using Least Significant Bit (LSB) method.
- Passcode protection – only authorized users can decrypt messages.
- User-friendly GUI for both encryption and decryption.
- Image quality remains unchanged after hiding the message.

## 📂 How to Run the Project
1. **Install dependencies**:
   ```sh
   pip install opencv-python cryptography numpy tkinter

### 🔐 Encryption Process
1. **Run the Encryption GUI**:
   ```sh
   python encrypt_gui.py
2. Enter a **Secret Message** and **Passcode**.
3. Choose an **Image** to hide the message.
4. Save the **Encrypted Image**.

### 🔓 Decryption Process
1. **Run the Decryption GUI**:
   ```sh
   python decrypt_gui.py
2. Enter the **Passcode**.
3. Select the **Encrypted Image**.
4. Reveal the **Hidden Message**.

## 📸 Result
<div align="center">
   <img src="https://github.com/Ashok3201/Secure-Data-Hiding-In-Images-Using-STEGANOGRAPHY/blob/main/pic.png" alt="Orignal Image" style="width:50%;">
   
   <img src="https://github.com/Ashok3201/Secure-Data-Hiding-In-Images-Using-STEGANOGRAPHY/blob/main/Encrypted_Image.png" alt="Encrypted Image" style="width:50%;">
</div>

## 🔧 Technologies Used
- **Python**
- **Tkinter** (GUI)
- **OpenCV** (Image Processing)
- **Cryptography.Fernet** (AES-based Encryption)
- **NumPy** (Data Handling)


## 🔮 Future Enhancements
- Support for more image formats (JPG, GIF, etc.)
- Stronger encryption methods (AES-256, RSA, etc.)
- Steganography in audio/video files
- Mobile app version for Android/iOS
- Cloud-based secure storage for encrypted images
