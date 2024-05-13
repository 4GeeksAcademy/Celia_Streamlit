import pickle
import streamlit as st
import tensorflow as tf
import joblib
import pandas as pd


def predict_medical_charge(data):
    # Cargar el modelo previamente entrenado para predecir el tipo de flor
    model = joblib.load('models/model_medical_charge.pkl')
    print(type(model))
    # Realizar la predicción con los datos proporcionados
    predictions = model.predict(data) 
    return predictions



def custom_transform(X):
  scaler = joblib.load('/workspaces/Celia_Streamlit/scaler_st.pkl')
  X_num = X.iloc[:, [0]]
  X_num_sc = scaler.transform(X_num)
  X_sc = pd.concat([pd.DataFrame(X_num_sc), X.iloc[:,[1]].reset_index(drop=True)], axis=1, ignore_index=True)

  return X_sc