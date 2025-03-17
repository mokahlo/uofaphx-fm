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
        st.write("**Duration:** 1 month")
        st.write("An introduction to the fundamentals of family medicine, focusing on patient-centered, evidence-based care. Residents become familiar with the residency program, faculty, and clinical settings.")
    with st.expander("Family Medicine Patient-Centered Medical Home Ambulatory"):
        st.write("**Duration:** 1 month")
        st.write("Experience in outpatient care emphasizing the patient-centered medical home model, focusing on continuity of care, preventive medicine, and chronic disease management.")
    with st.expander("Family Medicine Inpatient at Banner University Medical Center"):
        st.write("**Duration:** 6 weeks")
        st.write("Inpatient care experience managing a diverse patient population with various medical conditions, working closely with multidisciplinary teams.")
    with st.expander("Pediatric Inpatient at Phoenix Children's Hospital"):
        st.write("**Duration:** 1 month")
        st.write("Exposure to pediatric inpatient care, managing common and complex pediatric illnesses in a hospital setting.")
    with st.expander("Pediatric Outpatient at Valleywise Hospital"):
        st.write("**Duration:** 1 month")
        st.write("Experience in outpatient pediatric care, focusing on preventive health, growth and development assessments, and common pediatric illnesses.")
    with st.expander("Newborn Care at Valleywise Hospital"):
        st.write("**Duration:** 1 month")
        st.write("Care for newborns, including routine assessments, management of common neonatal conditions, and parent education.")
    with st.expander("General Surgery at Banner – University Medical Center Phoenix"):
        st.write("**Duration:** 1 month")
        st.write("Exposure to general surgical procedures, preoperative and postoperative care, and participation in surgical rounds.")
    with st.expander("Labor & Delivery at Banner – University Medical Center Phoenix"):
        st.write("**Duration:** 1 month")
        st.write("Hands-on experience in labor and delivery, managing normal and high-risk pregnancies, and performing deliveries under supervision.")
    with st.expander("Obstetrics Prenatal Clinic"):
        st.write("**Duration:** 1 month")
        st.write("Outpatient prenatal care, including routine check-ups, prenatal counseling, and management of common pregnancy-related conditions.")

with tab3:
    st.header("PGY-2 (Second Year) Rotations")
    with st.expander("Family Medicine Inpatient"):
        st.write("**Duration:** 6 weeks")
        st.write("Advanced inpatient care responsibilities, leading teams, and managing complex medical cases.")
    with st.expander("Family Medicine Ambulatory Care"):
        st.write("**Duration:** 1 month")
        st.write("Continued experience in outpatient settings, focusing on chronic disease management, preventive care, and patient education.")
    with st.expander("Cardiology"):
        st.write("**Duration:** 1 month")
        st.write("Training in the diagnosis and management of cardiovascular diseases, including inpatient and outpatient settings.")
    with st.expander("Community Medicine"):
        st.write("**Duration:** 1 month")
        st.write("Engagement with community health initiatives, public health projects, and understanding social determinants of health.")
    with st.expander("Geriatrics"):
        st.write("**Duration:** 1 month")
        st.write("Care for elderly patients, focusing on geriatric syndromes, polypharmacy, and functional assessments.")
    with st.expander("ICU at Banner University Medical Center"):
        st.write("**Duration:** 2 weeks")
        st.write("Critical care experience managing severely ill patients, understanding ventilator management, and participating in multidisciplinary rounds.")
    with st.expander("Pediatric Emergency Medicine at Phoenix Children's Hospital"):
        st.write("**Duration:** 1 month")
        st.write("Exposure to acute pediatric emergencies, trauma care, and rapid decision-making skills.")
    with st.expander("Dermatology"):
        st.write("**Duration:** 2 weeks")
        st.write("Diagnosis and management of common dermatologic conditions in outpatient settings.")
    with st.expander("Musculoskeletal/Sports Medicine"):
        st.write("**Duration:** 1 month")
        st.write("Evaluation and management of musculoskeletal injuries, sports-related conditions, and rehabilitation strategies.")
    with st.expander("Emergency Medicine"):
        st.write("**Duration:** 1 month")
        st.write("Experience in adult emergency care, managing acute medical conditions, and participating in resuscitation efforts.")
    with st.expander("Radiology"):
        st.write("**Duration:** 2 weeks")
        st.write("Understanding imaging modalities, interpreting common radiologic studies, and collaborating with radiologists.")
    with st.expander("Electives"):
        st.write("**Duration:** 2 months")
        st.write("Opportunities to explore areas of interest or focus on specific skills relevant to future practice.")

with tab4:
    st.header("PGY-3 (Third Year) Rotations")
    with st.expander("Family Medicine Inpatient"):
        st.write("**Duration:** 6 weeks")
        st.write("Leadership role in inpatient teams, mentoring junior residents, and managing complex cases.")
    with st.expander("Family Medicine Ambulatory Care"):
        st.write("**Duration:** 1 month")
        st.write("Advanced outpatient care, focusing on refining clinical skills, patient communication, and efficient practice management.")
    with st.expander("Practice Management"):
        st.write("**Duration:** 1 month")
        st.write("Training in the business aspects of medicine, including billing, coding, quality improvement, and leadership skills.")
    with st.expander("Pediatrics"):
        st.write("**Duration:** 1 month")
        st.write("Comprehensive pediatric care, integrating previous experiences to manage a wide range of pediatric conditions.")
    with st.expander("Gynecology"):
        st.write("**Duration:** 1 month")
        st.write("Experience in women's health, including routine gynecologic care, contraceptive management, and common gynecologic procedures.")
    with st.expander("Behavioral Health"):
        st.write("**Duration:** 1 month")
        st.write("Training in the recognition and management of common mental health conditions, counseling techniques, and collaboration with mental health professionals.")
    with st.expander("Electives"):
        st.write("**Duration:** 2 months")
        st.write("Further opportunities to tailor training to specific interests or career goals, including potential research projects or specialized clinical experiences.")
