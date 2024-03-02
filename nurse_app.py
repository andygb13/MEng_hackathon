import streamlit as st
import csv
import os
import mysql.connector

# Dictionary to store user information (for demonstration purposes)
user_info = {}

# Function to render register page
# to do: Add functionalities for existing users
def render_register():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if username in user_info:
            st.error("Username already exists. Please choose a different one.")
        else:
            user_info[username] = password
            st.success("Registration successful! Please proceed to login.")

# Function to log emotions
def log_emotions():
    st.title("Log Emotions")
    # Implement logic to log emotions here

# Function to check mental health resources
def check_resources():
    st.title("Mental Health Resources")
    # Implement logic to display mental health resources here

# Function to display feed of user experiences
def display_feed():
    st.title("User Experiences Feed")
    # Implement logic to display user experiences feed here

# Function to prompt user to write a journal entry
# Function to prompt user to write a journal entry
def log_journal():
    st.title("Log Emotions & Reflective Journal Entry")
    
    st.write("Select what contributed to your emotions:")
    # Updated options for contributing factors
    options = [
        "Conflict with a coworker/patient/family member",
        "Medication/procedure Error",
        "Imposter syndrome",
        "Code Event",
        "Patient death",
        "Verbal or physical abuse from patient/family members",
        "Tiredness/ exhaustion",
        "High patient:nurse ratio",
        "Poor patient outcomes",
        "Moral/Ethical distress",
        "Lack of Sleep",
        "Missed Breaks",
        "Unsafe assignments",
        "Staff shortages",
        "Conflict with management"
    ]
    selected_options = st.multiselect("Select Option(s)", options)
    
    st.write("Reflect on the selected emotion and write a journal entry below:")
    journal_entry = st.text_area("Journal Entry", height=200)
    
    skip_entry = st.checkbox("Skip entering journal entry")
    if st.button("Submit"):
        if not skip_entry:
            # Store journal entry and selected emotions in a CSV file
            file_path = "journal_entries.csv"
            header = ["Emotions", "Journal Entry"]
            new_entry = [", ".join(selected_options), journal_entry]
            if not os.path.exists(file_path):
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_entry)
            st.success("Journal entry and emotions logged successfully!")
        else:
            # Store only the selected emotions in a CSV file
            file_path = "journal_entries.csv"
            header = ["Emotions"]
            new_entry = [", ".join(selected_options)]
            if not os.path.exists(file_path):
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_entry)
            st.success("Emotions logged successfully!")

# Main function to control navigation between pages
def main():
    st.sidebar.title("Navigation")
    page_options = ["Register", "Log Emotions", "Check Resources", "Feed", "Log Journal"]
    selected_page = st.sidebar.selectbox("Go to", page_options)

    if selected_page == "Register":
        render_register()
    elif selected_page == "Log Emotions":
        log_emotions()
    elif selected_page == "Check Resources":
        check_resources()
    elif selected_page == "Log Journal":
        log_journal()
    elif selected_page == "Feed":
        display_feed()

if __name__ == "__main__":
    main()
