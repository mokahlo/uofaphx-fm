import streamlit as st
import hashlib
import smtplib
import random
import os

# Simulated database (replace with real DB in production)
USER_DATABASE = {}
VERIFICATION_CODES = {}
AUTHORIZED_EMAILS = ["mokahlou@gmail.com", "elemendza@gmail.com"]

# Email verification function
def send_verification_email(email, code):
    sender_email = "your-email@example.com"  # Replace with your email
    sender_password = "your-email-password"  # Replace with a secure password
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: Your Verification Code\n\nYour verification code is: {code}"
        server.sendmail(sender_email, email, message)

# Hashing function for password security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration function
def register():
    email = st.text_input("Enter your email:")
    if email in USER_DATABASE:
        st.error("This email is already registered.")
        return
    if email not in AUTHORIZED_EMAILS:
        st.error("You are not authorized to create an account.")
        return
    
    if st.button("Send Verification Code"):
        code = random.randint(100000, 999999)
        VERIFICATION_CODES[email] = code
        send_verification_email(email, code)
        st.session_state["verifying"] = True
        st.session_state["email"] = email
        st.rerun()
    
    if "verifying" in st.session_state:
        verification_code = st.text_input("Enter the verification code sent to your email:")
        if st.button("Verify Code"):
            if verification_code and int(verification_code) == VERIFICATION_CODES.get(email, 0):
                st.session_state["verified"] = True
                st.rerun()
            else:
                st.error("Invalid verification code.")
    
    if "verified" in st.session_state:
        password = st.text_input("Create a Password:", type="password")
        if st.button("Register"):
            USER_DATABASE[email] = hash_password(password)
            st.success("Registration successful! You can now log in.")
            del st.session_state["verified"]
            del st.session_state["verifying"]

# User login function
def login():
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        if email in USER_DATABASE and USER_DATABASE[email] == hash_password(password):
            st.session_state["authenticated"] = True
            st.session_state["user_email"] = email
            st.rerun()
        else:
            st.error("Invalid email or password.")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    choice = st.radio("Select an option", ["Login", "Register"])
    if choice == "Register":
        register()
    else:
        login()
else:
    st.title("UofA Phoenix Family Medicine Residents Wiki")
    st.sidebar.write(f"Logged in as: {st.session_state['user_email']}")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Home", "PGY-1", "PGY-2", "PGY-3"])
    
    with tab1:
        st.header("Welcome to UofA Phoenix Family Medicine Residents Wiki")
        st.write("A comprehensive resource for all family medicine residents.")
    
    with tab2:
        st.header("PGY-1 (Intern Year) Rotations")
        with st.expander("Family Medicine Core Orientation"):
            st.write("An introduction to the fundamentals of family medicine, focusing on patient-centered, evidence-based care.")
        with st.expander("Family Medicine Patient-Centered Medical Home Ambulatory"):
            st.write("Experience in outpatient care emphasizing the patient-centered medical home model, focusing on continuity of care.")
        with st.expander("Family Medicine Inpatient at Banner University Medical Center"):
            st.write("Inpatient care experience managing a diverse patient population with various medical conditions.")
    
    with tab3:
        st.header("PGY-2 (Second Year) Rotations")
        with st.expander("Family Medicine Inpatient"):
            st.write("Advanced inpatient care responsibilities, leading teams, and managing complex medical cases.")
        with st.expander("Family Medicine Ambulatory Care"):
            st.write("Continued experience in outpatient settings, focusing on chronic disease management and preventive care.")
        with st.expander("Cardiology"):
            st.write("Training in the diagnosis and management of cardiovascular diseases, including inpatient and outpatient settings.")
    
    with tab4:
        st.header("PGY-3 (Third Year) Rotations")
        with st.expander("Family Medicine Inpatient"):
            st.write("Leadership role in inpatient teams, mentoring junior residents, and managing complex cases.")
        with st.expander("Family Medicine Ambulatory Care"):
            st.write("Advanced outpatient care, focusing on refining clinical skills, patient communication, and efficient practice management.")
        with st.expander("Practice Management"):
            st.write("Training in the business aspects of medicine, including billing, coding, quality improvement, and leadership skills.")
