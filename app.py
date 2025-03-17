import streamlit as st

st.set_page_config(page_title="UofA Phoenix Family Medicine Residents Wiki", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Home", "PGY-1", "PGY-2", "PGY-3"])

if page == "Home":
    st.title("Welcome to UofA Phoenix Family Medicine Residents Wiki")
    st.write("A comprehensive resource for all family medicine residents.")

elif page == "PGY-1":
    st.title("PGY-1 (Intern Year) Rotations")
    st.write("- Family Medicine Core Orientation")
    st.write("- Family Medicine Patient-Centered Medical Home Ambulatory")
    st.write("- Family Medicine Inpatient at Banner University Medical Center")
    st.write("- Pediatric Inpatient at Phoenix Children's Hospital")
    st.write("- Pediatric Outpatient at Valleywise Hospital")
    st.write("- Newborn Care at Valleywise Hospital")
    st.write("- General Surgery at Banner – University Medical Center Phoenix")
    st.write("- Labor & Delivery at Banner – University Medical Center Phoenix")
    st.write("- Obstetrics Prenatal Clinic")

elif page == "PGY-2":
    st.title("PGY-2 (Second Year) Rotations")
    st.write("- Family Medicine Inpatient")
    st.write("- Family Medicine Ambulatory Care")
    st.write("- Cardiology")
    st.write("- Community Medicine")
    st.write("- Geriatrics")
    st.write("- ICU at Banner University Medical Center")
    st.write("- Pediatric Emergency Medicine at Phoenix Children's Hospital")
    st.write("- Dermatology")
    st.write("- Musculoskeletal/Sports Medicine")
    st.write("- Emergency Medicine")
    st.write("- Radiology")
    st.write("- Electives")

elif page == "PGY-3":
    st.title("PGY-3 (Third Year) Rotations")
    st.write("- Family Medicine Inpatient")
    st.write("- Family Medicine Ambulatory Care")
    st.write("- Practice Management")
    st.write("- Pediatrics")
    st.write("- Gynecology")
    st.write("- Behavioral Health")
    st.write("- Electives")
