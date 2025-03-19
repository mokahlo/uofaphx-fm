import streamlit as st
import smtplib
import random
import os
from datetime import datetime, timedelta
import pytz

# ✅ Ensure session state variables are initialized safely
if "verification_codes" not in st.session_state:
    st.session_state["verification_codes"] = []  # Initialize as empty list

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
        st.success("✅ A login code has been sent to your email. Check your inbox.")
    except Exception as e:
        st.error("❌ Error sending email. Please try again.")

def generate_code(email):
    """Generates and stores a verification code with a 5-minute expiration"""
    new_code = random.randint(100000, 999999)  # 6-digit code
    expires_at = datetime.now(pytz.utc) + timedelta(minutes=5)  # Store in UTC

    # ✅ Ensure session state variable is initialized before use
    if "verification_codes" not in st.session_state:
        st.session_state["verification_codes"] = []

    # Remove expired codes
    st.session_state["verification_codes"] = [
        c for c in st.session_state["verification_codes"] if c["expires_at"] > datetime.now(pytz.utc)
    ]

    # Store the new code with expiration
    st.session_state["verification_codes"].append({
        "email": email,
        "code": new_code,
        "expires_at": expires_at
    })

    return new_code

def validate_code(email, input_code):
    """Checks if the entered verification code is still valid"""
    now = datetime.now(pytz.utc)

    # ✅ Ensure session state variable is initialized before use
    if "verification_codes" not in st.session_state:
        st.session_state["verification_codes"] = []

    valid_codes = [c["code"] for c in st.session_state["verification_codes"] if c["email"] == email and c["expires_at"] > now]

    return int(input_code) in valid_codes

def format_expiration_time(expiration_time_utc):
    """Formats expiration time to Arizona Time (MST or MDT)"""
    arizona_tz = pytz.timezone("America/Phoenix")
    expiration_time_az = expiration_time_utc.astimezone(arizona_tz)
    return expiration_time_az.strftime("Expires on %B %d, %Y, at %I:%M %p Arizona Time")

def login():
    """Handles the authentication process in Streamlit"""
    
    # ✅ Ensure session state variable is initialized before use
    if "verification_codes" not in st.session_state:
        st.session_state["verification_codes"] = []

    # ✅ Unique key to avoid StreamlitDuplicateElementId error
    email = st.text_input("Enter your email:", key="email_input").strip()

    # Authorization Check
    if email and email not in AUTHORIZED_EMAILS:
        st.error("❌ You are not authorized to log in.")
        return

    # Generate and send verification code
    if email and st.button("Send Verification Code", key="send_code_button"):
        code = generate_code(email)  # Generate & store code
        send_verification_email(email, code)

    # ✅ Ensure session state variable is initialized before use
    if "verification_codes" not in st.session_state:
        st.session_state["verification_codes"] = []

    # ✅ Show expiration time for active verification code
    active_code_entry = next((c for c in st.session_state["verification_codes"] if c["email"] == email), None)
    if active_code_entry:
        expiration_message = format_expiration_time(active_code_entry["expires_at"])
        st.subheader("Your code is active:")
        st.write(f"⏳ {expiration_message}")

    # User enters verification code
    if email:
        verification_code = st.text_input("Enter the verification code sent to your email:", key="verification_input")

        if st.button("Verify Code", key="verify_button"):
            if verification_code and verification_code.strip().isdigit():
                entered_code = verification_code.strip()
                if validate_code(email, entered_code):
                    st.session_state["authenticated"] = True
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid or expired code. Please try again.")
            else:
                st.error("⚠️ Please enter a valid 6-digit code.")
