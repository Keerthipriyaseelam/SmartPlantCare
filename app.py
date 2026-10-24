import os
import streamlit as st
import time
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

st.set_page_config(
    page_title="SmartPlantCare",
    page_icon="🌱"
)

st.markdown("""
<style>
.stApp {
    background-color: #f1f8e9;
}


h1, h2, h3 {
    color: #1b5e20 !important;
}

.stApp p,
.stApp label {
    color: #37474f;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3 {
    color: #1b5e20 !important;
}


/* Make plant analysis text readable */
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    color: #37474f !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
    color: #1b5e20 !important;
}

.stButton > button {
    background-color: #2e7d32;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1b5e20;
    color: white;
}

[data-testid="stFileUploader"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px dashed #66bb6a;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 SmartPlantCare")
st.subheader("Plant Disease Early Warning System")

st.markdown("""
<div style="
    background: linear-gradient(135deg, #dcedc8, #a5d6a7);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin: 20px 0;
">
    <h2 style="color: #1b5e20;">
        🌿 Welcome to SmartPlantCare!
    </h2>
    <p style="color: #234b24; font-size: 17px;">
        Upload a plant leaf image to check its health
        and discover possible disease or pest symptoms.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center; color:#1b5e20;">
🌱 What Can SmartPlantCare Do?
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background:white; padding:20px;
    border-radius:12px; text-align:center;
    border:1px solid #c8e6c9; min-height:150px;">
        <h2>📸</h2>
        <h4 style="color:#1b5e20;">Upload Image</h4>
        <p>Upload a clear picture of your plant leaf.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:white; padding:20px;
    border-radius:12px; text-align:center;
    border:1px solid #c8e6c9; min-height:150px;">
        <h2>🔍</h2>
        <h4 style="color:#1b5e20;">Analyze Symptoms</h4>
        <p>Check visible symptoms and possible causes.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:white; padding:20px;
    border-radius:12px; text-align:center;
    border:1px solid #c8e6c9; min-height:150px;">
        <h2>🌿</h2>
        <h4 style="color:#1b5e20;">Plant Care Tips</h4>
        <p>Get suggestions for your plant's care.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        image.thumbnail((1024, 1024))

        st.image(
            image,
            caption="Uploaded plant leaf",
            use_container_width=True
        )

    except Exception:
        st.error("Invalid image. Please upload a valid JPG or PNG.")
        st.stop()


    if st.button("Analyze Plant 🌿"):
        with st.spinner("Analyzing plant image..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash", 
                     contents=[
                        """
                        Analyze this plant leaf image for possible
                        disease symptoms.

                        Explain:
                        1. Visible symptoms
                        2. Possible disease, if identifiable
                        3. Confidence and limitations
                        4. Recommended next steps

                        Do not claim a definite diagnosis if the
                        image is unclear. If unsure, say so.
                        """,
                        image
                    ]
                )

                st.subheader("Plant Health Analysis")
                st.write(response.text)


            except Exception as e:
                st.error(
                    "Analysis failed. Check your API key, "
                    "model availability, and internet connection."
                )
                st.caption(str(e))


st.markdown("""
<hr style="border: 1px solid #a5d6a7; margin-top: 30px;">

<div style="background: linear-gradient(135deg, #dcedc8, #f1f8e9);
            padding: 25px 15px; border-radius: 15px;
            text-align: center; margin-top: 15px;">

<h2 style="color: #1b5e20;">🌱 SmartPlantCare</h2>

<p style="color: #33691e;">
Helping you identify plant health problems early
and care for your plants better.
</p>

<p style="color: #37474f;">
<b>Our Features</b><br>
Plant Disease Detection | Symptom Analysis |
Plant Care Recommendations
</p>

<p style="color: #52734d; font-size: 14px;">
Disclaimer: AI results are suggestions and
are not a confirmed diagnosis.
</p>

<hr style="border: 0; border-top: 1px solid #c8e6c9;">

<p style="color: #52734d; font-size: 13px;">
© 2026 SmartPlantCare. All rights reserved.
</p>

<p style="color: #789078; font-size: 12px;">
Made with 🌿 for healthier plants.
</p>

</div>
""", unsafe_allow_html=True)

