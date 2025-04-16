import streamlit as st

# Custom CSS for improved styling and text justification
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e2f;  /* Dark background for better contrast */
        padding: 30px;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #f8f8ff !important;
        text-align: left;
        padding-bottom: 10px;
    }

    h3, .stSubheader {
        color: #ffe4b5 !important;
        text-align: left;
        padding-top: 20px;
    }

    p, li, .stMarkdown, .css-1v3fvcr {
        color: #f0f0f0 !important;
        text-align: justify !important;
        font-size: 16px !important;
        line-height: 1.6;
    }

    ul {
        padding-left: 40px;
    }

    .data-key {
        color: #fdd835;  /* Bright gold */
        font-weight: bold;
    }

    .data-desc {
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🧠 Mental Health Detection")

# Background Story
st.subheader("Background Story")
st.write("""
In today’s fast-paced world, mental health issues are becoming increasingly common, especially among individuals working in the IT industry. 
To address this growing concern, the goal of this project is to analyze daily activities of individuals, such as age, gender, sleep hours, 
stress levels, physical activity, social interaction, and more. By identifying patterns in this data, we aim to build a machine learning 
model that predicts whether an individual is likely to seek treatment for mental health concerns. This model will help in the early 
identification of at-risk individuals, enabling timely support and intervention to improve mental well-being.
""")

# Objective
st.subheader("Objective")
st.write("""
To thoroughly understand and analyze people's daily activities, a large dataset is essential. However, due to the unavailability of 
open-source datasets containing such confidential information, we researched data from multiple health organizations, including the 
World Health Organization (WHO) and others. From these datasets, we extracted common features (e.g., age, gender, sleep hours, 
stress levels, physical activity, social interaction) for analysis.

Based on the analyzed data, we aim to apply various machine learning algorithms and select the best-performing one to build a predictive model. 
By integrating Generative AI (GenAI), the model will take user inputs and provide personalized suggestions to improve mental well-being.
""")

# Key Steps
st.subheader("Key Steps")
st.write("""
- **Analyze Data**: Study the collected survey data to identify patterns and trends related to mental health.  
- **Apply Algorithms**: Test multiple machine learning algorithms and select the one with the best performance.  
- **Build Model**: Develop a predictive model using the selected algorithm to identify individuals at risk of mental health issues.  
- **Add GenAI**: Integrate Generative AI to provide personalized suggestions based on user inputs.  
- **Provide Help**: Offer actionable tips and recommendations to improve mental health and well-being.
""")

# Why this approach
st.subheader("Why This Approach?")
st.write("""
- **Data-Driven Insights**: Analyzing real-world data ensures accurate and meaningful results.  
- **Advanced Technology**: Combining machine learning with Generative AI enables personalized and effective solutions.  
- **Proactive Support**: Early identification and intervention can significantly improve mental health outcomes.
""")

# Data Understanding
st.subheader("Data Understanding")

st.markdown("""
<ul>
  <li><span class="data-key">Age</span>: <span class="data-desc">Represents the age of the individual (in years).</span></li>
  <li><span class="data-key">Sleep Hours</span>: <span class="data-desc">Indicates how many hours of sleep the person gets per day.</span></li>
  <li><span class="data-key">Gender</span>: <span class="data-desc">Represents the gender of the individual (e.g., Male, Female, Others).</span></li>
  <li><span class="data-key">Physical Activity</span>: <span class="data-desc">Time (in minutes) the person spends on physical activity daily.</span></li>
  <li><span class="data-key">Social Interaction</span>: <span class="data-desc">Rating (0–10) of how much time the person spends interacting with people.</span></li>
  <li><span class="data-key">Diet Quality</span>: <span class="data-desc">Indicates if the person follows a healthy diet (e.g., Poor, Average, Good).</span></li>
  <li><span class="data-key">Work Hours</span>: <span class="data-desc">Number of hours the person works per week.</span></li>
  <li><span class="data-key">Family History</span>: <span class="data-desc">Indicates family history of mental health issues (Yes/No).</span></li>
  <li><span class="data-key">Treatment</span>: <span class="data-desc">Indicates whether the person has sought mental health treatment (Yes/No).</span></li>
</ul>
""", unsafe_allow_html=True)
