import streamlit as st
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

# Main function to control navigation between pages
def main():
    st.sidebar.title("Navigation")
    page_options = ["Register", "Log Emotions", "Check Resources", "Feed"]
    selected_page = st.sidebar.selectbox("Go to", page_options)

    if selected_page == "Register":
        render_register()
    elif selected_page == "Log Emotions":
        log_emotions()
    elif selected_page == "Check Resources":
        check_resources()
    elif selected_page == "Feed":
        display_feed()

if __name__ == "__main__":
    main()
