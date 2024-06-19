from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model/linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Render the index.html template
@app.route('/')
def home():
    return render_template('index.html')

# Handle the form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    age = float(request.form['age'])
    leaves_used = float(request.form['leavesUsed'])
    leaves_remaining = float(request.form['leavesRemaining'])
    ratings = float(request.form['ratings'])
    past_exp = float(request.form['pastExp'])
    sex = request.form['sex']
    designation = request.form['designation']
    unit = request.form['unit']

    # Convert categorical variables to one-hot encoding
    data = {
        'AGE': [age],
        'LEAVES USED': [leaves_used],
        'LEAVES REMAINING': [leaves_remaining],
        'RATINGS': [ratings],
        'PAST EXP': [past_exp],
        'SEX_F': [1 if sex == 'F' else 0],
        'SEX_M': [1 if sex == 'M' else 0],
        'DESIGNATION_Analyst': [1 if designation == 'Analyst' else 0],
        'DESIGNATION_Associate': [1 if designation == 'Associate' else 0],
        'DESIGNATION_Director': [1 if designation == 'Director' else 0],
        'DESIGNATION_Manager': [1 if designation == 'Manager' else 0],
        'DESIGNATION_Senior Analyst': [1 if designation == 'Senior Analyst' else 0],
        'DESIGNATION_Senior Manager': [1 if designation == 'Senior Manager' else 0],
        'UNIT_Finance': [1 if unit == 'Finance' else 0],
        'UNIT_IT': [1 if unit == 'IT' else 0],
        'UNIT_Management': [1 if unit == 'Management' else 0],
        'UNIT_Marketing': [1 if unit == 'Marketing' else 0],
        'UNIT_Operations': [1 if unit == 'Operations' else 0],
        'UNIT_Web': [1 if unit == 'Web' else 0]
    }

    # Create a DataFrame from the form data
    df = pd.DataFrame(data)

    # Make prediction
    prediction = model.predict(df)

    # Return the prediction
    return f"Predicted Salary: ${prediction[0]:,.2f}"
if __name__ == '__main__':
    app.run(debug=True)
