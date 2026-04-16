import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go

# Cargar datos desde SQLite
def get_datos():
    conn = sqlite3.connect('meteorologia.db')
    df = pd.read_sql_query('''
        SELECT fint, tamax 
        FROM temperaturas 
        ORDER BY fint
    ''', conn)
    conn.close()
    df['hora'] = pd.to_datetime(df['fint']).dt.strftime('%H:%M')
    return df

df = get_datos()

# --- Layout de la app ---
st.title("Temperaturas máximas — ABANILLA")
st.caption("Estación 7250C · 16 de abril de 2026")

# Métricas resumen
col1, col2, col3 = st.columns(3)
col1.metric("Temp. máxima del día", f"{df['tamax'].max()} °C")
col2.metric("Temp. mínima del día", f"{df['tamax'].min()} °C")
col3.metric("Media", f"{df['tamax'].mean():.1f} °C")

# --- Gráfica combinada ---
fig = go.Figure()

# Barras azules
fig.add_trace(go.Bar(
    x=df['hora'],
    y=df['tamax'],
    name='Temp. máxima (barras)',
    marker_color='steelblue',
    opacity=0.7
))

# Línea roja
fig.add_trace(go.Scatter(
    x=df['hora'],
    y=df['tamax'],
    name='Temp. máxima (línea)',
    mode='lines+markers',
    line=dict(color='red', width=2.5),
    marker=dict(color='red', size=6)
))

# Estilo del gráfico
fig.update_layout(
    title='Temperatura máxima por hora',
    xaxis_title='Hora',
    yaxis_title='Temperatura (°C)',
    legend=dict(orientation='h', y=-0.2),
    hovermode='x unified',
    plot_bgcolor='white',
    yaxis=dict(gridcolor='lightgrey')
)

st.plotly_chart(fig, use_container_width=True)

# Tabla de datos
with st.expander("Ver datos completos"):
    st.dataframe(df[['hora', 'tamax']].rename(columns={
        'hora': 'Hora',
        'tamax': 'Temp. máxima (°C)'
    }), use_container_width=True)