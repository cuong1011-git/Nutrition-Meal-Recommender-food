# AI Web Application for Personalized Nutrition Meal Recommendation

This project is an AI-powered web application that recommends personalized daily meal plans based on body metrics and underlying health conditions. It uses **Rule-Based Filtering** to eliminate unsuitable foods and a **Constraint Satisfaction Problem (CSP)** solver to optimize meal combinations.

## Features
- **Rule-Based Filtering:** Filters out foods that violate dietary restrictions for Diabetes, Hypertension, Heart Disease, and Obesity.
- **CSP Meal Planner:** Generates a daily meal plan (Breakfast, Lunch, Dinner, Snack) that satisfies caloric and macronutrient constraints.
- **Interactive UI:** Built with Streamlit for a seamless user experience.
- **EDA & Evaluation:** Includes data visualization and model performance metrics.

## Installation Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nutrition-meal-recommender.git
   cd nutrition-meal-recommender
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Locally

Execute the following command in your terminal:
```bash
streamlit run app.py
```
The application will open in your default web browser.

## How to Deploy on Streamlit Community Cloud

1. Push your code to a public GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click "New app".
4. Select your repository, branch, and set the main file path to `app.py`.
5. Click "Deploy". Your app will be live in a few minutes!
