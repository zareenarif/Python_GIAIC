import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = "key.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    KEY = f.read()

cipher = Fernet(KEY)

# File to store user data
DATA_FILE = "secure_data.txt"

# Load data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

# Helper functions
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(token):
    return cipher.decrypt(token.encode()).decode()

# Save data
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f)

# App
st.title("🔒 Secure Data Encryption App")

menu = ["Login", "Register", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Registration
if choice == "Register":
    st.subheader("📝 Register New User")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.error("User already exists!")
            else:
                stored_data[username] = {
                    "password": hash_passkey(password),
                    "data": ""
                }
                save_data()
                st.success("User registered successfully!")
        else:
            st.warning("Please fill all fields.")

# Login
elif choice == "Login":
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_passkey(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials!")

# Store Data
elif choice == "Store Data":
    if st.session_state.logged_in:
        st.subheader("📥 Store Secure Data")
        data = st.text_area("Enter data to store securely:")

        if st.button("Encrypt & Save"):
            if data:
                encrypted = encrypt(data)
                stored_data[st.session_state.username]["data"] = encrypted
                save_data()
                st.success("Data stored securely!")
            else:
                st.warning("Please enter data.")
    else:
        st.warning("Please login first.")

# Retrieve Data
elif choice == "Retrieve Data":
    if st.session_state.logged_in:
        st.subheader("🔍 Retrieve Your Data")

        encrypted = stored_data[st.session_state.username].get("data", "")
        if encrypted:
            try:
                decrypted = decrypt(encrypted)
                st.success(f"Your Decrypted Data: {decrypted}")
            except:
                st.error("Decryption failed!")
        else:
            st.warning("No data found.")
    else:
        st.warning("Please login first.")
