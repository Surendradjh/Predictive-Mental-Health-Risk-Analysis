import streamlit as st
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.markdown("""
    <style>
    .stApp {
        background-color: #112222;
        color: #f0f0f0;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #ffffff;
    }

    .image-card {
        background-color: rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 20px;
        margin: 30px 0;
        transition: transform 0.3s ease, background-color 0.3s ease;
        text-align: center;
    }

    .image-card:hover {
        transform: scale(1.03);
        background-color: rgba(255, 255, 255, 0.10);
    }

    .image-card img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
        transition: transform 0.3s ease;
    }

    .image-card:hover img {
        transform: scale(1.05);
    }

    .insight-text {
        text-align: justify;
        color: #e6e6e6;
        font-size: 16px;
        margin-top: 20px;
        transition: font-weight 0.3s ease;
        font-weight: 400;
    }

    .image-card:hover .insight-text {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Data Analysis")
option = st.selectbox("", ["UniFeature analysis", "MultiFeature Analysis"])

# Helper to display image + insight
def image_with_hover_insight(image_path, insight_text):
    img_base64 = image_to_base64(image_path)
    html = f"""
    <div class="image-card">
        <img src="data:image/png;base64,{img_base64}" />
        <div class="insight-text">{insight_text}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Logic for different sections
if option == "UniFeature analysis":
    image_with_hover_insight(
        "Deployment/plots/Count of Treatment.png",
        "The number of individuals needing treatment is higher than those who do not in this dataset."
    )
    image_with_hover_insight(
        "Deployment/plots/Age Distribution.png",
        "- The age distribution almost follows a uniform distribution.<br>- The minimum age is between 18 and 20.<br>- The maximum age is between 95 and 98."
    )
    image_with_hover_insight(
        "Deployment/plots/count based on Gender.png",
        "Half of the participants in this dataset are male, while the other half include females and individuals of other gender identities."
    )
    image_with_hover_insight(
        "Deployment/plots/sleeping Hours.png",
        "Sleeping hours follow a normal distribution."
    )
    image_with_hover_insight(
        "Deployment/plots/Social Interaction.png",
        "People's social interaction is almost following a uniform distribution."
    )
    image_with_hover_insight(
        "Deployment/plots/Physical Activity.png",
        "People's physical activity timings are following a uniform distribution."
    )

else:
    st.subheader("Multiple Feature's Analysis")

    image_with_hover_insight(
        "Deployment/plots/Age vs Treatment.png",
        "Older age groups show a significantly higher count of individuals seeking treatment, while the group not requiring treatment appears steady and much smaller in comparison."
    )
    image_with_hover_insight(
        "Deployment/plots/Data Distributions.png",
        "- ✅ No significant outliers observed.<br>- Sleep Hours shows a narrow distribution.<br>- Physical Activity shows high variability."
    )
    image_with_hover_insight(
        "Deployment/plots/Gender-Diet-Treatment.png",
        "- 👨‍⚕️ Males with poor diet seek treatment the most.<br>- 👩‍⚕️ Females show similar trends.<br>- ✅ Diet quality strongly influences mental health."
    )
    image_with_hover_insight(
        "Deployment/plots/Family History vs Treatment.png",
        "No strong relationship between family history and treatment. Many individuals without a family history still seek help."
    )
    image_with_hover_insight(
        "Deployment/plots/correlation between features.png",
        "Individual features show weak correlation with stress level. Use feature selection techniques to find better combinations or non-linear patterns."
    )
