# predictor.py
import json
import joblib
import pandas as pd

class SitiosRecomendador:
    def __init__(self, modelo_path='modelo_entrenado.pkl', json_path='usuarios.json'):
        self.model = joblib.load(modelo_path)  # Cargar modelo
        self.label_encoders = joblib.load('label_encoders.pkl')  # Cargar codificadores
        self.json_path = json_path

    def predecir_sitios(self, cedula):
        # Abrir el JSON de usuarios
        with open(self.json_path, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)

        # Si la cédula no existe
        if cedula not in usuarios:
            return None

        datos = usuarios[cedula]  # Datos del usuario

        # Convertir los datos a DataFrame (lo que pide el modelo)
        df = pd.DataFrame([datos])

        # Codificar texto a números
        for col in df.select_dtypes(include=['object']).columns:
            if col in self.label_encoders:
                df[col] = df[col].apply(
                    lambda x: self.label_encoders[col].transform([x])[0]
                    if x in self.label_encoders[col].classes_ else -1
                )

        # Predecir con el modelo
        pred = self.model.predict(df)[0]

        # Convertir los resultados de números a texto
        sitios = {}
        for i, col in enumerate(['Sitio1', 'Sitio2', 'Sitio3']):
            sitios[col] = self.label_encoders[col].inverse_transform([pred[i]])[0]

        return sitios
    
    print ("No hay problemas prueba")