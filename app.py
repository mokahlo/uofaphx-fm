import streamlit as st
import os
import auth  # Import authentication module

# Configure Page
st.set_page_config(page_title="Residency Rotations", page_icon="favicon.png", layout="wide")

# Define rotation folders for each residency year
ROTATIONS_FOLDER = "rotations"
YEARS = ["PGY-1", "PGY-2", "PGY-3", "Electives"]

# Check authentication before displaying content
if not st.session_state["authenticated"]:
    auth.login()  # ✅ Call login function
else:
    # Sidebar Navigation: Residency Years
    st.sidebar.title("Residency Years")
    selected_year = st.sidebar.radio("Select a Residency Year:", YEARS)

    # ✅ Fix: Adjust Title Display for Electives
    if selected_year == "Electives":
        st.title("Electives")  # ✅ Show just "Electives"
    else:
        st.title(f"Residency Year: {selected_year}")  # ✅ Keep format for PGY-1, PGY-2, PGY-3

    # Get list of available rotations (text files) for the selected year
    year_folder_path = os.path.join(ROTATIONS_FOLDER, selected_year)
    if os.path.exists(year_folder_path):
        rotation_files = [f for f in os.listdir(year_folder_path) if f.endswith(".txt")]
        rotation_names = [os.path.splitext(f)[0].replace("_", " ") for f in rotation_files]
    else:
        rotation_files = []
        rotation_names = []

    # Display Tabs for Rotations in the Selected Residency Year or Electives
    if rotation_files:
        selected_rotation = st.tabs(rotation_names)  # Create Tabs for each rotation
        
        for i, file_name in enumerate(rotation_files):
            with selected_rotation[i]:
                file_path = os.path.join(year_folder_path, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    rotation_content = file.read()
                st.header(os.path.splitext(file_name)[0].replace("_", " "))  # Format title
                st.markdown(rotation_content)  # Display file content as formatted text
    else:
        st.warning(f"No rotations found for {selected_year}. Please check the folder structure.")
