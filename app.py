from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

# List of 39 features (replace with your actual names)
feature_names = [
    "Age", "Policy_Sales_Channel", "Insured_Amount", "Claim_Amount",
    "Vehicle_Age", "Vehicle_Damage", "Annual_Premium", "Days_Since_Last_Claim",
    "Region_Code", "Policy_Type", "Customer_Tenure", "Num_Policies",
    "Vehicle_Type", "Vehicle_Make", "Vehicle_Model", "Gender",
    "Marital_Status", "Education_Level", "Occupation", "Num_Accidents",
    "Previous_Claims", "Claim_Type", "Policy_Creation_Year", "Policy_Expiry_Year",
    "Driving_Experience", "No_Claim_Bonus", "Agent_ID", "Claim_Submitted_Days",
    "Insured_History", "Fraud_Score", "Police_Report_Flag", "Claim_Description_Length",
    "Reported_Late", "Hospitalized", "Police_Involved", "Witness_Count",
    "Repair_Cost", "Claim_Processing_Time", "Region_Score"
]

@app.route('/')
def home():
    return render_template("index.html", feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = []
        for feature in feature_names:
            features.append(float(request.form[feature]))

        input_array = np.array([features])
        prediction = model.predict(input_array)

        result = "Fraudulent Claim" if prediction[0] == 1 else "Legitimate Claim"
        return render_template("index.html", prediction_text=result, feature_names=feature_names)

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", prediction_text="Error in input", feature_names=feature_names)
# Run app
if __name__ == "__main__":
    app.run(debug=True)