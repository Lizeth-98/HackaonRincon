# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:58:00 2024

@author: josue
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Definición de los rangos para los parámetros
ph = ctrl.Antecedent(np.arange(0, 14, 0.1), 'pH')
tds = ctrl.Antecedent(np.arange(0, 2000, 1), 'TDS')

# Definición del rango para la calidad del agua
quality = ctrl.Consequent(np.arange(0, 101, 1), 'Calidad del Agua')

# Funciones de pertenencia para pH
ph['acido'] = fuzz.trapmf(ph.universe, [0, 0, 4.5, 6.5])
ph['neutro'] = fuzz.trimf(ph.universe, [6, 7, 8])
ph['alcalino'] = fuzz.trapmf(ph.universe, [7.5, 9.5, 14, 14])

# Funciones de pertenencia para TDS
tds['bajo'] = fuzz.trapmf(tds.universe, [0, 0, 300, 500])
tds['medio'] = fuzz.trimf(tds.universe, [400, 1000, 1600])
tds['alto'] = fuzz.trapmf(tds.universe, [1500, 1700, 2000, 2000])

# Funciones de pertenencia para la Calidad del Agua
quality['mala'] = fuzz.trapmf(quality.universe, [0, 0, 25, 50])
quality['regular'] = fuzz.trimf(quality.universe, [25, 50, 75])
quality['buena'] = fuzz.trapmf(quality.universe, [50, 75, 100, 100])

# Definición de las reglas difusas
rule1 = ctrl.Rule(ph['acido'] & tds['alto'], quality['mala'])
rule2 = ctrl.Rule(ph['neutro'] & tds['medio'], quality['regular'])
rule3 = ctrl.Rule(ph['alcalino'] & tds['bajo'], quality['buena'])
rule4 = ctrl.Rule(ph['neutro'] & tds['bajo'], quality['buena'])
rule5 = ctrl.Rule(ph['neutro'] & tds['alto'], quality['mala'])
rule6 = ctrl.Rule(ph['acido'] & tds['medio'], quality['regular'])
rule7 = ctrl.Rule(ph['alcalino'] & tds['medio'], quality['regular'])
rule8 = ctrl.Rule(ph['acido'] & tds['bajo'], quality['mala'])
rule9 = ctrl.Rule(ph['alcalino'] & tds['alto'], quality['mala'])

# Controlador difuso
quality_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
quality_sim = ctrl.ControlSystemSimulation(quality_ctrl)

# Datos de ejemplo (puedes reemplazar estos datos con los datos reales de tus sensores)
ph_values = np.array([7.5, 6.5, 8, 5, 7, 9, 6, 8.5, 7.2, 7.8])
tds_values = np.array([300, 400, 1500, 800, 700, 1800, 450, 200, 600, 1000])
quality_values = []

# Realizar la simulación para cada conjunto de datos
for ph_value, tds_value in zip(ph_values, tds_values):
    quality_sim.input['pH'] = ph_value
    quality_sim.input['TDS'] = tds_value
    quality_sim.compute()
    quality_values.append(quality_sim.output['Calidad del Agua'])

quality_values = np.array(quality_values)

# Realizar la regresión lineal múltiple
X = np.column_stack((ph_values, tds_values))
y = quality_values

regressor = LinearRegression()
regressor.fit(X, y)

# Predicciones del modelo de regresión
y_pred = regressor.predict(X)

# Imprimir los coeficientes de la regresión
print("Coeficientes de la regresión lineal múltiple:")
print(f"Intercepto: {regressor.intercept_}")
print(f"Coeficiente para pH: {regressor.coef_[0]}")
print(f"Coeficiente para TDS: {regressor.coef_[1]}")

# Gráfica de resultados
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(y, label='Valores calculados por Lógica Difusa', marker='o')
plt.plot(y_pred, label='Valores predichos por Regresión Lineal', linestyle='--', marker='x')
plt.title('Calidad del Agua: Lógica Difusa vs. Regresión Lineal')
plt.xlabel('Índice de muestra')
plt.ylabel('Calidad del Agua')
plt.legend()

plt.subplot(2, 1, 2)
plt.scatter(y, y_pred)
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--')
plt.title('Valores Reales vs. Valores Predichos')
plt.xlabel('Valores calculados por Lógica Difusa')
plt.ylabel('Valores predichos por Regresión Lineal')

plt.tight_layout()
plt.show()

# Evaluación del modelo
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Coeficiente de Determinación (R^2): {r2:.2f}")

# Predicción de la calidad del agua con el modelo de regresión lineal para un nuevo conjunto de datos
new_ph_value = 7.5
new_tds_value = 300

new_quality_value = regressor.predict([[new_ph_value, new_tds_value]])
print(f"\nPredicción de la Calidad del Agua con Regresión Lineal: {new_quality_value[0]:.2f}")
