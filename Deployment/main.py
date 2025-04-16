import streamlit as st
import pickle
import pandas as pd

# Background and styling
st.markdown(
    """
    <style>
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        background-image: url("https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        opacity: 0.15;
        z-index: -1;
    }

    .stApp {
        background-color: #1e1e2f;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    h1, h2, h3, h4, h5 {
        color: #ffd700 !important;
    }

    .block-container {
        padding: 2rem;
    }

    p, li {
        text-align: justify;
        color: #e0e0e0;
        font-size: 16px;
    }

    .center-button {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    .stButton>button {
        background-color: #ff7f50;
        color: white;
        border-radius: 12px;
        padding: 0.5em 2em;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #ff5722;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title and Form
st.title("🧠 Mental Health Detection")
st.markdown("#### Please fill in your daily activity details to get a mental wellness insight.")

# Input Form
with st.form("mental_health_form"):
    col1, col2 = st.columns(2)

    with col1:
        work_hours = st.number_input("🕒 Working hours per week", min_value=20, max_value=70)
        Family_history = st.selectbox("👨‍👩‍👧 Family history of mental health issues?", ("Yes", "No"))
        sleep = st.number_input("😴 Sleep hours per day", min_value=4, max_value=10)
        Diet = st.selectbox("🍽️ Diet quality", ("Good", "Average", "Poor"))

    with col2:
        stress = st.slider("😰 Stress levels (1-10)", min_value=0, max_value=10)
        physical_activity = st.number_input("🏃 Physical activity (minutes/day)", min_value=0, max_value=180)
        social_interaction = st.slider("🗣️ Social interaction level (1-10)", min_value=0, max_value=10)

    # Center the submit button
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Predict")
    st.markdown('</div>', unsafe_allow_html=True)

# Model prediction
if submitted:
    with open("encoder.pkl", 'rb') as file:
        encode = pickle.load(file)
    with open("xgboost_model.pkl", "rb") as file:
        model = pickle.load(file)

    df = pd.DataFrame([[work_hours, Family_history, sleep, stress,
                        physical_activity, social_interaction, Diet]],
                      columns=['Work Hours', 'Family History', 'Sleep Hours',
                               'Stress Level', 'Physical Activity',
                               'Social Interaction', 'Diet Quality'])

    transformed_df = encode.transform(df)
    prediction = model.predict(transformed_df)[0]

    # Output results
    if prediction == 1:
        st.warning("⚠️ You may be at risk for mental health issues. It's recommended to take some self-care actions.")
    else:
        st.success("✅ You're doing well! Keep up the good habits.")

    # Personalized Tips
    st.markdown("### 💡 Personalized Tips to Boost Your Mental Health")
    tips = []

    if Diet != "Good":
        tips.append("🍎 **Eat a Nutrient-Rich Snack Daily**  \nSupports brain health with omega-3s, vitamins, and minerals.")

    if stress > 6:
        tips.append("🧘 **Meditate or Stretch for 15 Minutes**  \nEases anxiety and improves focus.")
        tips.append("🌬️ **Practice Deep Breathing for 10 Minutes**  \nLowers stress and anxiety levels.")
        tips.append("🚰 **Drink Water & Take 5-Minute Breaks**  \nHydration supports mental clarity.")
        tips.append("🎧 **Walk 30 Minutes Daily with Music**  \nReduces stress and uplifts mood.")

    if sleep < 7:
        tips.append("🛌 **Set a Consistent Sleep Schedule (7–8 Hours)**  \nImproves energy and stabilizes mood.")

    if work_hours > 50:
        tips.append("📅 **Limit Work to 40–45 Hours Per Week**  \nPrevents burnout and enhances productivity.")

    if social_interaction < 5:
        tips.append("👥 **Spend at Least 1 Hour Socializing Daily**  \nBoosts emotional well-being and reduces isolation.")

    for tip in tips:
        st.markdown(f"<p>{tip}</p>", unsafe_allow_html=True)

