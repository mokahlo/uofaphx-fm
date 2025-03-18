import streamlit as st
import os
import auth  # Import authentication module

# ✅ Ensure session state variables are initialized to avoid KeyError
st.session_state.setdefault("authenticated", False)
st.session_state.setdefault("tab_index", 0)  # Track tab index for scrolling

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
        st.title(f"{selected_year}")

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

        # ✅ Enhanced Sorting: Extract numeric prefix safely
        def extract_number(filename):
            """Extracts the numeric prefix from a filename, defaults to a high number if missing"""
            parts = filename.split("_", 1)  # Split at the first underscore
            return int(parts[0]) if parts[0].isdigit() else 999  # Default to 999 if no number

        rotation_files.sort(key=extract_number)

        rotation_details = [load_rotation_details(os.path.join(year_folder_path, f)) for f in rotation_files]
        tab_names = [details[0] for details in rotation_details]  # Extract titles as tab names
    else:
        rotation_files = []
        rotation_details = []
        tab_names = []

    # Display Tabs for Rotations in the Selected Residency Year or Electives
    if rotation_files:
        # ✅ Create left and right navigation buttons for scrolling
        col1, col2, col3 = st.columns([1, 8, 1])

        with col1:
            if st.button("⬅", disabled=st.session_state.tab_index == 0):
                st.session_state.tab_index = max(0, st.session_state.tab_index - 1)

        with col3:
            if st.button("➡", disabled=st.session_state.tab_index + 1 >= len(tab_names)):
                st.session_state.tab_index = min(len(tab_names) - 1, st.session_state.tab_index + 1)

        # ✅ Display only the currently selected tab
        selected_tab = tab_names[st.session_state.tab_index]
        st.subheader(selected_tab)
        st.markdown(rotation_details[st.session_state.tab_index][1])  # Show content for the selected tab

    else:
        st.warning(f"No rotations found for {selected_year}. Please check the folder structure.")
