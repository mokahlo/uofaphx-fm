import streamlit as st
import smtplib
import random
import os

#Favcon Image
st.set_page_config(
    page_title="Residency Rotations",
    page_icon="favicon.png"  # Updated path

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
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "An introduction to the fundamentals of family medicine, focusing on patient-centered, evidence-based care."
    },
    "Family Medicine Patient-Centered Medical Home Ambulatory": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Outpatient Clinics",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Experience in outpatient care emphasizing the patient-centered medical home model, focusing on continuity of care."
    },
    "Family Medicine Inpatient at Banner University Medical Center": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Inpatient care experience managing a diverse patient population with various medical conditions."
    },
    "Pediatric Inpatient at Phoenix Children's Hospital": {
        "duration": "1 month",
        "location": "Phoenix Children's Hospital",
        "address": "1919 E. Thomas Rd., Phoenix, AZ 85016",
        "parking": "Parking garage available; validation provided for residents.",
        "description": "Comprehensive inpatient pediatric care, managing a wide range of childhood illnesses and conditions."
    },
    "Pediatric Outpatient at Valleywise Health": {
        "duration": "1 month",
        "location": "Valleywise Health Medical Center",
        "address": "2601 E. Roosevelt St., Phoenix, AZ 85008",
        "parking": "On-site parking available; permits provided.",
        "description": "Outpatient pediatric care focusing on preventive medicine and common pediatric conditions."
    },
    "Newborn Care at Valleywise Health": {
        "duration": "1 month",
        "location": "Valleywise Health Medical Center",
        "address": "2601 E. Roosevelt St., Phoenix, AZ 85008",
        "parking": "On-site parking available; permits provided.",
        "description": "Care for newborns, including routine examinations and management of common neonatal issues."
    },
    "General Surgery at Banner – University Medical Center Phoenix": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Exposure to general surgical procedures and perioperative patient management."
    },
    "Labor & Delivery at Banner – University Medical Center Phoenix": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Hands-on experience in managing labor, delivery, and postpartum care."
    },
    "Obstetrics Prenatal Clinic": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Outpatient Clinics",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Prenatal care focusing on routine examinations and management of common prenatal conditions."
    }
}

pgy2_rotations = {
    "Family Medicine Inpatient": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Advanced inpatient care responsibilities, leading teams, and managing complex medical cases."
    },
    "Family Medicine Ambulatory Care": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Outpatient Clinics",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Continued experience in outpatient settings, focusing on chronic disease management and preventive care."
    },
    "Cardiology": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Cardiology Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Training in the diagnosis and management of cardiovascular diseases, including inpatient and outpatient settings."
    },
    "Community Medicine": {
        "duration": "1 month",
        "location": "Various Community Health Centers in Phoenix",
        "address": "Varies by specific health center.",
        "parking": "Parking availability varies by location.",
        "description": "Engagement with community health initiatives and understanding public health principles."
    },
    "Geriatrics": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Geriatrics Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Focused on the care of elderly patients, addressing complex medical and psychosocial issues."
    },
    "ICU": {
        "duration": "2 weeks",
        "location": "Banner – University Medical Center Phoenix Intensive Care Unit",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Experience in managing critically ill patients in the intensive care setting."
    },
    "Pediatric Emergency Medicine": {
        "duration": "1 month",
        "location": "Phoenix Children's Hospital",
        "address": "1919 E. Thomas Rd., Phoenix, AZ 85016",
        "parking": "Parking garage available; validation provided for residents.",
        "description": "Training in pediatric emergency care, managing acute illnesses and injuries in children."
    },
    "Dermatology": {
        "duration": "2 weeks",
        "location": "Banner – University Medical Center Phoenix Dermatology Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Diagnosis and management of common dermatologic conditions."
    },
    "Musculoskeletal/Sports Medicine": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Sports Medicine Clinic",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Training in the management of musculoskeletal injuries and conditions, with a focus on sports-related issues."
    },
    "Emergency Medicine": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Emergency Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Exposure to a wide range of acute medical conditions in the emergency setting."
    },
    "Radiology": {
        "duration": "2 weeks",
        "location": "Banner – University Medical Center Phoenix Radiology Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Understanding imaging modalities and their application in diagnosis."
    },
    "Electives": {
        "duration": "2 months",
        "location": "Varies based on elective choice",
        "address": "Varies by elective selection.",
        "parking": "Varies by location.",
        "description": "Opportunities to tailor training to specific interests or career goals, including potential research projects or specialized clinical experiences."
    }
}

pgy3_rotations = {
    "Family Medicine Inpatient": {
        "duration": "6 weeks",
        "location": "Banner – University Medical Center Phoenix",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Leadership role in inpatient teams, mentoring junior residents, and managing complex cases."
    },
    "Family Medicine Ambulatory Care": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Outpatient Clinics",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Advanced outpatient care, focusing on refining clinical skills, patient communication, and efficient practice management."
    },
    "Gynecology": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Gynecology Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Comprehensive training in women's health, including routine gynecological care and management of common conditions."
    },
    "Behavioral Health/Addiction": {
        "duration": "2 months",
        "location": "Banner – University Medical Center Phoenix Behavioral Health Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Focused on mental health care, substance use disorders, and integrating behavioral health into primary care."
    },
    "Musculoskeletal/Orthopedics": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Orthopedics Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Training in diagnosing and managing musculoskeletal conditions, including joint injections and fracture care."
    },
    "Pediatrics": {
        "duration": "1 month",
        "location": "Phoenix Children's Hospital",
        "address": "1919 E. Thomas Rd., Phoenix, AZ 85016",
        "parking": "Parking garage available; validation provided for residents.",
        "description": "Comprehensive pediatric care, including preventive health, acute illnesses, and chronic condition management."
    },
    "Urology": {
        "duration": "2 weeks",
        "location": "Banner – University Medical Center Phoenix Urology Department",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Exposure to common urological conditions and procedures relevant to family medicine practice."
    },
    "Electives": {
        "duration": "4 months",
        "location": "Varies based on elective choice",
        "address": "Varies by elective selection.",
        "parking": "Varies by location.",
        "description": "Opportunities to tailor training to specific interests or career goals, including potential research projects or specialized clinical experiences."
    }
}

# Define the elective rotations
elective_rotations = {
    "Sports Medicine": {
        "duration": "1 month",
        "location": "Banner – University Medical Center Phoenix Sports Medicine Clinic",
        "address": "1111 E. McDowell Rd., Phoenix, AZ 85006",
        "parking": "Free parking available on-site for residents.",
        "description": "Focused training in the diagnosis and management of sports-related injuries and conditions."
    },
    "Rural Health": {
        "duration": "1 month",
        "location": "Various rural health centers across Arizona",
        "address": "Varies by assigned location",
        "parking": "Parking availability varies by location.",
        "description": "Experience in providing comprehensive healthcare in rural and underserved communities."
    },
    "Integrative Medicine": {
        "duration": "1 month",
        "location": "Andrew Weil Center for Integrative Medicine",
        "address": "655 N. Alvernon Way, Suite 120, Tucson, AZ 85711",
        "parking": "Free parking available on-site.",
        "description": "Training in holistic approaches to patient care, combining conventional and alternative therapies."
    },
    "Research": {
        "duration": "1 month",
        "location": "University of Arizona College of Medicine – Phoenix",
        "address": "475 N. 5th Street, Phoenix, AZ 85004",
        "parking": "Parking garage available; validation provided for residents.",
        "description": "Opportunities to engage in clinical or academic research projects under faculty supervision."
    },
    "Global Health": {
        "duration": "1 month",
        "location": "Various international healthcare settings",
        "address": "Varies by assigned location",
        "parking": "Not applicable.",
        "description": "Exposure to healthcare delivery and public health initiatives in international settings."
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
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "PGY-1", "PGY-2", "PGY-3", "Electives"])
    
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

    with tab5:
        st.header("Elective Rotations")
        display_rotation_details(elective_rotations)
