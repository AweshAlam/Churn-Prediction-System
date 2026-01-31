# coding: utf-8
import os
import pandas as pd
from flask import Flask, request, render_template
import pickle

# ✅ Correct Flask app initialization
app = Flask(__name__)

# ✅ Load model ONCE (important for Render)
MODEL_PATH = "model.sav"
model = pickle.load(open(MODEL_PATH, "rb"))

# ✅ Load dataset safely
DATA_PATH = "first_telc.csv"
df_1 = pd.read_csv(DATA_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        input_data = [
            request.form['query1'],
            request.form['query2'],
            request.form['query3'],
            request.form['query4'],
            request.form['query5'],
            request.form['query6'],
            request.form['query7'],
            request.form['query8'],
            request.form['query9'],
            request.form['query10'],
            request.form['query11'],
            request.form['query12'],
            request.form['query13'],
            request.form['query14'],
            request.form['query15'],
            request.form['query16'],
            request.form['query17'],
            request.form['query18'],
            request.form['query19'],
        ]

        columns = [
            'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',
            'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
            'InternetService', 'OnlineSecurity', 'OnlineBackup',
            'DeviceProtection', 'TechSupport', 'StreamingTV',
            'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod', 'tenure'
        ]

        new_df = pd.DataFrame([input_data], columns=columns)

        df_2 = pd.concat([df_1, new_df], ignore_index=True)

        labels = [f"{i} - {i+11}" for i in range(1, 72, 12)]
        df_2['tenure_group'] = pd.cut(
            df_2.tenure.astype(int),
            range(1, 80, 12),
            right=False,
            labels=labels
        )

        df_2.drop(columns=['tenure'], inplace=True)

        final_df = pd.get_dummies(df_2[
            ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
             'MultipleLines', 'InternetService', 'OnlineSecurity',
             'OnlineBackup', 'DeviceProtection', 'TechSupport',
             'StreamingTV', 'StreamingMovies', 'Contract',
             'PaperlessBilling', 'PaymentMethod', 'tenure_group']
        ])

        prediction = model.predict(final_df.tail(1))[0]
        probability = model.predict_proba(final_df.tail(1))[0][1] * 100

        if prediction == 1:
            o1 = "This customer is likely to churn ❌"
        else:
            o1 = "This customer is likely to continue ✅"

        o2 = f"Confidence: {probability:.2f}%"

        return render_template(
            "index.html",
            output1=o1,
            output2=o2,
            **{f"query{i+1}": input_data[i] for i in range(19)}
        )

    return render_template("index.html")


# ✅ Render / Docker entrypoint
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
