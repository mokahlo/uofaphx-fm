import streamlit as st
import smtplib
import random
import os
from datetime import datetime, timedelta

# Configure Page
st.set_page_config(page_title="Residency Rotations", page_icon="favicon.png", layout="wide")

# Define rotation folders for each residency year
ROTATIONS_FOLDER = "rotations"
YEARS = ["PGY-1", "PGY-2", "PGY-3", "Electives"]

# Load allowed emails from external file
def load_allowed_emails():
    try:
        with open("emails.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

AUTHORIZED_EMAILS = load_allowed_emails()

# Initialize session storage for codes
if "verification_codes" not in st.session_state:
    st.session_state["verification_codes"] = []  # Stores {"email": ..., "code": ..., "expires_at": ...}

# Email verification function
def send_verification_email(email, code):
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
        st.error(f"Error sending email: {e}")

# Generate and store verification code
def generate_code(email):
    new_code = random.randint(100000, 999999)  # Generate a 6-digit code
    expires_at = datetime.now() + timedelta(minutes=5)  # Code expires in 5 minutes

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

# Validate verification code
def validate_code(email, input_code):
    now = datetime.now()
    valid_codes = [c["code"] for c in st.session_state["verification_codes"] if c["email"] == email and c["expires_at"] > now]

    return int(input_code) in valid_codes

# User authentication system
def login():
    email = st.text_input("Enter your email:")

    # Only check authorization if the user has entered an email
    if email and email not in AUTHORIZED_EMAILS:
        st.error("You are not authorized to log in.")
        return

    if email and st.button("Send Verification Code"):
        code = generate_code(email)  # Generate & store code
        send_verification_email(email, code)

    # Show remaining time for active codes
    if email in [c["email"] for c in st.session_state["verification_codes"]]:
        st.subheader("Active Codes:")
        for code_entry in st.session_state["verification_codes"]:
            if code_entry["email"] == email:
                remaining_time = (code_entry["expires_at"] - datetime.now()).seconds
                st.write(f"🔢 **{code_entry['code']}** - Expires in {remaining_time // 60}:{remaining_time % 60:02d} minutes")

    # Validate user input code
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

# Load rotation details from a text file
def load_rotation_details(file_path):
    """Reads the content of a rotation file"""
    if not os.path.exists(file_path):
        return {"title": "Not Available", "content": "No information available."}
    
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    title = os.path.splitext(os.path.basename(file_path))[0].replace("_", " ")  # Extracts the title from the filename
    return {"title": title, "content": content}

# Check authentication before displaying content
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    login()
else:
    # Sidebar Navigation: Residency Years
    st.sidebar.title("Residency Years")
    selected_year = st.sidebar.radio("Select a Residency Year:", YEARS)

    # Get list of available rotations (text files) for the selected year
    year_folder_path = os.path.join(ROTATIONS_FOLDER, selected_year)
    if os.path.exists(year_folder_path):
        rotation_files = [f for f in os.listdir(year_folder_path) if f.endswith(".txt")]
        rotation_names = [os.path.splitext(f)[0].replace("_", " ") for f in rotation_files]  # Clean filenames
    else:
        rotation_files = []
        rotation_names = []

    # Display Tabs for Rotations in the Selected Residency Year
    st.title(f"Residency Year: {selected_year}")

    if rotation_files:
        selected_rotation = st.tabs(rotation_names)  # Create Tabs for each rotation
        
        for i, file_name in enumerate(rotation_files):
            with selected_rotation[i]:
                file_path = os.path.join(year_folder_path, file_name)
                rotation_info = load_rotation_details(file_path)
                st.header(rotation_info["title"])
                st.markdown(rotation_info["content"])  # Display file content as formatted text
    else:
        st.warning(f"No rotations found for {selected_year}. Please check the folder structure.")
