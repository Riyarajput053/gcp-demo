import pickle
import numpy as np

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_species(data):
    prediction = model.predict([data])
    return int(prediction[0])
