from flask import Flask, render_template, request
import pickle
import numpy as np
import os  

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Creating full dynamic addresses of model and scalar files
model_path = os.path.join(BASE_DIR, 'svm_model_for_something.sav')
scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')

# Loading models and scalars
model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect user input
            pclass = float(request.form['Pclass'])
            sex = float(request.form['encoded_Sex'])
            age = float(request.form['Age'])
            sibsp = float(request.form['SibSp'])
            parch = float(request.form['Parch'])
            fare = float(request.form['Fare'])
            embarked = int(request.form['encoded_Embarked'])
            
            # Encoding logic (Input processing)
            emb_q = 1 if embarked == 1 else 0
            emb_s = 1 if embarked == 2 else 0

            # Data Processing and Prediction
            features = np.array([[pclass, sex, age, sibsp, parch, fare, emb_q, emb_s]])
            scaled_features = scaler.transform(features)  # Scaling the input
            prediction = model.predict(scaled_features)[0] # Getting results from the model
            
            output = "Survived" if prediction == 1 else "Not Survived"
            return render_template('index.html', prediction_text=f"Result: {output}")
        
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)