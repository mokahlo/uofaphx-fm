import streamlit as st
import smtplib
import random
import os
from datetime import datetime, timedelta  # ✅ NEW: Handle expiration timing

# Favicon Image
st.set_page_config(
    page_title="Residency Rotations",
    page_icon="favicon.png"
)

# Load allowed emails from external file
def load_allowed_emails():
    try:
        with open("emails.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

AUTHORIZED_EMAILS = load_allowed_emails()

# ✅ NEW: Initialize session storage for codes if not present
if "verification_codes" not in st.session_state:
    st.session_state["verification_codes"] = []  # Stores {"email": ..., "code": ..., "expires_at": ...}

# ✅ UPDATED: Email verification function (unchanged)
def send_verification_email(email, code):
    sender_email = "mokahlou@gmail.com"  # Replace with your Gmail
    sender_password = os.getenv("GOOGLE_APP_PASSWORD")  # App password stored securely

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            message = f"Subject: Your Login Code\n\nYour verification code is: {code}"
            server.sendmail(sender_email, email, message)
        st.success("A login code has been sent to your email. Check your inbox.")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# ✅ NEW: Function to generate and store codes with expiration
def generate_code(email):
    new_code = random.randint(100000, 999999)  # Generate a 6-digit code
    expires_at = datetime.now() + timedelta(minutes=5)  # Set expiration time (5 minutes)

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

# ✅ NEW: Function to validate codes (allowing past codes within 5 minutes)
def validate_code(email, input_code):
    now = datetime.now()
    valid_codes = [c["code"] for c in st.session_state["verification_codes"] if c["email"] == email and c["expires_at"] > now]

    return int(input_code) in valid_codes

# ✅ UPDATED: Login function now supports multiple valid codes
def login():
    email = st.text_input("Enter your email:")

    # Only check authorization if the user has entered an email
    if email and email not in AUTHORIZED_EMAILS:
        st.error("You are not authorized to log in.")
        return

    if email and st.button("Send Verification Code"):
        code = generate_code(email)  # ✅ NEW: Use the function to generate & store multiple codes
        send_verification_email(email, code)

    # ✅ NEW: Show remaining time for active codes
    if email in [c["email"] for c in st.session_state["verification_codes"]]:
        st.subheader("Active Codes:")
        for code_entry in st.session_state["verification_codes"]:
            if code_entry["email"] == email:
                remaining_time = (code_entry["expires_at"] - datetime.now()).seconds
                st.write(f"🔢 **{code_entry['code']}** - Expires in {remaining_time // 60}:{remaining_time % 60:02d} minutes")

    # ✅ UPDATED: Validate against multiple valid past codes
    if email:
        verification_code = st.text_input("Enter the verification code sent to your email:")

        if st.button("Verify Code"):
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

# ✅ NO CHANGES TO ROTATION FUNCTIONALITY BELOW
def display_rotation_info(rotation_details):
    st.write(f"### {rotation_details['title']}")
    st.write(f"**Last Updated:** {rotation_details['last_updated']}")
    st.write(f"**Written by:** {rotation_details['written_by']}")
    st.write("----")
    
    for section, content in rotation_details["details"].items():
        with st.expander(section):
            st.write(content)

# Define rotation details
rotations = {
    "General Surgery (A/Endo)": {
        "title": "General Surgery (A/Endo) Rotation",
        "last_updated": "11/26/24",
        "written_by": "Anas, updated by Nat",
        "details": {
            "First Day Logistics": """Details on when and where to report, 
            WhatsApp group info, etc.""",
            "Team Structure": """Overview of resident roles and hierarchy.""",
            "Schedule & Service Expectations": """Daily expectations, clinic vs. OR assignments.""",
            "Sign Out": """Sign-out procedures and responsibilities.""",
            "Progress Notes": """Standard note templates and expectations.""",
            "Hospital Orders/Discharge Orders": """Common discharge procedures.""",
            "Clinic Expectations": """How to manage clinic patients and documentation.""",
        }
    },
    "Obstetrics & Gynecology": {
        "title": "Obstetrics & Gynecology Rotation",
        "last_updated": "10/15/24",
        "written_by": "Nat",
        "details": {
            "First Day Logistics": "Arrive at hospital by 6 AM...",
            "Team Structure": "You will be assigned a resident mentor...",
        }
    }
}

# Run the login system
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    login()
else:
    st.success("Welcome! You are logged in.")
    selected_rotation = st.selectbox("Select a Rotation", list(rotations.keys()))
    display_rotation_info(rotations[selected_rotation])
