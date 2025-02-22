import streamlit as st
import random
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Elevate Mindset AI", page_icon="🌟", layout="wide")

# Custom Styling without animations and updated footer color
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        * { font-family: 'Poppins', sans-serif; }
        body { background-color: #f4f7fc; color: #333; }
        .title { 
            font-size: 50px; 
            font-weight: bold; 
            text-align: center; 
            background: linear-gradient(90deg, #6A11CB, #3f51b5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px; 
        }
        .subheader { 
            font-size: 26px; 
            font-weight: 600; 
            text-align: center; 
            color: #3f51b5;
            margin-bottom: 15px; 
            border-bottom: 3px solid #6A11CB; 
            padding-bottom: 10px; 
        }
        .quote-box, .success-box { 
            border-radius: 15px; 
            padding: 18px; 
            text-align: center; 
            font-weight: bold; 
            margin-bottom: 20px; 
        }
        .quote-box { 
            background-color: #fffae5; 
            border-left: 8px solid #ff9800; 
            color: #444; 
        }
        .success-box { 
            background-color: #e5ffe5; 
            border-left: 8px solid #2e7d32; 
            color: #1b5e20; 
        }
        .footer { 
            font-size: 18px; 
            color: white; 
            text-align: center; 
            padding: 20px;
            margin-top: 30px; 
            background: #ff5722; 
            border-radius: 10px; 
            font-weight: bold; 
        }
        .stButton>button { 
            background: linear-gradient(90deg, #6A11CB, #3f51b5);
            color: white; 
            font-size: 18px; 
            font-weight: bold; 
            border: none; 
            border-radius: 5px; 
            padding: 10px 20px; 
            cursor: pointer; 
            transition: transform 0.3s ease; 
            margin-top: 10px;
        }
        .stButton>button:hover { 
            transform: scale(1.1); 
        }
        /* Target the entire sidebar container */
        [data-testid="stSidebar"] {
            background-color: #333333;
            color: #ffffff;
        }
        /* Ensure the sidebar content text is white */
        [data-testid="stSidebar"] .css-1d391kg, 
        [data-testid="stSidebar"] * {
            color: #ffffff;
        }
        /* Style the links in the sidebar */
        [data-testid="stSidebar"] a {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Define section functions
def show_home():
    st.markdown("""
    <style>
        .home-heading {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(90deg, #4A90E2, #50E3C2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            transition: transform 0.3s ease;
            cursor: pointer;
        }
        .home-heading:hover {
            transform: scale(1.05);
        }
        .home-box {
            border: 2px solid #f7dc6f; /* Light yellow border */
            background-color: #fcf3cf; /* Pale yellow background */
            padding: 20px;
            border-radius: 10px;
            margin: 20px auto;
            width: 80%;
            text-align: center;
        }
        .home-box p {
            font-size: 22px;
            color: #f1c40f; /* Bright yellow text */
            transition: color 0.3s ease;
        }
        .home-box p:hover {
            color: #f39c12;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='home-heading'>🌟 Elevate Your Mindset & Thrive 🚀</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='home-box'>
        <p>
            Welcome to your personal growth hub, where inspiration meets action!
            Dive into daily motivational quotes, goal-setting exercises, productivity challenges,
            interactive quizzes, and a progress tracker – all designed to empower your journey.
            Unleash your potential, cultivate a growth mindset, and embrace every opportunity
            to succeed. Let's embark on this transformative journey together!
        </p>
    </div>
    """, unsafe_allow_html=True)



def show_daily_inspiration():
    st.markdown("<h2 class='subheader'>💡 Daily Inspiration</h2>", unsafe_allow_html=True)
    quotes = [
        "Dream big and dare to fail. — Norman Vaughan",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. — William James",
        "Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill"
    ]
    if st.button("✨ Inspire Me!"):
        st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

def show_goal_setting():
    st.markdown("<h2 class='subheader'>🎯 Set & Achieve Goals</h2>", unsafe_allow_html=True)
    goal = st.text_input("What is your goal for this week?")
    if goal:
        st.success(f"🚀 Goal Set: **{goal}**. Stay committed and keep moving forward!")

def show_productivity():
    st.markdown("<h2 class='subheader'>🔥 Productivity Boost</h2>", unsafe_allow_html=True)
    challenges = [
        "Learn something new today and share it with someone.",
        "Step out of your comfort zone and try something different!",
        "Spend 15 minutes reflecting on your achievements.",
        "List three things you're grateful for today.",
        "Declutter your workspace and organize your thoughts."
    ]
    if st.button("💡 Get Challenge!"):
        st.info(f"💡 **Challenge:** {random.choice(challenges)}")

def show_reflection():
    st.markdown("<h2 class='subheader'>💭 Reflect & Grow</h2>", unsafe_allow_html=True)
    reflection = st.text_area("Pen down your thoughts:")
    if reflection:
        st.success(f"💡 **Insightful Reflection:** {reflection}")

def show_achievements():
    st.markdown("<h2 class='subheader'>🏆 Celebrate Success</h2>", unsafe_allow_html=True)
    achievement = st.text_input("Share a recent win:")
    if achievement:
        st.markdown(f"<div class='success-box'>🎉 You achieved: {achievement}</div>", unsafe_allow_html=True)

def show_growth_quiz():
    st.markdown("<h2 class='subheader'>📊 Growth Quiz</h2>", unsafe_allow_html=True)
    st.write("Answer the following questions to see your growth insights.")

    # Question 1: Challenge frequency
    q1 = st.selectbox("1. How often do you challenge yourself?", 
                        ["Select an option", "Rarely", "Sometimes", "Often", "Always"])
    # Question 2: Reflection frequency
    q2 = st.selectbox("2. How often do you reflect on your progress?", 
                        ["Select an option", "Rarely", "Sometimes", "Often", "Always"])
    # Question 3: Motivation slider
    q3 = st.slider("3. How motivated do you feel today? (1 = low, 10 = high)", 1, 10, 5)
    # Question 4: Productivity rating
    q4 = st.selectbox("4. How do you rate your productivity?", 
                        ["Select an option", "Low", "Moderate", "High", "Very High"])
    # Question 5: Satisfaction level
    q5 = st.selectbox("5. How satisfied are you with your progress so far?",
                        ["Select an option", "Not satisfied", "Somewhat satisfied", "Satisfied", "Very satisfied"])

    if st.button("Submit Quiz"):
        # Check if required questions have been answered
        if (q1 == "Select an option" or q2 == "Select an option" or 
            q4 == "Select an option" or q5 == "Select an option"):
            st.warning("Please select an option for all questions.")
        else:
            # Mapping for multiple-choice answers
            mapping = {"Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}
            prod_mapping = {"Low": 1, "Moderate": 2, "High": 3, "Very High": 4}
            satis_mapping = {"Not satisfied": 1, "Somewhat satisfied": 2, "Satisfied": 3, "Very satisfied": 4}

            score1 = mapping[q1]
            score2 = mapping[q2]
            score3 = q3
            score4 = prod_mapping[q4]
            score5 = satis_mapping[q5]

            total_score = score1 + score2 + score3 + score4 + score5
            st.success(f"Your Scores - Challenge: {score1}, Reflection: {score2}, Motivation: {score3}, Productivity: {score4}, Satisfaction: {score5}")
            st.write(f"**Total Score:** {total_score} (Maximum possible: 26)")

            # Create a bar chart to visualize individual scores
            import pandas as pd
            quiz_data = {
                "Category": ["Challenge", "Reflection", "Motivation", "Productivity", "Satisfaction"],
                "Score": [score1, score2, score3, score4, score5]
            }
            df_quiz = pd.DataFrame(quiz_data).set_index("Category")
            st.bar_chart(df_quiz)

            # Provide detailed feedback based on the total score
            if total_score <= 10:
                st.error("It seems you might need a boost. Consider setting small, achievable goals and reflecting more often on your progress.")
            elif total_score <= 18:
                st.info("You're on the right track! Keep challenging yourself and take time to reflect on your growth.")
            else:
                st.success("Fantastic work! You have a strong growth mindset. Keep up the excellent progress!")


           

def show_success_wall():
    st.markdown("<h2 class='subheader'>🌟 Success Wall</h2>", unsafe_allow_html=True)
    if "success_wall" not in st.session_state:
        st.session_state.success_wall = []
    success_message = st.text_input("Post a success story:")
    if st.button("Post to Wall"):
        if success_message:
            st.session_state.success_wall.append(success_message)
            st.success("🎉 Success story added!")
    if st.session_state.success_wall:
        for story in st.session_state.success_wall:
            st.markdown(f"<div class='success-box'>{story}</div>", unsafe_allow_html=True)

def show_daily_reminders():
    st.markdown("<h2 class='subheader'>🔄 Stay Motivated</h2>", unsafe_allow_html=True)
    reminders = [
        "Every small step counts. Keep moving forward. 🚀",
        "Your future self will thank you for today's effort! 🌟",
        "Success comes from consistency. Keep showing up! 💪",
        "Failure is just another step towards growth. Never give up! 🔥",
        "Great things take time. Stay patient and persistent! ⏳"
    ]
    if st.button("🔔 Get Reminder!"):
        st.success(random.choice(reminders))

def show_progress_chart():
    st.markdown("<h2 class='subheader'>📈 Progress Tracker</h2>", unsafe_allow_html=True)
    st.write("Here is a sample chart of your progress over the past weeks.")
    # Simulated progress data for demonstration purposes
    progress_data = {
        "Goals Set": [5, 6, 7, 8],
        "Goals Achieved": [3, 4, 5, 6]
    }
    df_progress = pd.DataFrame(progress_data, index=["Week 1", "Week 2", "Week 3", "Week 4"])
    st.bar_chart(df_progress)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='text-align: center;'>Navigation</h2>", unsafe_allow_html=True)
app_mode = st.sidebar.radio("Go to", [
    "Home", 
    "Daily Inspiration", 
    "Goal Setting", 
    "Productivity Challenge", 
    "Self Reflection", 
    "Achievements", 
    "Growth Quiz", 
    "Success Wall", 
    "Daily Reminders",
    "Progress Tracker"
])

# Render the selected section
if app_mode == "Home":
    show_home()
elif app_mode == "Daily Inspiration":
    show_daily_inspiration()
elif app_mode == "Goal Setting":
    show_goal_setting()
elif app_mode == "Productivity Challenge":
    show_productivity()
elif app_mode == "Self Reflection":
    show_reflection()
elif app_mode == "Achievements":
    show_achievements()
elif app_mode == "Growth Quiz":
    show_growth_quiz()
elif app_mode == "Success Wall":
    show_success_wall()
elif app_mode == "Daily Reminders":
    show_daily_reminders()
elif app_mode == "Progress Tracker":
    show_progress_chart()

# Footer with updated color
st.markdown("""
<div class="footer">
  <h2 style="font-size: 32px; margin: 10px 0; color: #ffffff;">Reach New Heights Together!</h2>
  <p style="font-size: 20px; margin: 10px 0; color: #ffffff;">Empowering Growth with Elevate Mindset AI</p>
</div>
<style>
.footer {
  width: 100%;
  background: linear-gradient(90deg, #4A90E2, #50E3C2); /* Blue-green gradient */
  padding: 40px 0;
  text-align: center;
  transition: background 0.5s ease;
}
.footer:hover {
  background: linear-gradient(90deg, #50E3C2, #4A90E2);
}
</style>
""", unsafe_allow_html=True)



