import streamlit as st
import smtplib
import random
import os
from datetime import datetime, timedelta

# ✅ Ensure session state variables are initialized
if "verification_codes" not in st.session_state:
    st.session_state["verification_codes"] = []  # Stores {"email": ..., "code": ..., "expires_at": ...}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Load allowed emails from external file
def load_allowed_emails():
    """Loads a list of authorized emails from emails.txt"""
    try:
        with open("emails.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

AUTHORIZED_EMAILS = load_allowed_emails()

def send_verification_email(email, code):
    """Sends the verification email with a 6-digit login code"""
    sender_email = "mokahlou@gmail.com"  # Replace with your Gmail
    sender_password = os.getenv("GOOGLE_APP_PASSWORD")  # Securely stored app password

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            message = f"Subject: Your Login Code\n\nYour verification code is: {code}"
            server.sendmail(sender_email, email, message)
        st.success("A login code has been sent to your email. Check your inbox.")
    except Exception as e:
        st.error("Error sending email. Please try again.")

def generate_code(email):
    """Generates and stores a verification code with a 5-minute expiration"""
    new_code = random.randint(100000, 999999)  # 6-digit code
    expires_at = datetime.now() + timedelta(minutes=5)  # Expiry time

    # Store the new code with expiration
    st.session_state["verification_codes"].append({
        "email": email,
        "code": new_code,
        "expires_at": expires_at
    })

    # Remove expired codes
    st.session_state["verification_codes"] = [
        c for c in st.session_state["verification_codes"] if c["expires_at"] > datetime.now()
    ]

    return new_code

def validate_code(email, input_code):
    """Checks if the entered verification code is still valid"""
    now = datetime.now()
    valid_codes = [c["code"] for c in st.session_state["verification_codes"] if c["email"] == email and c["expires_at"] > now]

    return int(input_code
