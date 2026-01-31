📊 Customer Churn Prediction System
📋 Overview
This project is a Machine Learning Web Application designed to predict the likelihood of a customer leaving a service (Churn). It utilizes a Random Forest/XGBoost backend (depending on your model) to analyze customer behavior—such as contract type, monthly charges, and technical support usage—to provide real-time predictions.

🚀 Key Features
Modern Glassmorphism UI: A sleek, responsive dashboard built with a unified HTML5/CSS3 interface.

Real-time Prediction: Immediate feedback on whether a customer is "Likely to Churn" or "Happy to Stay."

Comprehensive Data Input: Capture 19 distinct customer attributes, including tenure, payment methods, and service types.

Actionable Insights: Highlighting specific risk factors based on customer profile inputs.

🧠 The Machine Learning Workflow
The application follows a standard data science pipeline to ensure high accuracy in predictions:

Data Ingestion: Loading historical telecom/customer data.

Preprocessing: Handling missing values, encoding categorical variables (One-Hot Encoding), and scaling numerical features.

Model Training: Using ensemble methods to capture complex patterns in customer behavior.

Deployment: Serving the model via a Flask API to this front-end interface.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Custom Glassmorphism), Bootstrap 4, Google Fonts (Poppins).

Backend: Flask (Python).

Machine Learning: Scikit-Learn, Pandas, NumPy.

Environment: Jinja2 Template Engine.

⚙️ Installation & Setup
Clone the repository

Bash
git clone https://github.com/AweshAlam/Churn-Prediction-System.git
cd Customer-Churn-Prediction
Install Dependencies

Bash
pip install -r requirements.txt
Run the Application

Bash
python app.py
The app will be available at http://127.0.0.1:5000/.

📁 Project Structure
Plaintext
├── app.py              # Flask Application logic
├── model.pkl           # Pre-trained ML Model
├── templates/
│   └── index.html      # Unified UI (HTML + CSS)
├── static/
│   ├── mystyle.css     # Additional stylesheets
└── requirements.txt    # Project dependencies
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.

Developed with ❤️ by Awesh
