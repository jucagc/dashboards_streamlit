
import pandas as pd
import plotly.express as px


def crear_grafico(df):
    df_review = df.groupby('review_score').agg(
        Venta_total = ('cantidad_itens', 'sum')
    ).reset_index()
    
    
    colors = ['#0ba8fc', '#3795c7', '#105fd9', '#4c27f1', '#00cdff']
    
    fig = px.pie(df_review,
        values = 'Venta_total',
        names = 'review_score',
        title = 'Calificacion de las Ventas',
        color_discrete_sequence = colors
    )
    
    fig.update_layout(yaxis_title = 'Calificacion', xaxis_title = 'Ventas ($), showlegend = False')
    fig.update_traces(textposition = 'inside', textinfo = 'percent+label', insidetextfont = dict(size = 16)) 
    
    return fig

