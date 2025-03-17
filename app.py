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
    with st.expander("Family Medicine Core Orientation"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Family Medicine Patient-Centered Medical Home Ambulatory"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Family Medicine Inpatient at Banner University Medical Center"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Pediatric Inpatient at Phoenix Children's Hospital"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Pediatric Outpatient at Valleywise Hospital"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Newborn Care at Valleywise Hospital"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("General Surgery at Banner – University Medical Center Phoenix"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Labor & Delivery at Banner – University Medical Center Phoenix"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Obstetrics Prenatal Clinic"):
        st.write("[Placeholder text for detailed information]")

with tab3:
    st.header("PGY-2 (Second Year) Rotations")
    with st.expander("Family Medicine Inpatient"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Family Medicine Ambulatory Care"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Cardiology"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Community Medicine"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Geriatrics"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("ICU at Banner University Medical Center"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Pediatric Emergency Medicine at Phoenix Children's Hospital"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Dermatology"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Musculoskeletal/Sports Medicine"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Emergency Medicine"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Radiology"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Electives"):
        st.write("[Placeholder text for detailed information]")

with tab4:
    st.header("PGY-3 (Third Year) Rotations")
    with st.expander("Family Medicine Inpatient"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Family Medicine Ambulatory Care"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Practice Management"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Pediatrics"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Gynecology"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Behavioral Health"):
        st.write("[Placeholder text for detailed information]")
    with st.expander("Electives"):
        st.write("[Placeholder text for detailed information]")
