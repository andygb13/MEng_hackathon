import streamlit as st
import base64

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
    
    st.divider()


    st.header("Start With a Breathing Exercise!")
    with st.expander("Breathing Exercise"):
        st.markdown("""
        Before starting the breathing pattern, adopt a comfortable sitting position and place the tip of the tongue on the tissue right behind the top front teeth.

        To use the 4-7-8 technique, focus on the following breathing pattern:
        1. Emptying the lungs of air
        2. Breathing in quietly through the nose for 4 seconds
        3. Holding the breath for a count of 7 seconds
        4. Exhaling forcefully through the mouth, pursing the lips, and making a “whoosh” sound for 8 seconds
        5. Repeating the cycle up to 4 times
        """)
    with st.expander("Box Breathing"):
        st.write("Imagine a box while doing this exercise to help focus your mind. Get settled. Exhale deeply for 4. Hold for 4. Inhale for 4. Hold for 4. Repeat.")


    st.header("Midfulness Audio Recordings")
    st.write("A very basic yet powerful mindfulness meditation practice. The idea is simply to focus your attention on your breathing—to its natural rhythm and flow and the way it feels on each inhale and exhale.")

    anxiety_path = "./assets/anxiety_logo.png"  # Replace this with the URL of your image
    link_url = "https://www.anxietycanada.com/articles/mindfulness-mindful-breathing/" 

    # Format HTML with Markdown
    st.caption("Mindfulness – Mindful Breathing:")
    html_code = f'<a href="{link_url}"><img src="data:image/jpeg;base64,{base64.b64encode(open(anxiety_path, "rb").read()).decode()}" alt="Link to resource"></a>'
    st.markdown(html_code, unsafe_allow_html=True)

    st.write("The body scan is a mindfulness meditation practice involving scanning your body for pain, tension, or anything out of the ordinary. The aim of this exercise is to bring awareness to the physical sensations in different parts of your body, and it can be performed while lying down, sitting, or in other postures. ")

    link_url = "https://www.anxietycanada.com/articles/mindful-body-scan/ "

    # Format HTML with Markdown
    st.caption("Mindfulness – Body Scan:")
    html_code = f'<a href="{link_url}"><img src="data:image/jpeg;base64,{base64.b64encode(open(anxiety_path, "rb").read()).decode()}" alt="Link to resource"></a>'
    st.markdown(html_code, unsafe_allow_html=True)


    st.header("TIPP Skills")
    st.write("This is a super easy skill to use in times of crisis or high emotional states like when you feel overwhelmed and your emotions are going to consume you.")

    anxiety_path = "./assets/embrace_therapy_logo.png"  # Replace this with the URL of your image
    link_url = "https://iembracetherapy.com/distress-tolerance-tipp-skills/#:~:text=TIPP%20is%20a%20dialectical%20Behavioral,breathing%2C%20and%20progressive%20muscle%20relaxation" 

    # Format HTML with Markdown
    st.caption("Distress Tolerance:")
    html_code = f'<a href="{link_url}"><img src="data:image/jpeg;base64,{base64.b64encode(open(anxiety_path, "rb").read()).decode()}" alt="Link to resource"></a>'
    st.markdown(html_code, unsafe_allow_html=True)


    st.header("STOP Tool")
    st.write("The STOP skill consists of the following sequence: Stop, Take a step back, Observe, Proceed mindfully.")
    st.write("Click on each letter to learn more.")
    with st.expander("S"):
        st.write("STOP! When you feel that your emotions seem to be in control, stop! Don’t react. Don’t move a muscle. Just freeze especially those muscles around the mouth. Freezing for a moment helps prevent you from doing what your emotions want you to do (which is to act without thinking). Stay in control. Remember, you are the boss of your emotions. Name the emotion – put a label on it.")
    with st.expander("T"):
        st.write("Take a step back! When you are faced with a difficult situation, it may be hard to think about how to deal with it on the spot. Give yourself some time to calm down and think. Take a step back from the situation. Get unstuck from what is going on. Take a deep breath and continue breathing deeply as long as you need and until you are in control. Do not let your emotions control what you do. It is a rare incident, indeed, wherein we need to make a split-second decision about anything. Hence, it is okay to take our time to decide how to respond.")
    with st.expander("O"):
        st.write("Observe! Observe what is happening around you and within you, who is involved, and what are other people doing or saying. Listen to the Automatic Negative Thoughts (ANTs) that occur…remember those are based on an outdated Belief System that was programmed before you were seven. To make effective choices, it is important NOT to jump to conclusions. Instead, gather the relevant facts so you can understand what is going on and what options are available.")
    with st.expander("P"):
        st.write("Proceed Mindfully! Ask yourself, “What do I want from this situation?” or “What are my goals?” or “What choice might make this situation better or worse?” or “What act will allow for success?” Stay calm, stay in control, and when you have some information and how that may impact your goals, you will be better prepared to deal with the situation effectively. Remember your brain needs time to think all of this through.")


    st.header("Opposite Action Skill")
    st.write("All emotions activate us to respond and the type of activation is biologically wired. The Opposite Action Skill allows us to choose to respond opposite from what our biological response would activate us to do. ")
    with st.expander("Switch it up!"):
        st.markdown("""
            **Anger** gets us ready to attack. It activates us to attack or defend.
                    *Opposite*: show kindness/concern or walk away.

        **Shame** gets us ready to hide. It activates us isolate.
        *Opposite*: raise your head up, give eye contact, shoulders back.

        **Fear** gets us ready to run or hide. It activates us to escape danger.
        *Opposite*: go towards, stay involved in it, build courage.

        **Depression** gets us ready to be inactive. It activates us to avoid contact.
        *Opposite*: get active.

        **Disgust** gets us ready to reject or distance ourselves. It activates us to avoid.
        *Opposite*: push through and get through situation.
                    """)
        

    st.header("ABC Please Skill")
    st.write("The ABC PLEASE skill is about taking good care of ourselves so that we can take care of others. Also, an important component of DBT is to reduce our vulnerability. When we take good care of ourselves, we are less likely to be vulnerable to disease and emotional crisis.")
    with st.expander("A"):
        st.write("Accumulate positive emotions by doing things that are pleasant.")
    with st.expander("B"):
        st.write("Build mastery by doing things we enjoy. Whether it is reading, cooking, cleaning, fixing a car, working a cross word puzzle, or playing a musical instrument. Practice these things to build master and in time we feel competent.")
    with st.expander("C"):
        st.write("Cope Ahead by rehearsing a plan ahead of time so that we can be prepared to cope skillfully.")


    st.header("Sound Meditation")
    st.write("Listen in and use the sounds to help calm the mind.")
    st.caption("10 Minute Crystal Singing Bowl Meditation | Sound Healing For Relaxation & Stress Relief")
    video_url = 'https://www.youtube.com/watch?v=unCya_-8ECs&ab_channel=JessicaRichburg' 
    st.video(video_url)


    st.header("Gratitude")
    st.write("Shift your mindset.")
    st.write("Name three things that you are grateful for today. ")


    st.header("Self Talk")
    st.write("Talk to yourself as you would to a loved one.")
    with st.expander("View Steps"):
        st.markdown("""
        **Step 1:** Think of someone you love, like a family member, friend, or even a beloved pet.
                    
        **Step 2:** Picture them in your mind sitting across from you looking distressed, sad, or upset. 
                    
        **Step 3:** Offer them words of understanding and compassion. 
                    
        **Step 4:** Now use the same words on yourself. Talk to yourself as you would that friend. 
        """)

    
    st.header("Theater Mode")
    st.write("Visualize yourself into a new perspective on your emotions. ")
    with st.expander("View Steps"):
        st.markdown("""
        **Step 1:** Think about a recent challenging interaction with someone you care about.
                     
        **Step 2:** Imagine you’re sitting in the front row of a movie theater seeing yourself and the other person interacting on a movie screen. 
                    
        **Step 3:** Picture yourself slowly moving to the middle of the theater and farther back from the screen.
                     
        **Step 4:** Now go to the very back row of the theater and watch the interaction from there.
                     
        **Step 5:** Finally, move to the exit of the theater and watch the screen get smaller and smaller. 
                    
        **Step 6:** Notice that the sounds of the interactions gets fainter and fainter as you move farther and farther away. 

        """)


    st.header("Self Validation Quotes")
    st.write("Boost your sense of self-worth. Try saying these quotes to yourself:")
    self_val_path = "./assets/self_val.jpg" 
    st.image(self_val_path, use_column_width=True)


    st.header("Resource for Tips for Stress")
    st.write("Try these tips when you feel like your stress is getting out of hand.")
    stress_path = "./assets/stress.png"
    st.image(stress_path, use_column_width=True)




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
