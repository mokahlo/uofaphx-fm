import streamlit as st
import smtplib
import random
import os

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

# Email verification function
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

# Login function
def login():
    email = st.text_input("Enter your email:")

    # Only check authorization if the user has entered an email
    if email and email not in AUTHORIZED_EMAILS:
        st.error("You are not authorized to log in.")
        return

    if email and st.button("Send Verification Code"):
        code = random.randint(100000, 999999)
        st.session_state["verification_code"] = code
        st.session_state["email"] = email
        send_verification_email(email, code)

    if "verification_code" in st.session_state and st.session_state.get("email") == email:
        verification_code = st.text_input("Enter the verification code sent to your email:")

        if st.button("Verify Code"):
            if verification_code and verification_code.strip().isdigit():
                entered_code = int(verification_code.strip())
                if entered_code == st.session_state["verification_code"]:
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("Invalid verification code. Please try again.")
            else:
                st.error("Please enter a valid 6-digit code.")

# Function to display rotation details
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
        "written_by": "