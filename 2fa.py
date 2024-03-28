import pyotp
import pyqrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr():
    global totp, secret_key_entry
    # Get secret key from entry
    secret_key = secret_key_entry.get()

    messagebox.showinfo("Alert!","Scan this QR code in Google Authenticator App")

    # Create a TOTP object
    totp = pyotp.TOTP(secret_key)

    # Generate QR code
    qrcode = pyqrcode.create(totp.provisioning_uri("Authenticating User!"))
    qrcode.png("2fa_qr_code.png", scale=8)

    # Display QR code
    img = Image.open("2fa_qr_code.png")
    img.show()

def verify_otp():
    otp_input = otp_entry.get()
    if totp.verify(otp_input):
        messagebox.showinfo("OTP Verification", "OTP verification Successful! Access Granted :)")
    else:
        messagebox.showerror("OTP Verification", "OTP verification Failed! Access denied!")

def exit_application():
    root.destroy()

# Create main window
root = tk.Tk()
root.geometry("400x300")
root.title("Multi Factor Authentication")

# Secret Key Entry
secret_key_label = tk.Label(root, text="Enter the Secret key")
secret_key_label.pack()
secret_key_entry = tk.Entry(root)
secret_key_entry.pack(pady=5)

# Generate QR Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# OTP Entry
otp_label = tk.Label(root, text="Enter the OTP from your Authenticator App")
otp_label.pack()
otp_entry = tk.Entry(root)
otp_entry.pack(pady=5)

# Verify OTP Button
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack(pady=5)

root.mainloop()
