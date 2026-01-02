# 🚢 Titanic Survival Predictor - ML Web App

This is a **Machine Learning** web application that predicts the survival probability of Titanic passengers based on their profiles.

## 🚀 Project Overview
This project uses a **Support Vector Machine (SVM)** model to predict whether a passenger would have survived the Titanic disaster based on features like Age, Fare, Class, and Family details.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn, Pandas, Numpy, matplotlib, seaborn
- **Frontend:** HTML5, CSS3
- **Model Storage:** Pickle (`.sav` and `.pkl` files)

## 📂 File Structure
- `app.py`: The main Flask server file.
- `svm_model_for_something.sav`: The trained SVM model.
- `scaler.pkl`: The scaler used for data normalization.
- `templates/index.html`: The user interface for the web app.
- `train.csv`: The dataset used for training.

## 📊 Dataset Stats
Based on the Titanic dataset:
- **Age Range:** 0.42 to 80 years.
- **Fare Range:** 0 to 512.3292.
- **Siblings/Spouses Range:** 0 to 8.
- **Parents/Children Range:** 0 to 6.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `python app.py`.
