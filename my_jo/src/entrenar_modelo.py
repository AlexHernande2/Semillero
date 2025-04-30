import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('C:/Users/edwin/OneDrive/Desktop/Semillero/my_jo/src/Otro.csv', encoding='latin1', delimiter=';')

#Corregir posibles problemas en los nombres de columnas
df.columns = df.columns.str.strip()  # Elimina espacios ocultos
df.columns = df.columns.str.replace('Ã©', 'é')  # Corregir caracteres especiales
df.columns = df.columns.str.replace('Ã±', 'ñ')
df.columns = df.columns.str.replace('ï»¿', '')  # Eliminar caracteres invisibles del inicio

# Ver las primeras filas del dataset
print("Filas del dataset")
print(df.head())

print("Verificicación si alguna dila tiene valores nulos")
print(df.isnull().sum())


df = df.dropna()

describe = df.describe()
print("Lineas \n",describe)

label_encoders = {}  # Diccionario para almacenar los codificadores de cada columna
#df.select_dtypes(include=['object']).columns obtiene todas la col q contienen texto (object pandas)
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])  # Convierte a números
    label_encoders[column] = le
    print(f"\nCodificación para la columna: {column}")
    for original, code in zip(le.classes_, le.transform(le.classes_)):
        print(f"{original} → {code}")
        

# #features
X = df.drop(columns=['Sitio1', 'Sitio2', 'Sitio3'])  #drop es para que evite esas columnas no las tenga en cuenta
#targets
y = df[['Sitio1', 'Sitio2', 'Sitio3']]

#size 20% para prueba y el otro 80 para entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Se crea un clasificador de Bosques Aleatorios con 100 árboles.
base_model = RandomForestClassifier(n_estimators=100, random_state=42)
model = MultiOutputClassifier(base_model)
#Se entrena el modelo
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Calcular la precisión para cada sitio por separado
accuracies = []
for i, col in enumerate(y_test.columns):
    acc = accuracy_score(y_test[col], y_pred[:, i])  # Comparar valores reales con predicciones
    print(f'Precisión para {col}: {acc * 100:.2f}%')
    accuracies.append(acc)
# Calcular el promedio de precisión
average_accuracy = sum(accuracies) / len(accuracies)
print(f'Precisión promedio del modelo: {average_accuracy * 100:.2f}%')


for sitio in ['Sitio1', 'Sitio2', 'Sitio3']:
    print(f"\nDistribución de clases en {sitio}:")
    print(df[sitio].value_counts().head(10))  # ver los más comunes


#  nuevos datos en un DataFrame 
new_data = pd.DataFrame({
    'Edad': [40],
    'Sexo': ['M'],
    'Tiempo disponible': [2],
    'Interes': ['Comida'],
    'subInteres': ['Rapida'],
})


for column in new_data.select_dtypes(include=['object']).columns:
    if column in label_encoders:
        # Si el valor no está en las clases conocidas, asignamos -1
        new_data[column] = new_data[column].apply(lambda x: label_encoders[column].transform([x])[0] if x in label_encoders[column].classes_ else -1)


# Hacer la predicción
predicted_sites = model.predict(new_data)
print(f'Sitios de interés predichos: {predicted_sites}')

predicted_sites = model.predict(new_data)
sitios_predichos = predicted_sites[0]  # Extrae la primera fila de predicciones

#Crear un diccionario para almacenar los sitios en texto
sitios_texto = {}

# Convertir automáticamente cada sitio numérico a texto
for i, sitio_col in enumerate(['Sitio1', 'Sitio2', 'Sitio3']):
    sitios_texto[sitio_col] = label_encoders[sitio_col].inverse_transform([sitios_predichos[i]])[0]


# Imprimir los sitios predichos en texto
for sitio, nombre in sitios_texto.items():
    print(f"{sitio}: {nombre}")

import joblib

# Guardar modelo y codificadores
#C:\Users\edwin\OneDrive\Desktop\Semillero\my_jo\src
joblib.dump(model, 'modelo_entrenado.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Modelo y codificadores guardados!")