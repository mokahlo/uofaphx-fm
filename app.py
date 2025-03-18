import streamlit as st
import os
import auth  # Import authentication module

# ✅ Ensure session state variables are initialized to avoid KeyError
st.session_state.setdefault("authenticated", False)

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

    # ✅ Adjust Title Display for Electives
    if selected_year == "Electives":
        st.title("Electives")
    else:
        st.title(f"Residency Year: {selected_year}")

    # Function to read tab name & content from a .txt file
    def load_rotation_details(file_path):
        """Reads the content of a rotation file and extracts the title"""
        if not os.path.exists(file_path):
            return "Unknown Rotation", "No information available."

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Extract title from the first non-empty line
        title = "Unknown Rotation"
        content_start = 0
        for i, line in enumerate(lines):
            line = line.strip()
            if line:  # Skip empty lines
                title = line.replace("#", "").strip()  # Remove markdown header #
                content_start = i + 1
                break

        # Read the rest of the file as content
        content = "".join(lines[content_start:]).strip()
        return title, content

    # Get list of available rotations (text files) for the selected year
    year_folder_path = os.path.join(ROTATIONS_FOLDER, selected_year)
    if os.path.exists(year_folder_path):
        rotation_files = [f for f in os.listdir(year_folder_path) if f.endswith(".txt")]

        # ✅ Sort rotation files based on numerical prefix
        rotation_files.sort(key=lambda x: int(x.split("_")[0]))

        rotation_details = [load_rotation_details(os.path.join(year_folder_path, f)) for f in rotation_files]
        tab_names = [details[0] for details in rotation_details]  # Extract titles as tab names
    else:
        rotation_files = []
        rotation_details = []
        tab_names = []

    # Display Tabs for Rotations in the Selected Residency Year or Electives
    if rotation_files:
        selected_rotation = st.tabs(tab_names)  # Create tabs from extracted titles

        for i, (tab_name, content) in enumerate(rotation_details):
            with selected_rotation[i]:
                st.markdown(content)  # ✅ Display only content (no redundant title)
    else:
        st.warning(f"No rotations found for {selected_year}. Please check the folder structure.")
