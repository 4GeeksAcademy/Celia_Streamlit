import streamlit as st
import pandas as pd
from utils import predict_medical_charge, custom_transform
import numpy as np

# Título de la aplicación
st.title('Predicción aproximada del coste de su seguro médico')
st.image('sanidad.jpg', use_column_width=True)

# Texto introductorio
st.write('**Por favor, ingrese estos datos personales para realizar la predicción:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características de la flor
columns = ['age', 'smoker']

# Bucle para recorrer las columnas y obtener los datos de entrada
for col in columns:
    if col == 'age':
        input_data[col] = st.slider(col, min_value=0, max_value=100, value=35, step=1)
    elif col == 'smoker':
        input_data[col] = 1 if st.selectbox(col, options=["Sí", "No"]) == "Sí" else 0
        #input_data[col] = st.selectbox(col, options=["Sí", "No"])

#imput_data = {col: (st.slider(col, min_value=0, max_value=100, value=35, step=1) if col == 'Edad del interesado' else st.selectbox(col, options=["Sí", "No"])) for col in columns}


# Botón para realizar la predicción
if st.button('Predicción'):
    # Convertir el diccionario de entrada a un DataFrame de una sola fila
    input_df = pd.DataFrame([input_data])

    # Realizar la predicción utilizando la función predict_flores
    predicted_value = predict_medical_charge(input_df)

    # Mostrar el resultado de la predicción
    st.success('Éxito al realizar la predicción!')

    st.write(f'Coste anual de su seguro médico: {round(np.exp(predicted_value[0]), 2)} $')
 