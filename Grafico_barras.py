import pandas as pd
import plotly.express as px


def crear_grafico(df):
    revenue_productos = df.groupby('product_category_name')[['Venta_total']].sum().sort_values('Venta_total', ascending = True).reset_index()
    
    
    fig = px.bar(revenue_productos.tail(10),
        x = 'Venta_total',
        y = 'product_category_name',
        text = 'Venta_total',
        title = 'Top 10 Categorias de Productos por Ventas'
    )
        
    fig.update_layout(yaxis_title = 'Productos', xaxis_title = 'Ingresos ($)', showlegend = False)
    fig.update_traces(texttemplate = '%{text:.3s}')
    
    return fig
