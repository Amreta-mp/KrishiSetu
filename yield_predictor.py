import pandas as pd
import pickle

def predict_yield(features):
    model = pickle.load(open("models/yield_model.pkl", "rb"))
    return model.predict([features])[0]
