
import pandas as pd
import plotly.express as px


def crear_grafico(df):
    df_mapa = df.groupby('geolocation_state').agg({
    'Venta_total': 'sum',
    'geolocation_lat': 'mean',
    'geolocation_lng': 'mean'
    }).reset_index().sort_values(by='Venta_total', ascending = False)

    graf_mapa = px.scatter_geo(df_mapa, 
        lat = 'geolocation_lat',
        lon = 'geolocation_lng', 
        scope = 'south america',
        template = 'seaborn', 
        size = 'Venta_total',
        hover_name = 'geolocation_state', 
        hover_data = {'geolocation_lat': False, 'geolocation_lng': False}, 
        title = 'Ventas por Estado',
    )
    
    return graf_mapa