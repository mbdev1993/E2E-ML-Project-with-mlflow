from flask import Flask, render_template, request
import os
import flask
import numpy as np
import pandas as pd
from mlProject.pipelines.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def training():
    os.system('python main.py')
    return "Training Completed"

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "fixed acidity": [float(request.form["fixed_acidity"])],
        "volatile acidity": [float(request.form["volatile_acidity"])],
        "citric acid": [float(request.form["citric_acid"])],
        "residual sugar": [float(request.form["residual_sugar"])],
        "chlorides": [float(request.form["chlorides"])],
        "free sulfur dioxide": [float(request.form["free_sulfur_dioxide"])],
        "total sulfur dioxide": [float(request.form["total_sulfur_dioxide"])],
        "density": [float(request.form["density"])],
        "pH": [float(request.form["pH"])],
        "sulphates": [float(request.form["sulphates"])],
        "alcohol": [float(request.form["alcohol"])]
    }

    df = pd.DataFrame(data)

    obj = PredictionPipeline()
    prediction = obj.predict(df)

    return render_template(
        "results.html",
        prediction=round(float(prediction[0]), 2)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)