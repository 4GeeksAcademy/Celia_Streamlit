import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
import pandas as pd

def main():
    st.title('Sinitas Valencia: cuidamos de ti')

    # Agregar el GIF de Lottie
    st_lottie_url = "https://lottie.host/bf7c272f-fc7b-4398-9483-2efb1a114e45/MxxSjX48OV.json"
    st_lottie_component = st_lottie(st_lottie_url, width=600, height=300)


    st.write('**Por favor, seleccione el servicio predictivo que desea utilizar**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('Predicción seguro médico (con CSV)', 'Predicción seguro médico (manualmente)'), 
                      index=0, 
                      key='option')
    
    if st.button('Predecir'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Predicción seguro médico (con CSV)':
        switch_page("pred_charge_csv")
    elif opcion == 'Predicción seguro médico (manualmente)':
        switch_page("pred_charge_man")

if __name__ == "__main__":
    main()