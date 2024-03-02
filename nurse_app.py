import streamlit as st
#import mysql.connector

# Dictionary to store user information (for demonstration purposes)
user_info = {}
state = "hello"

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

# Function to log emotions
def recommended_exercises(emotions_list):
    # Implement logic to recommended exercises here

    placeholder = st.empty()

    recommend_list = []
    

    if "Anxious" or "Powerless" or "Overwhelmed" or "Bored" or "Jealous" or "Annoyed" in emotions_list:
        recommend_list.append("Box Breathing Exercise")
    if "Lonely" or "Hurt" or "Disappointed" or "Ashamed" or "Excluded" or "Guilty" in emotions_list:
        recommend_list.append("Mindfulness Audio Recording")
    if "Scared" in emotions_list:
        recommend_list.append("Scared")

    # Default
    if st.session_state.page == 0:
        i=0
        with placeholder.container():
            st.title("We Recommend")
        for exercise in recommend_list:
            i+=1
            with st.chat_message("user"):
                st.write(exercise)
                st.button('Go to Exercise', key=i, on_click=nextpage) 
    # Box Breathing 
    elif st.session_state.page == 1:
        multi = '''Before starting the breathing pattern, adopt a comfortable sitting position and place the tip of the tongue on the tissue right behind the top front teeth.To use the 4-7-8 technique, focus on the following breathing pattern:

●	emptying the lungs of air

●	breathing in quietly through the nose for 4 seconds

●	holding the breath for a count of 7 seconds

●	exhaling forcefully through the mouth, pursing the lips, and making a “whoosh” sound for 8 seconds

●	repeating the cycle up to 4 times
'''
        with placeholder.container():
            st.markdown(multi)
    
def nextpage(): st.session_state.page = 1

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
    if "page" not in st.session_state:
        st.session_state.page = 0

    if selected_page == "Register":
        render_register()
    elif selected_page == "Log Emotions":
        log_emotions()
    elif selected_page == "Check Resources":
        check_resources()
    elif selected_page == "Feed":
        display_feed()

    st.session_state.page = 0

if __name__ == "__main__":
    main()
