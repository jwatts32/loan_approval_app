import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_lgbm_model.pkl')

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")
st.title("🏦 Loan Approval Predictor")

st.markdown("Enter applicant details below to predict whether a loan will be approved or rejected.")

# Input form
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
dependents = st.selectbox("Number of Dependents", ['0', '1', '2', '3+'])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=1)
credit_history = st.selectbox("Credit History", ["Yes", "No"])
credit_history = 1.0 if credit_history == "Yes" else 0.0
area = st.selectbox("Area", ['Urban', 'Rural', 'Semiurban'])

# One-hot encoding for categorical variables
input_data = {
    'Applicant_Income': app_income,
    'Coapplicant_Income': coapp_income,
    'Loan_Amount': loan_amount,
    'Credit_History': credit_history,

    # Gender
    'Gender_Female': int(gender == 'Female'),
    'Gender_Male': int(gender == 'Male'),

    # Married
    'Married_No': int(married == 'No'),
    'Married_Yes': int(married == 'Yes'),

    # Education
    'Education_Graduate': int(education == 'Graduate'),
    'Education_Not Graduate': int(education == 'Not Graduate'),

    # Self Employed
    'Self_Employed_No': int(self_employed == 'No'),
    'Self_Employed_Yes': int(self_employed == 'Yes'),

    # Area
    'Area_Rural': int(area == 'Rural'),
    'Area_Semiurban': int(area == 'Semiurban'),
    'Area_Urban': int(area == 'Urban'),

    # Dependents
    'Dependents_0': int(dependents == '0'),
    'Dependents_1': int(dependents == '1'),
    'Dependents_2': int(dependents == '2'),
    'Dependents_3+': int(dependents == '3+'),
}

# Convert input to DataFrame
feature_names = joblib.load('model_features.pkl')
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_names, fill_value=0)

# Prediction
if st.button("Predict Loan Status"):
    prediction = model.predict(input_df)[0]
    prediction_label = "✅ Approve" if prediction == 1 else "❌ Reject"
    st.success(f"Prediction: {prediction_label}")
