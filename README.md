# 🚢 Titanic Survival Predictor - ML Web App

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-red.svg)
![Machine Learning](https://img.shields.io/badge/Model-SVM-orange.svg)
![Deployment](https://img.shields.io/badge/Hosted-Render-brightgreen.svg)

This repository contains a professional-grade, end-to-end Machine Learning application designed to predict passenger survival on the Titanic. The project integrates rigorous data science methodologies with a modern web interface to deliver real-time predictive analytics.

---

### 🔗 **Live Production Environment**
The application is fully deployed and accessible globally:
> **Deployment URL:** [https://titanic-survival-predictor-ml-web-app.onrender.com](https://titanic-survival-predictor-ml-web-app.onrender.com)

---

### 🚀 **Technical Architecture & Methodology**

#### **1. Mathematical Modeling (SVM)**
The engine utilizes a **Support Vector Machine (SVM)** classifier, chosen for its superior performance in high-dimensional feature spaces. The model focuses on optimizing the decision boundary to categorize survival outcomes with high precision.

#### **2. Advanced Data Pipeline**
* **EDA:** Comprehensive Exploratory Data Analysis conducted using **Matplotlib** and **Seaborn** to identify key correlations (e.g., Sex, Class, and Age).
* **Feature Engineering:** Strategic handling of missing values and categorical encoding.
* **Normalization:** Implementation of `StandardScaler` to ensure the SVM model's convergence and stability.

#### **3. Full-Stack Integration**
* **Backend:** A RESTful API built with **Flask** manages the inference requests.
* **Frontend:** A responsive UI developed with **HTML5** and **CSS3**, optimized for both desktop and mobile viewports.

---

### 🛠️ **Technological Ecosystem**

| Domain | Technology Stack |
| :--- | :--- |
| **Programming** | Python 3.11 |
| **Data Analytics** | Pandas, NumPy |
| **Model Development** | Scikit-learn (SVM, StandardScaler) |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Render, Gunicorn |

---

### 📂 **System Structure**
* `app.py`: The central controller for routing and prediction logic.
* `titanic_project.ipynb`: The complete R&D lifecycle including model validation.
* `svm_model_for_something.sav`: High-fidelity serialized model for low-latency inference.
* `requirements.txt`: Environment specification for reproducible builds.

---

### ⚙️ **Deployment & Local Execution**
1.  **Clone Repository:**
    ```bash
    git clone [https://github.com/sheikhemamul777/Titanic-Survival-Predictor-ML-Web-App.git](https://github.com/sheikhemamul777/Titanic-Survival-Predictor-ML-Web-App.git)
    ```
2.  **Environment Setup:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Initiate Application:**
    ```bash
    python app.py
    ```

---
© 2026 | Developed by Sheikh Emamul | Machine Learning Portfolio
