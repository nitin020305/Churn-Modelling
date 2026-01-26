from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('RF.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = 0
    churn_prob = 0.52
    features = None
    
    if request.method == 'POST':
        features = [
            float(request.form['credit_score']),
            float(request.form['age']),
            float(request.form['tenure']),
            float(request.form['balance']),
            float(request.form['num_products']),
            float(request.form['has_cr_card']),
            float(request.form['is_active']),
            float(request.form['salary']),
            float(request.form['geo_france']),
            float(request.form['geo_germany']),
            float(request.form['geo_spain']),
            1-float(request.form['gender_male']),
            float(request.form['gender_male'])
        ]
        features_array = np.array([features])
        prediction = int(model.predict(features_array)[0])
        churn_prob = float(model.predict_proba(features_array)[0][1])
    
    return render_template('index.html', 
                         prediction=prediction, 
                         churn_prob=churn_prob,
                         features=features)

if __name__ == '__main__':
    app.run(debug=True)
