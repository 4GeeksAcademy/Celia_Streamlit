import streamlit as st
import pandas as pd
from utils import predict_medical_charge, custom_transform
import numpy as np

# Título de la aplicación
st.title('Predicción aproximada del coste de su seguro médico desde un archivo CSV')
st.image('Captura.JPG', use_column_width=True)

# Widget para cargar un archivo CSV
uploaded_file = st.file_uploader("Seleccione un archivo CSV", type=['csv'])

# Si se carga un archivo
if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Mostrar una vista previa de los primeros registros del DataFrame
    st.write('**Vista Previa del DataFrame:**')
    st.write(df.head())

    # Sección para realizar la predicción
    st.subheader('Realizar la predicción')

    columns = ['age', 'smoker']

    # Widget para seleccionar las columnas a utilizar para la predicción
    feature_cols = st.multiselect('Selecciona las columnas para la predicción', df.columns)

    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Realizar Predicción con CSV'):
        # Realizar la predicción utilizando las columnas seleccionadas
        predicted_values = predict_medical_charge(df[feature_cols])
        rounded_predictions = np.exp(predicted_values).round(2)

        # Mostrar los resultados de la predicción
        st.success('Éxito al realizar la predicción!')
        st.write('Los resultados de la predicción son:')
        st.write(pd.DataFrame(rounded_predictions))
       

        # Convertir los resultados de la predicción a un DataFrame
        predictions_df = pd.DataFrame(rounded_predictions, columns=['Predicciones'])

        # Widget para descargar el archivo CSV de las predicciones
        st.subheader('Descargar Predicciones como CSV')
        st.download_button(label='Descargar CSV',
            data=predictions_df.to_csv(index=False),
            file_name='predicciones.csv',
            mime='text/csv')