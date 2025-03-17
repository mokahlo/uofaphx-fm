import streamlit as st

def main():
    st.set_page_config(page_title="UofA Phoenix Family Medicine Residents Wiki", layout="wide")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Rotations Guide"])
    
    if page == "Home":
        st.title("Welcome to UofA Phoenix Family Medicine Residents Wiki")
        st.write("A comprehensive resource for all family medicine residents.")
    
    elif page == "Rotations Guide":
        st.title("Rotations Guide")
        st.subheader("Inpatient Medicine")
        st.write("Details about inpatient responsibilities and expectations.")
        st.subheader("OB/GYN")
        st.write("Important protocols and procedures for OB/GYN rotation.")
        st.subheader("Pediatrics")
        st.write("Guidelines for handling pediatric cases.")
    
if __name__ == "__main__":
    main()
