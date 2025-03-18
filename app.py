import streamlit as st
import os

# Configure Page
st.set_page_config(page_title="Residency Rotations", page_icon="favicon.png", layout="wide")

# Sidebar Navigation: Residency Years
st.sidebar.title("Residency Years")
years = ["PGY-1", "PGY-2", "PGY-3"]
selected_year = st.sidebar.radio("Select a Residency Year:", years)

# Define folder where rotation files are stored
ROTATIONS_FOLDER = "rotations"

def load_rotation_details(rotation_name):
    """Loads rotation details from a text file"""
    file_path = os.path.join(ROTATIONS_FOLDER, f"{rotation_name}.txt")
    
    if not os.path.exists(file_path):
        return {"title": rotation_name, "content": "No information available."}

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return {"title": rotation_name.replace("_", " "), "content": content}

# Available Rotations for Each Residency Year
rotations_per_year = {
    "PGY-1": ["General_Surgery", "Obstetrics_and_Gynecology"],
    "PGY-2": ["Internal_Medicine"],
    "PGY-3": ["Emergency_Medicine"]
}

# Display Tabs for Rotations in the Selected Residency Year
st.title(f"Residency Year: {selected_year}")

if selected_year in rotations_per_year:
    rotation_names = rotations_per_year[selected_year]
    selected_rotation = st.tabs(rotation_names)  # Create Tabs for each rotation
    
    for i, rotation_name in enumerate(rotation_names):
        with selected_rotation[i]:
            rotation_info = load_rotation_details(rotation_name)
            st.header(rotation_info["title"])
            st.markdown(rotation_info["content"])  # Display as formatted text
