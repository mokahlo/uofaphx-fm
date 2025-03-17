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

# Function to display rotation details
def display_rotation_details(rotations):
    for rotation, details in rotations.items():
        with st.expander(rotation):
            st.write(f"**Duration:** {details['duration']}")
            st.write(f"**Location:** {details['location']}")
            st.write(f"**Address:** {details['address']}")
            st.write(f"**Parking Information:** {details['parking']}")
            st.write(f"**Description:** {details['description']}")

# Rotation details for each postgraduate year
pgy1_rotations = {
    "Family Medicine Core Orientation": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix",
        "address" : "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "An introduction to the fundamentals of family medicine, focusing on patient-centered, evidence-based care."
    },
    "Family Medicine Patient-Centered Medical Home Ambulatory": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Outpatient Clinics",
        "parking": "Free parking available on-site for residents.",
        "description": "Experience in outpatient care emphasizing the patient-centered medical home model, focusing on continuity of care."
    },
    "Family Medicine Inpatient at Banner University Medical Center": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "parking": "Free parking available on-site for residents.",
        "description": "Inpatient care experience managing a diverse patient population with various medical conditions."
    }
}

pgy2_rotations = {
    "Family Medicine Inpatient": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "parking": "Free parking available on-site for residents.",
        "description": "Advanced inpatient care responsibilities, leading teams, and managing complex medical cases."
    },
    "Cardiology": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Cardiology Department",
        "parking": "Free parking available on-site for residents.",
        "description": "Training in the diagnosis and management of cardiovascular diseases, including inpatient and outpatient settings."
    },
    "Community Medicine": {
        "duration": "1 month",
        "location": "Community Health Centers in Phoenix",
        "parking": "Parking availability varies by location.",
        "description": "Engagement with community health initiatives and understanding public health principles."
    }
}

pgy3_rotations = {
    "Family Medicine Inpatient": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "parking": "Free parking available on-site for residents.",
        "description": "Leadership role in inpatient teams, mentoring junior residents, and managing complex cases."
    },
    "Practice Management": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix",
        "parking": "Free parking available on-site for residents.",
        "description": "Training in the business aspects of medicine, including billing, coding, quality improvement, and leadership skills."
    },
    "Electives": {
        "duration": "2 months",
        "location": "Varies based on elective choice",
        "parking": "Varies by location.",
        "description": "Further opportunities to tailor training to specific interests or career goals, including potential research projects or specialized clinical experiences."
    }
}

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
        display_rotation_details(pgy1_rotations)

    with tab3:
        st.header("PGY-2 (Second Year) Rotations")
        display_rotation_details(pgy2_rotations)

    with tab4:
        st.header("PGY-3 (Third Year) Rotations")
        display_rotation_details(pgy3_rotations)
