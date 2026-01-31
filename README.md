# 📊 Customer Churn Prediction System

A full-stack **Machine Learning Web Application** that predicts the likelihood of a customer leaving a service (**Customer Churn**). The system combines a modern, glassmorphism-inspired UI with a robust ML backend to deliver fast, interpretable churn predictions.

---
## Live
https://churn-prediction-system-uw0i.onrender.com/

## 📋 Overview

Customer retention is critical for subscription-based businesses. This project leverages supervised machine learning models (Random Forest / XGBoost, depending on configuration) to analyze customer behavior—such as contract type, tenure, monthly charges, and support usage—and generate real-time churn predictions through a web interface.

The application is designed to be **simple to run locally**, **easy to extend**, and **production-ready** with minimal modifications.

---

## 🚀 Key Features

* **Modern Glassmorphism UI**
  Sleek, responsive dashboard using HTML5, CSS3, and Bootstrap 4.

* **Real-Time Predictions**
  Instantly classifies customers as **"Likely to Churn"** or **"Happy to Stay"**.

* **Comprehensive Data Input**
  Accepts **19 customer attributes**, including:

  * Tenure
  * Monthly & Total Charges
  * Contract Type
  * Payment Method
  * Internet & Technical Support Services

* **Actionable Insights**
  Highlights potential churn risk factors based on user input.

---

## 🧠 Machine Learning Workflow

The project follows a standard, industry-grade data science pipeline:

1. **Data Ingestion**
   Historical telecom/customer churn dataset loading.

2. **Preprocessing**

   * Handling missing values
   * Encoding categorical features (One-Hot Encoding)
   * Scaling numerical variables

3. **Model Training**

   * Ensemble learning (Random Forest / XGBoost)
   * Optimized for classification accuracy and generalization

4. **Deployment**

   * Trained model serialized (`model.pkl`)
   * Served via a Flask backend

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3 (Custom Glassmorphism Design)
* Bootstrap 4
* Google Fonts (Poppins)

### Backend

* Flask (Python)
* Jinja2 Template Engine

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AweshAlam/Churn-Prediction-System.git
cd Customer-Churn-Prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Access the App

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
├── app.py              # Flask application logic
├── model.pkl           # Pre-trained machine learning model
├── templates/
│   └── index.html      # Unified UI (HTML + embedded CSS)
├── static/
│   └── mystyle.css     # Additional custom styles
└── requirements.txt    # Project dependencies
```

---

## 📈 Future Improvements

* Add probability scores for churn predictions
* Integrate SHAP/LIME for model explainability
* Deploy on cloud platforms (AWS / Render / Heroku)
* Add authentication and user management
* Support multiple ML models via model switching

---

## 🤝 Contributing

Contributions are welcome and greatly appreciated!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute.

---

## ❤️ Author

Developed with passion by **Awesh Alam**
If you found this project useful, consider giving it a ⭐ on GitHub!
