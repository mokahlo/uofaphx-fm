import streamlit as st

st.set_page_config(page_title="UofA Phoenix Family Medicine Residents Wiki", layout="wide")

st.title("UofA Phoenix Family Medicine Residents Wiki")

# Create Tabs for Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Home", "PGY-1", "PGY-2", "PGY-3"])

with tab1:
    st.header("Welcome to UofA Phoenix Family Medicine Residents Wiki")
    st.write("A comprehensive resource for all family medicine residents.")

with tab2:
    st.header("PGY-1 (Intern Year) Rotations")
    st.write("- Family Medicine Core Orientation")
    st.write("- Family Medicine Patient-Centered Medical Home Ambulatory")
    st.write("- Family Medicine Inpatient at Banner University Medical Center")
    st.write("- Pediatric Inpatient at Phoenix Children's Hospital")
    st.write("- Pediatric Outpatient at Valleywise Hospital")
    st.write("- Newborn Care at Valleywise Hospital")
    st.write("- General Surgery at Banner – University Medical Center Phoenix")
    st.write("- Labor & Delivery at Banner – University Medical Center Phoenix")
    st.write("- Obstetrics Prenatal Clinic")

with tab3:
    st.header("PGY-2 (Second Year) Rotations")
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

with tab4:
    st.header("PGY-3 (Third Year) Rotations")
    st.write("- Family Medicine Inpatient")
    st.write("- Family Medicine Ambulatory Care")
    st.write("- Practice Management")
    st.write("- Pediatrics")
    st.write("- Gynecology")
    st.write("- Behavioral Health")
    st.write("- Electives")
