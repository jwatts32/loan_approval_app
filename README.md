# loan_approval_app
Interactive app built with **Streamlit** utilizing **LightGBM** to predict if a loan app should be **approved** or **rejected** based on user input

## Features
- Manual input for users
- Provides data-based decision in real-time
- Mechanized by machine learning model that was trained on historical data

## How It Works

Uses a LightGBM model trained on features that include the following:

- Applicant Income
- Co-applicant Income
- Loan Amount
- Credit History
- Marital Status
- Gender
- Education
- Dependents
- Employment Status
- Property Area

Given the user's input, the model outputs a decision of **Approve** or **Reject**.

## Tech Stack
- Python
- pandas
- sklearn
- Logistic Regression
- Random Forest Classification
- LightGBM
- joblib
- Streamlit

## Setup Instructions
1. Clone repository:
   --bash
   git clone https://github.com/jwatts32/loan-approval-app.git
   cd loan-approval-app

2. Install dependencies:
     --bash
     pip install -r requirements.txt

3. Run the app:
     streamlit run loan_app.py

