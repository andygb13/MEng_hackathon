import streamlit as st
import csv
import os

# Dictionary to store user information (for demonstration purposes)
user_info = {}
signup_completed = False

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

def share_experience():
    st.title("Share Your Experience")

    lock_button = st.button("🔒 Lock (Private)")
    post_button = st.button("📬 Post to Forum")

    # Check the clicked button
    if lock_button:
        # # Insert the locked experience into the database
        # cursor.execute("INSERT INTO experiences (content, posted) VALUES (%s, %s)", (experience, False))
        # conn.commit()
        # st.info("Your experience is private and saved in your history.")
        pass

    elif post_button:
        # Insert the experience into the database if the user chooses to post
        # cursor.execute("INSERT INTO experiences (content, posted) VALUES (%s, %s)", (experience, True))
        # conn.commit()
        # st.success("Your experience has been posted to the forum!")   
        pass

# Main function to control navigation between pages
def main():
    st.sidebar.title("Navigation")
    page_options = ["Register", "Log Emotions", "Check Resources", "Feed", "Log Journal", "Experience"]
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
    elif selected_page == "Experience":
        share_experience()    

# Function to render register page
def render_register():
    global signup_completed

    st.title("Sign Up")
    name = st.text_input("Name")
    occupation = st.text_input("Occupation")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    licence = st.text_input("Licence #")
    if st.button("Sign Up"):
        if password == confirm_password:
            # Store user information in a dictionary
            user_info = {
                'Name': name,
                'Occupation': occupation,
                'Email': email,
                'Password': password,
                'Licence': licence
            }

            # Write user information to CSV file
            with open('user_info.csv', 'a', newline='') as csvfile:
                fieldnames = ['Name', 'Occupation', 'Email', 'Password', 'Licence']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header if file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()

                # Write user data to CSV file
                writer.writerow(user_info)

            st.success("Sign up successful! Please proceed to login.")
            signup_completed = True
            # Redirect to waiver page
            render_waiver()
        else:
            st.error("Passwords do not match. Please try again.")

# Function to render waiver page
def render_waiver():
    st.title("Waiver Page")
    st.write("Please read and agree to the terms below:")

    # Display waiver text
    waiver_text = """
    As a user of this mental health application tailored for nurses, I acknowledge the following:
    
    1. The mental health app provides resources and tools designed to support my mental well-being as a nurse.
    
    2. I understand that the app does not substitute professional medical advice, diagnosis, or treatment.
    
    3. Any information shared or discussions held within the app are strictly confidential and must not be shared outside the app.
    
    4. I agree to take full responsibility for any actions taken or decisions made based on the information provided by the app.
    
    5. I acknowledge that participation in any activities or discussions within the app is voluntary, and I have the right to withdraw at any time.
    
    6. I understand that the app may collect anonymized data for research and improvement purposes, ensuring my privacy is maintained.
    
    By checking the box below, I confirm that I have read, understood, and agree to abide by the terms stated above. I acknowledge that failure to comply with these terms may result in the termination of my access to the app.
    """
    st.write(waiver_text)

    # Checkbox for agreement
    agreed = st.checkbox("I agree to the terms stated above.")

    if agreed:
        st.write("Thank you for agreeing to the terms.")
        # Uncomment line below to render the main page once the waiver has been successfully signed.
        # render_mainpage()


if __name__ == "__main__":
    main()
