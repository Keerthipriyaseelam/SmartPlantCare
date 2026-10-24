# 🌱 SmartPlantCare – Plant Disease Early Warning System

## About
SmartPlantCare is an AI-powered web application that analyzes plant leaf images to identify visible symptoms, explore possible disease causes, and provide plant care recommendations.

## Features
- Upload plant leaf images (JPG, JPEG, PNG).
- Analyze visible symptoms using Google Gemini AI.
- Identify possible diseases or pest-related damage.
- Receive plant care and prevention suggestions.
- Simple, user-friendly interface built with Streamlit.

## Technologies Used
Python | Streamlit | Google Gemini AI | Pillow | python-dotenv

## Installation & Usage
1. Install the required packages:
   ```bash
   pip install streamlit google-genai python-dotenv pillow
   ```
2. Create a `.env` file and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Security
Keep your API key private. Never upload your `.env` file to GitHub.

## Disclaimer
AI results are possible assessments, not confirmed diagnoses. Accuracy depends on image quality and model performance.

## License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.
