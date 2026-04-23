# 🌦️🌈✨ SUPER PROYECTO DE TRATAMIENTO DE DATOS METEOROLÓGICOS 🌡️🔥🚀✨

¡BIENVENIDO/A AL MEJOR SISTEMA DE GESTIÓN DE TEMPERATURAS DE **A CORUÑA**! 🌊🏙️💎 Disfruta de una experiencia meteorológica EXTREMA potenciada por Python y Streamlit. 🐍🚀🌈💥

## 🌟🚀 ¿QUÉ HACE ESTE INCREÍBLE Y MARAVILLOSO PROYECTO? 🌟🚀

Este repositorio galáctico está diseñado para:
1. 📥 **DESCARGAR** AUTOMÁTICAMENTE los datos climáticos diarios de la **AEMET** usando su API oficial. 🛰️📡🌍💫
2. 💾 **ALMACENAR** la información en una base de datos local súper robusta de **SQLite**. 🗄️💎🏛️🛡️
3. 🧹 **LIMPIAR** y procesar los datos para que brillen más que la estrella Polar. ☀️🧼✨💎
4. 📊 **VISUALIZAR** gráficas interactivas, dinámicas y coloridas que te dejarán sin palabras. 📈🔥🌈🎨🖼️

## 🛠️⚙️ COMPONENTES DEL SISTEMA ⚙️🛠️

### 🛰️⚡ `aemet.py`
El motor de extracción nuclear. 🚀🔋 Se conecta a la API de AEMET, pide los datos del último mes y los guarda con todo el amor del mundo en `aemet_coruña.db`. 🤖💖🛸🌌 ¡OJO CON LA API KEY! 🔑🤫🛡️

### 💎🏛️ `aemet_coruña.db`
Tu santuario sagrado de datos. 🏯🏰 Aquí descansan las temperaturas máximas registradas día tras día en la ciudad de cristal. 💤🌡️🏙️💎

### 🎨📈 `graficas.py`
¡LA MAGIA PURA! ✨🔮 Utiliza **Streamlit** y **Plotly** para crear un Dashboard de otro planeta. 📊🖼️🛸🪐 ¡Corregido y optimizado para mostrar la evolución mensual perfecta! 📅✅🚀

### 🧹👔 `limpieza_datos.py` 
El mayordomo de élite del código. El encargado de que cada bit esté en su sitio. 👔✨🧤🧼

## 🚀🔥 CÓMO PONERLO EN MARCHA (¡RÁPIDO!) 🔥🚀

1. 🎟️ Consigue tu API KEY en AEMET OpenData. 🔑✨
2. 🤫 Crea un archivo `.env` con tu gran secreto: `API_KEY=tu_token_aqui`. 📝🛡️
3. 🏃‍♂️💨 Descarga los datos: 
   ```bash
   python aemet.py
   ```
4. 🎈🌈 Lanza el dashboard espectacular: 
   ```bash
   streamlit run graficas.py
   ```

## 📈🎯 MEJORAS RECIENTES (¡TODO RECIÉN SALIDO DEL HORNO!) 🎯📈
✅ **SOLUCIONADO**: Error de datos "por hora" que no existían. 🕒🚫🙌
✅ **NUEVO**: Visualización completa de **Temperaturas Máximas del Mes**. 📅✅🔥
✅ **NUEVO**: Métricas mensuales espectaculares para un análisis de alto nivel. 📊🎯💎

---
¡Hecho con muchísima ilusión, pasión y muchísimos, muchísimos emojis por tu asistente de confianza! 🥳🙌🎉✨🔝🚀🔥🌈💖🌍💫🛰️💎📊📈✅
