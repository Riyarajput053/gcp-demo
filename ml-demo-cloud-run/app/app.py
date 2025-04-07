from flask import Flask, request, render_template
from app.utils import predict_species

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = predict_species(features)
    return f"Predicted Iris species class: {prediction}"
