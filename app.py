import streamlit as st
import smtplib
import random
import os

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
    if email not in AUTHORIZED_EMAILS:
        st.error("You are not authorized to log in.")
        return

    if st.button("Send Verification Code"):
        code = random.randint(100000, 999999)
        st.session_state["verification_code"] = code
        st.session_state["email"] = email
        send_verification_email(email, code)
    
    if "verification_code" in st.session_state:
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

# Authentication check
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.title("UofA Phoenix Family Medicine Residents Wiki")
    st.sidebar.write(f"Logged in as: {st.session_state['email']}")
    
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
