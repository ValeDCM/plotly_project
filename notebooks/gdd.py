import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión