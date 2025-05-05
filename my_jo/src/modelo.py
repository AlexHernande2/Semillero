import joblib
import pandas as pd

# Cargar modelo y encoders
modelo = joblib.load('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/Semillero/my_jo/src/modelo_entrenado.pkl')
label_encoders = joblib.load('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/Semillero/my_jo/src/label_encoders.pkl')

def predecir_sitios(datos_usuario):
    # Convertir a DataFrame
    new_data = pd.DataFrame([datos_usuario])
    
    # Codificar variables categóricas
    for col in new_data.select_dtypes(include=['object']).columns:
        new_data[col] = new_data[col].apply(
            lambda x: label_encoders[col].transform([x])[0] 
            if x in label_encoders[col].classes_ else -1
        )
    
    # Hacer predicción
    predicted = modelo.predict(new_data)
    
    # Decodificar resultados
    sitios = []
    for i, col in enumerate(['Sitio1', 'Sitio2', 'Sitio3']):
        sitio = label_encoders[col].inverse_transform([predicted[0][i]])[0]
        sitios.append(sitio)
    
    return sitios