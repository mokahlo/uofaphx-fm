import streamlit as st
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
import os

st.set_page_config(page_title="UofA Phoenix Family Medicine Residents Wiki", layout="wide")

# Google OAuth Setup
CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8501"
AUTHORIZED_EMAILS = ["alloweduser1@example.com", "alloweduser2@example.com"]

flow = Flow.from_client_secrets_file(
    "client_secret.json",  # You must download this from Google API Console
    scopes=["openid", "email", "profile"],
    redirect_uri=REDIRECT_URI
)

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def authenticate():
    auth_url, _ = flow.authorization_url(prompt="consent")
    st.markdown(f"[Login with Google]({auth_url})")
    
    code = st.text_input("Enter the authentication code from Google:")
    if st.button("Verify"):
        try:
            flow.fetch_token(code=code)
            credentials = flow.credentials
            request = google.auth.transport.requests.Request()
            id_info = id_token.verify_oauth2_token(credentials.id_token, request, CLIENT_ID)
            
            user_email = id_info.get("email")
            if user_email in AUTHORIZED_EMAILS:
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = user_email
                st.rerun()
            else:
                st.error("Access Denied: Unauthorized Email")
        except Exception as e:
            st.error("Authentication Failed")

if not st.session_state["authenticated"]:
    authenticate()
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
