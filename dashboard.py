import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Análisis histórico de Bitcoin",
    page_icon="📊",
    layout="wide"
)

# Título y descripción
st.title("📊 Análisis histórico de Bitcoin")
st.markdown("Proyecto de análisis de datos aplicado al mercado financiero.")

# Cargar datos
@st.cache_data
def cargar_datos():
    btc = pd.read_csv("data/bitcoin_limpio.csv", parse_dates=["Date"])
    btc["rendimiento_diario"] = btc["Close"].pct_change()
    btc["volatilidad_30d"] = btc["rendimiento_diario"].rolling(30).std() * 100
    btc["Year"] = btc["Date"].dt.year
    btc["Month"] = btc["Date"].dt.month
    return btc

btc = cargar_datos()

# Calcular rendimiento anual (necesario para las métricas)
rendimiento_anual = btc.groupby("Year")["Close"].agg(inicio="first", fin="last")
rendimiento_anual["rendimiento"] = ((rendimiento_anual["fin"] - rendimiento_anual["inicio"]) / rendimiento_anual["inicio"] * 100).round(2)
rendimiento_anual = rendimiento_anual.reset_index()
rendimiento_anual["color"] = rendimiento_anual["rendimiento"].apply(lambda x: "Positivo" if x > 0 else "Negativo")

# Métricas resumen
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Precio actual", f"${btc['Close'].iloc[-1]:,.2f}")

with col2:
    st.metric("Máximo histórico", f"${btc['Close'].max():,.2f}")

with col3:
    mejor_año = rendimiento_anual.loc[rendimiento_anual['rendimiento'].idxmax(), 'Year']
    mejor_rendimiento = rendimiento_anual['rendimiento'].max()
    st.metric("Mejor año", f"{mejor_año}", f"{mejor_rendimiento:.0f}%")

with col4:
    peor_año = rendimiento_anual.loc[rendimiento_anual['rendimiento'].idxmin(), 'Year']
    peor_rendimiento = rendimiento_anual['rendimiento'].min()
    st.metric("Peor año", f"{peor_año}", f"{peor_rendimiento:.0f}%")


# Filtro por rango de fechas
st.subheader("Filtrar por período")
col_fecha1, col_fecha2 = st.columns(2)

with col_fecha1:
    fecha_inicio = st.selectbox("Desde", options=sorted(btc["Year"].unique()), index=0)

with col_fecha2:
    fecha_fin = st.selectbox("Hasta", options=sorted(btc["Year"].unique()), index=len(btc["Year"].unique())-1)

# Filtrar el dataframe según las fechas seleccionadas
btc_filtrado = btc[(btc["Year"] >= fecha_inicio) & (btc["Year"] <= fecha_fin)]


# Gráfico 1 - Evolución histórica del precio
st.subheader("Evolución histórica del precio de Bitcoin")
fig1 = px.line(btc_filtrado, x="Date", y="Close",
              labels={"Date": "Fecha", "Close": "Precio de cierre (USD)"},
              color_discrete_sequence=["orange"])
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2 - Volatilidad histórica
st.subheader("Volatilidad histórica de Bitcoin (30 días)")
fig2 = px.line(btc_filtrado, x="Date", y="volatilidad_30d",
              labels={"Date": "Fecha", "volatilidad_30d": "Volatilidad (%)"},
              color_discrete_sequence=["orange"])
st.plotly_chart(fig2, use_container_width=True)


# Gráfico 3 - Rendimiento anual
st.subheader("Rendimiento anual de Bitcoin")
rendimiento_anual = btc_filtrado.groupby("Year")["Close"].agg(inicio="first", fin="last")
rendimiento_anual["rendimiento"] = ((rendimiento_anual["fin"] - rendimiento_anual["inicio"]) / rendimiento_anual["inicio"] * 100).round(2)
rendimiento_anual = rendimiento_anual.reset_index()
rendimiento_anual["color"] = rendimiento_anual["rendimiento"].apply(lambda x: "Positivo" if x > 0 else "Negativo")
fig3 = px.bar(rendimiento_anual, x="Year", y="rendimiento",
              color="color",
              color_discrete_map={"Positivo": "green", "Negativo": "red"},
              labels={"Year": "Año", "rendimiento": "Rendimiento (%)", "color": ""})
st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4 - Volumen vs Precio
st.subheader("Relación entre volumen operado y precio promedio anual")
volumen_anual = btc_filtrado.groupby("Year")["Volume"].mean().reset_index()
precio_anual = btc_filtrado.groupby("Year")["Close"].mean().reset_index()
fig4 = px.bar(volumen_anual, x="Year", y="Volume",
              labels={"Year": "Año", "Volume": "Volumen promedio (USD)"},
              color_discrete_sequence=["steelblue"])
fig4.add_scatter(x=precio_anual["Year"], y=precio_anual["Close"],
                 mode="lines+markers", name="Precio promedio",
                 yaxis="y2", line=dict(color="orange"))
fig4.update_layout(yaxis2=dict(overlaying="y", side="right",
                               title="Precio promedio (USD)"))
st.plotly_chart(fig4, use_container_width=True)

# Gráfico 5 - Volatilidad mensual
st.subheader("Volatilidad promedio por mes")
meses = {1:"Ene", 2:"Feb", 3:"Mar", 4:"Abr", 5:"May", 6:"Jun",
         7:"Jul", 8:"Ago", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dic"}
volatilidad_mensual = btc_filtrado.groupby("Month")["volatilidad_30d"].mean().reset_index()
volatilidad_mensual["Mes"] = volatilidad_mensual["Month"].map(meses)
fig5 = px.bar(volatilidad_mensual, x="volatilidad_30d", y="Mes",
              orientation="h",
              labels={"volatilidad_30d": "Volatilidad (%)", "Mes": "Mes"},
              color_discrete_sequence=["steelblue"])
st.plotly_chart(fig5, use_container_width=True)
