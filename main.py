import streamlit as st
import random
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import base64
from fpdf import FPDF
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Elevate Mindset AI",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        * { font-family: 'Poppins', sans-serif; }
        
        /* Enhanced Navigation */
        .stSidebar .stRadio > div { 
            padding: 15px; 
            border-radius: 10px; 
            transition: background 0.3s ease;
        }
        .stSidebar .stRadio > div:hover { 
            background: rgba(255,255,255,0.1); 
        }
        .stSidebar .stRadio label { 
            font-size: 18px !important; 
            padding: 10px !important; 
        }
        
        /* Username Input Styling */
        .username-input { 
            padding: 20px;
            border-radius: 15px;
            background: rgba(255,255,255,0.1);
            margin-bottom: 30px;
        }
        .username-input h3 { 
            color: #fff; 
            margin-bottom: 15px; 
        }
        
        /* Homepage Styling */
        .home-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            margin-bottom: 30px;
        }
        .feature-card {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            margin: 15px 0;
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        /* Footer Styling */
        .footer {
            width: 100%;
            background: linear-gradient(90deg, #4A90E2, #50E3C2);
            padding: 40px 0;
            text-align: center;
            transition: background 0.5s ease;
            border-radius: 15px;
            margin-top: 30px;
        }
        .footer:hover {
            background: linear-gradient(90deg, #50E3C2, #4A90E2);
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'username' not in st.session_state:
    st.session_state.username = None
if 'success_wall' not in st.session_state:
    st.session_state.success_wall = []

# PDF Generation Function
from fpdf import FPDF

def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font for the entire document
    pdf.set_font("Arial", size=12)
    
    # Add a title
    pdf.set_font("Arial", style="B", size=16)  # Bold and larger font
    pdf.cell(200, 10, txt="Your Personal Growth Report", ln=True, align='C')
    pdf.ln(10)  # Add some space
    
    # Add user information
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt=f"User: {st.session_state.username if st.session_state.username else 'Guest'}", ln=True, align='L')
    pdf.ln(10)
    
    # Add a section header
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Weekly Progress", ln=True, align='L')
    pdf.ln(5)
    
    # Add a table for progress data
    pdf.set_font("Arial", size=12)
    pdf.set_fill_color(200, 220, 255)  # Light blue background for headers
    pdf.cell(40, 10, txt="Week", border=1, fill=True)
    pdf.cell(40, 10, txt="Goals Set", border=1, fill=True)
    pdf.cell(40, 10, txt="Goals Achieved", border=1, fill=True, ln=True)
    
    # Add table rows
    pdf.set_fill_color(255, 255, 255)  # White background for rows
    for week, goals_set, goals_achieved in zip(
        ["Week 1", "Week 2", "Week 3", "Week 4"],
        [5, 6, 7, 8],
        [3, 4, 5, 6]
    ):
        pdf.cell(40, 10, txt=week, border=1)
        pdf.cell(40, 10, txt=str(goals_set), border=1)
        pdf.cell(40, 10, txt=str(goals_achieved), border=1, ln=True)
    
    pdf.ln(10)  # Add some space
    
    # Add insights section
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Insights", ln=True, align='L')
    pdf.ln(5)
    
    # Add bullet points for insights (using ASCII characters)
    pdf.set_font("Arial", size=12)
    insights = [
        "- Consistent improvement in goal setting",
        "- Increasing achievement rate",
        "- Great work on maintaining momentum!"
    ]
    for insight in insights:
        pdf.cell(10)  # Indent for bullet points
        pdf.cell(0, 10, txt=insight, ln=True)
    
    # Add a footer
    pdf.set_y(-20)  # Position at the bottom of the page
    pdf.set_font("Arial", style="I", size=10)
    pdf.cell(0, 10, txt="Generated by Elevate Mindset AI", align='C')
    
    # Return the PDF as bytes
    return pdf.output(dest='S')

# Username Input in Sidebar
with st.sidebar:
    st.markdown("<div class='username-input'>", unsafe_allow_html=True)
    username = st.text_input("Enter your name to personalize your experience:")
    if username:
        st.session_state.username = username
        st.success(f"Welcome, {username}! Let's grow together 🌱")
    st.markdown("</div>", unsafe_allow_html=True)

# Enhanced Homepage
def show_home():
    st.markdown(f"""
    <div class='home-container'>
        <h1 style='font-size: 38px; margin-bottom: 20px;'>🌟 Welcome {st.session_state.username if st.session_state.username else ""} to Elevate Mindset AI 🚀</h1>
        <p style='font-size: 20px;'>Your personal growth companion for mindset elevation and productivity enhancement</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h3>📚 Daily Insights</h3>
            <p>Get personalized motivational content daily</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h3>📈 Progress Tracking</h3>
            <p>Visualize your growth journey</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <h3>🎯 Goal Management</h3>
            <p>Set and achieve your objectives</p>
        </div>
        """, unsafe_allow_html=True)

    # New Small Box with Text and Emojis
    st.markdown("""
    <style>
        .small-box {
            background-color: #2e2e2e; /* Dark background */
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            color: #ffffff; /* White text */
            border-left: 5px solid #6A11CB; /* Purple accent border */
            transition: transform 0.3s ease;
        }
        .small-box:hover {
            transform: translateY(-5px); /* Hover effect */
        }
        .small-box h3 {
            font-size: 24px;
            margin-bottom: 10px;
            color: #ffffff; /* White text */
        }
        .small-box p {
            font-size: 18px;
            color: #ffffff; /* White text */
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='small-box'>
        <h3>💡 Did You Know?</h3>
        <p>
            🌱 Small, consistent steps lead to big changes over time. <br>
            🧠 A growth mindset can increase your resilience and productivity. <br>
            🎉 Celebrate every win, no matter how small!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Daily Inspiration Section
def show_daily_inspiration():
    st.markdown("<h2 class='subheader'>💡 Daily Inspiration</h2>", unsafe_allow_html=True)
    
    # Add a motivational tip section
    st.markdown("""
    <style>
        .motivational-tip {
            background-color: #2e2e2e; /* Dark background */
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            color: #ffffff; /* White text */
            border-left: 5px solid #6A11CB; /* Purple accent border */
            transition: transform 0.3s ease;
        }
        .motivational-tip:hover {
            transform: translateY(-5px); /* Hover effect */
        }
        .motivational-tip h3 {
            font-size: 24px;
            margin-bottom: 10px;
            color: #ffffff; /* White text */
        }
        .motivational-tip p {
            font-size: 18px;
            color: #ffffff; /* White text */
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='motivational-tip'>
        <h3>🌟 Motivational Tip of the Day</h3>
        <p>
            Start your day with a positive affirmation. <br>
            Repeat to yourself: <strong>"I am capable, I am strong, and I can achieve my goals!"</strong> <br>
            🧠 This simple practice can boost your confidence and set the tone for a productive day.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add a quote generator
    st.markdown("<h3 class='subheader'>✨ Get Inspired with a Random Quote</h3>", unsafe_allow_html=True)
    
    quotes = [
        "Dream big and dare to fail. — Norman Vaughan",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. — William James",
        "Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
        "The only way to do great work is to love what you do. — Steve Jobs",
        "Believe you can and you're halfway there. — Theodore Roosevelt",
        "Your time is limited, don't waste it living someone else's life. — Steve Jobs",
        "The best time to plant a tree was 20 years ago. The second best time is now. — Chinese Proverb",
        "You are never too old to set another goal or to dream a new dream. — C.S. Lewis"
    ]
    
    if st.button("✨ Inspire Me!"):
        selected_quote = random.choice(quotes)
        st.markdown(f"<div class='quote-box'>{selected_quote}</div>", unsafe_allow_html=True)

    # Add a section for user-submitted quotes
    st.markdown("<h3 class='subheader'>📝 Share Your Favorite Quote</h3>", unsafe_allow_html=True)
    user_quote = st.text_area("Write your favorite motivational quote here:")
    if st.button("Submit Quote"):
        if user_quote:
            st.success("🎉 Thank you for sharing your quote! Here's what you wrote:")
            st.markdown(f"<div class='quote-box'>{user_quote}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a quote before submitting.")

   

# Goal Setting Section
def show_goal_setting():
    st.markdown("<h2 class='subheader'>🎯 Set & Achieve Goals</h2>", unsafe_allow_html=True)
    
    # Add a form for goal setting
    with st.form("goal_form"):
        # Goal Title
        goal_title = st.text_input("What is your goal?")
        
        # Goal Category
        goal_category = st.selectbox(
            "Category:",
            ["Personal", "Professional", "Health", "Education", "Other"]
        )
        
        # Goal Deadline
        goal_deadline = st.date_input("Deadline:")
        
        # Goal Priority
        goal_priority = st.selectbox(
            "Priority:",
            ["Low", "Medium", "High"]
        )
        
        # Goal Description
        goal_description = st.text_area("Description (optional):")
        
        # Submit Button
        submitted = st.form_submit_button("Set Goal")
        
        if submitted:
            if goal_title:
                # Save the goal in session state
                if "goals" not in st.session_state:
                    st.session_state.goals = []
                
                st.session_state.goals.append({
                    "title": goal_title,
                    "category": goal_category,
                    "deadline": goal_deadline,
                    "priority": goal_priority,
                    "description": goal_description,
                    "progress": 0  # Initial progress
                })
                st.success("🚀 Goal Set! Keep pushing forward!")
            else:
                st.warning("Please enter a goal title.")

    # Display Goals
    if "goals" in st.session_state and st.session_state.goals:
        st.markdown("<h3 class='subheader'>📋 Your Goals</h3>", unsafe_allow_html=True)
        
        for i, goal in enumerate(st.session_state.goals):
            with st.expander(f"{goal['title']} ({goal['category']})"):
                st.markdown(f"""
                    <div class='goal-card'>
                        <p><strong>Deadline:</strong> {goal['deadline']}</p>
                        <p><strong>Priority:</strong> {goal['priority']}</p>
                        <p><strong>Description:</strong> {goal['description']}</p>
                        <p><strong>Progress:</strong></p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Progress Bar
                progress = st.slider(
                    f"Update Progress for '{goal['title']}'",
                    0, 100, goal['progress'],
                    key=f"progress_{i}"
                )
                st.session_state.goals[i]["progress"] = progress
                
                # Delete Button
                if st.button(f"Delete Goal: {goal['title']}", key=f"delete_{i}"):
                    st.session_state.goals.pop(i)
                    st.success(f"Goal '{goal['title']}' deleted!")
                    st.experimental_rerun()

# Custom Styling for Goal Cards
st.markdown("""
    <style>
        .goal-card {
            background-color: #2e2e2e; /* Dark background */
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            color: #ffffff; /* White text */
            border-left: 5px solid #6A11CB; /* Purple accent border */
            transition: transform 0.3s ease;
        }
        .goal-card:hover {
            transform: translateY(-5px); /* Hover effect */
        }
        .goal-card p {
            font-size: 18px;
            color: #ffffff; /* White text */
        }
    </style>
""", unsafe_allow_html=True)

# Productivity Challenge Section
def show_productivity():
    st.markdown("<h2 class='subheader'>🔥 Productivity Boost</h2>", unsafe_allow_html=True)
    
    # List of productivity challenges
    challenges = [
        "Learn something new today and share it with someone.",
        "Step out of your comfort zone and try something different!",
        "Spend 15 minutes reflecting on your achievements.",
        "List three things you're grateful for today.",
        "Declutter your workspace and organize your thoughts.",
        "Set a timer for 25 minutes and focus on one task (Pomodoro Technique).",
        "Take a 10-minute walk to clear your mind.",
        "Write down your top 3 priorities for the day.",
        "Turn off notifications and work distraction-free for an hour.",
        "Review your goals and adjust them if necessary."
    ]

    # Initialize session state for completed challenges
    if "completed_challenges" not in st.session_state:
        st.session_state.completed_challenges = []

    # Initialize session state for community challenges
    if "community_challenges" not in st.session_state:
        st.session_state.community_challenges = []

    # Display a random challenge for the day
    st.markdown("<h3 class='subheader'>💡 Today's Productivity Challenge</h3>", unsafe_allow_html=True)
    if "today_challenge" not in st.session_state:
        st.session_state.today_challenge = random.choice(challenges)
    
    st.markdown(f"""
        <div class='challenge-card'>
            <h3>🌟 {st.session_state.today_challenge}</h3>
        </div>
    """, unsafe_allow_html=True)

    # Mark challenge as completed
    if st.button("✅ Mark as Completed"):
        if st.session_state.today_challenge not in st.session_state.completed_challenges:
            st.session_state.completed_challenges.append(st.session_state.today_challenge)
            st.success("Great job! Challenge marked as completed.")
        else:
            st.warning("You've already completed this challenge!")

    # Display progress
    st.markdown("<h3 class='subheader'>📊 Your Progress</h3>", unsafe_allow_html=True)
    total_challenges = len(challenges)
    completed = len(st.session_state.completed_challenges)
    progress = (completed / total_challenges) * 100  # Progress in percentage

    st.write(f"**Completed Challenges:** {completed}/{total_challenges}")
    st.progress(progress / 100)  # Normalize to 0.0 to 1.0

    # Display completed challenges
    if st.session_state.completed_challenges:
        st.markdown("<h4 class='subheader'>🎉 Completed Challenges</h4>", unsafe_allow_html=True)
        for challenge in st.session_state.completed_challenges:
            st.markdown(f"<div class='challenge-card'>{challenge}</div>", unsafe_allow_html=True)

    # Community Challenges Section
    st.markdown("<h3 class='subheader'>🌍 Community Challenges</h3>", unsafe_allow_html=True)
    st.write("Share your own productivity challenges with the community:")

    # Submit a new challenge
    user_challenge = st.text_area("Write your productivity challenge:")
    if st.button("📤 Submit Challenge"):
        if user_challenge:
            st.session_state.community_challenges.append({
                "challenge": user_challenge,
                "upvotes": 0
            })
            st.success("Thank you for sharing your challenge!")
        else:
            st.warning("Please write a challenge before submitting.")

    # Display community challenges
    if st.session_state.community_challenges:
        st.write("Community Challenges:")
        for i, challenge in enumerate(st.session_state.community_challenges):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"<div class='challenge-card'>{challenge['challenge']}</div>", unsafe_allow_html=True)
            with col2:
                if st.button(f"👍 {challenge['upvotes']}", key=f"upvote_{i}"):
                    st.session_state.community_challenges[i]["upvotes"] += 1
                    st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

# Custom Styling for Challenge Cards
st.markdown("""
    <style>
        .challenge-card {
            background-color: #2e2e2e; /* Dark background */
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            color: #ffffff; /* White text */
            border-left: 5px solid #6A11CB; /* Purple accent border */
            transition: transform 0.3s ease;
        }
        .challenge-card:hover {
            transform: translateY(-5px); /* Hover effect */
        }
        .challenge-card h3 {
            font-size: 24px;
            margin-bottom: 10px;
            color: #ffffff; /* White text */
        }
    </style>
""", unsafe_allow_html=True)

# Self Reflection Section
def show_reflection():
    st.markdown("<h2 class='subheader'>💭 Reflect & Grow</h2>", unsafe_allow_html=True)
    reflection = st.text_area("Pen down your thoughts:")
    if reflection:
        st.success(f"💡 **Insightful Reflection:** {reflection}")

# Achievements Section
def show_achievements():
    st.markdown("<h2 class='subheader'>🏆 Celebrate Success</h2>", unsafe_allow_html=True)
    achievement = st.text_input("Share a recent win:")
    if achievement:
        st.markdown(f"<div class='success-box'>🎉 You achieved: {achievement}</div>", unsafe_allow_html=True)

# Growth Quiz Section
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
            quiz_data = {
                "Category": ["Challenge", "Reflection", "Motivation", "Productivity", "Satisfaction"],
                "Score": [score1, score2, score3, score4, score5]
            }
            df_quiz = pd.DataFrame(quiz_data)

            # Create a colorful bar chart using Plotly
            fig = px.bar(
                df_quiz,
                x="Category",
                y="Score",
                text="Score",
                color="Category",
                color_discrete_sequence=px.colors.qualitative.Pastel,  # Use a colorful palette
                title="Your Growth Quiz Results"
            )

            # Customize the chart layout
            fig.update_layout(
                plot_bgcolor="#1e1e1e",  # Dark background
                paper_bgcolor="#1e1e1e",  # Dark background
                font=dict(color="#ffffff"),  # White text
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False),
                title_font=dict(size=24, color="#ffffff"),  # Title styling
                hoverlabel=dict(font=dict(color="#1e1e1e"))  # Hover label styling
            )

            # Display the chart
            st.plotly_chart(fig, use_container_width=True)

            # Provide detailed feedback based on the total score
            if total_score <= 10:
                st.error("It seems you might need a boost. Consider setting small, achievable goals and reflecting more often on your progress.")
            elif total_score <= 18:
                st.info("You're on the right track! Keep challenging yourself and take time to reflect on your growth.")
            else:
                st.success("Fantastic work! You have a strong growth mindset. Keep up the excellent progress!")

# Success Wall Section
def show_success_wall():
    st.markdown("<h2 class='subheader'>🌟 Success Wall</h2>", unsafe_allow_html=True)
    success_message = st.text_input("Post a success story:")
    if st.button("Post to Wall"):
        if success_message:
            st.session_state.success_wall.append(success_message)
            st.success("🎉 Success story added!")
    if st.session_state.success_wall:
        for story in st.session_state.success_wall:
            st.markdown(f"<div class='success-box'>{story}</div>", unsafe_allow_html=True)

# Daily Reminders Section
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

# Enhanced Progress Tracker with Plotly
def show_progress_chart():
    st.markdown("<h2 class='subheader'>📈 Enhanced Progress Tracker</h2>", unsafe_allow_html=True)
    
    # Sample data
    progress_data = {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Goals Set": [5, 6, 7, 8],
        "Goals Achieved": [3, 4, 5, 6]
    }
    
    # Create Plotly chart
    fig = px.line(progress_data, x="Week", y=["Goals Set", "Goals Achieved"],
                  title="Your Progress Over Time",
                  labels={"value": "Number of Goals", "variable": "Metric"},
                  markers=True)
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    
    st.plotly_chart(fig, use_container_width=True, className="plotly-chart")
    
    # PDF Generation
    if st.button("📄 Generate Progress Report"):
        content = f"""
        Progress Report for {st.session_state.username if st.session_state.username else "User"}
        
        Weekly Progress:
        {progress_data}
        
        Insights:
        - Consistent improvement in goal setting
        - Increasing achievement rate
        - Great work on maintaining momentum!
        """
        
        pdf = create_pdf(content)
        st.success("Report generated successfully!")
        
        # Download link
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="progress_report.pdf">Download Report</a>'
        st.markdown(href, unsafe_allow_html=True)

# Main App Logic
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

# Footer
st.markdown("""
<div class="footer">
  <h2 style="font-size: 32px; margin: 10px 0; color: #ffffff;">Reach New Heights Together!</h2>
  <p style="font-size: 20px; margin: 10px 0; color: #ffffff;">Empowering Growth with Elevate Mindset AI</p>
</div>
""", unsafe_allow_html=True)



