<<<<<<< HEAD
# 🌦️🌡️ Proyecto de Tratamiento y Visualización de Datos Meteorológicos ☀️📊

¡Bienvenido/a al repositorio más ardiente (y refrescante) de toda la red! 🚀✨ Este espectacular proyecto ha sido diseñado para coger aburridos y caóticos datos textuales y convertirlos en **un dashboard asombroso y súper visual**. 🤩🔥 Si alguna vez has querido saber el calor que ha hecho en **Abanilla (Estación 7250C)** hora por hora, ¡este es tu lugar! 🌵🏜️🏖️

---

## 🌟 ¿De qué trata este increíble proyecto? 🧐💡

Básicamente, hacemos **magia con datos** 🪄✨. Tenemos lecturas de temperatura procedentes de nuestra querida estación meteorológica, y a través de la magia maravillosa de Python 🐍, procesamos todo ese texto, lo metemos limpito en una base de datos ultrarrápida 🗄️ y terminamos mostrando un dashboard interactivo alucinante donde puedes ver cómo han subido las temperaturas a lo largo del día. 📈🥵🥶

Todo el flujo de trabajo (Pipeline) 🌊 se divide en dos fases colosales:

1. **🧹 Limpieza y Almacenamiento (Extracción + Carga)** 
2. **🎨 Visualización Súper Épica (Dashboard interactivo)**

---

## 📁 🗺️ Estructura de nuestro asombroso Proyecto 📂🔍

¿Qué te vas a encontrar aquí? Pues te lo cuento con todo lujo de detalles: 👇👇

- 📄 **`datostemperatura.txt`** ➡️ Nuestra fuente de la verdad absoluta. 📜 Contiene toda la información de las temperaturas en formato crudo (JSON). ¡Aquí está la información pura! 💎
- 🧹 **`limpieza_datos.py`** ➡️ ¡El conserje de nuestro proyecto! 👨‍🔧 Este script escrito en Python coge el archivo de texto, lo lee, lo mima, y le quita las partes innecesarias para meter únicamente `fint` (la fecha/hora) y `tamax` (la temperatura máxima) directo al horno (la base de datos). 🔨🔧
- 🗄️ **`meteorologia.db`** ➡️ Nuestra poderosísima e invencible base de datos SQLite. ¡Guarda nuestros datos a salvo bajo 7 llaves! 🗝️🛡️
- 📊 **`graficas.py`** ➡️ ¡La superestrella de este show! 🌟🌍 Es una espectacular e inmaculada aplicación de **Streamlit** que se conecta a la base de datos, llama a **Pandas** 🐼 y grafica unos charts espectaculares gracias a **Plotly** 📈.

---

## 🛠️ ¿Qué Tecnologías Premium hemos usado? 💻🚀

Para llegar a este nivel de excelencia estadística y visual, hemos necesitado a los "Vengadores" de la analítica de datos: 🦸‍♂️🦸‍♀️

- **Python 🐍:** El rey indiscutible de lenguajes. Fácil, bonito y letal. 👑
- **SQLite 🗄️:** Ligero y potente, nadie guarda datos tan rápido sin necesidad de servidores extraños. ⚡
- **Pandas 🐼:** Nada de osos perezosos, aquí usamos Pandas para manipular DataFrames a la velocidad de la luz. 💨
- **Plotly 📉📊:** ¿Gráficos estáticos aburridos? ¡NO EN ESTE REPOSITORIO! 🙅‍♂️ Hacemos gráficos combinados interactivos con barras azules 🟦 y líneas rojas 🟥.
- **Streamlit 🎈✨:** La guinda del pastel 🍒. Construimos interfaces web preciosas en tiempo récord. ¡Streamlit es el MVP! 🏆

---

## 🚀 ¿Cómo poner a funcionar esta Nave Espacial? 🛸🌌

Si tú también quieres sentir el poder en tus manos y ejecutar esto localmente, solo tienes que seguir estos pasos mágicos: 📝👣

### ⚡ Paso 1: Poner los datos a punto (Limpieza) 🧽🛁
Abre tu terminal favorita 💻 y ejecuta el script de limpieza para crear la base de datos y poblarla de información fidedigna:
```bash
python limpieza_datos.py
```
*Si todo va bien, el terminal te gritará de alegría diciéndote cuántos registros insertó. (¡OJO, esto es importantísimo!)* 🚨✅

### ⚡ Paso 2: Encender los motores de visualización 🚀🔥
Una vez tengas tu archivo `meteorologia.db` brillante y listo, ¡arranca Streamlit! 🎈
```bash
streamlit run graficas.py
```

### ⚡ Paso 3: ¡Disfrutar del espectáculo! 🍿🤓
Tu navegador web 🌐 se abrirá automáticamente (o entra a `http://localhost:8501`) y podrás contemplar un deleite para los ojos. 👀✨

---

## 🔥 Funcionalidades Estrella (Features) ⭐🎖️

¿Qué verás cuando entres a la app? 🎁

- 🌡️ **Métricas Directas al Grano:** Podrás ver en números enormes la **Temperatura Máxima**, la **Mínima** y la **Media** del día. ¡Mátame de amor por estos KPIs! 💘📌
- 📉 **Gráfico Combinado (El Jefe Final):** Te mostramos un gráfico de barras 📊 (`steelblue`) y una línea espectacular 📉 con marcadores (`red`). Puedes pasar el ratón `hovermode='x unified'` para ver qué temperatura hacía a una hora concreta. 🕰️😎
- 📑 **Tabla Expansible Súper Elegante:** ¿Eres más de leer números puros? ¡No hay problema! Tenemos un `st.expander` mágico que se despliega 🦅 revelándote el Dataframe completito para que no pierdas ningún detalle. 🕵️‍♂️🔍

---

## 🤗 ¡Despedida y Agradecimientos! 🎉🎊🥳

¡Y esto es todo, amigas y amigos! 🙌 Este proyecto demuestra que transformar simples ficheros de texto plano en dashboards interactivos y bonitos está a un par de scripts de distancia. 📝💻✨

No olvides darle amor a este código 💖, hidratarse bien en los días en que `tamax` suba demasiado 🥤🥵 y, sobre todo... 

**¡Feliz Programación / Happy Coding!** 👩‍💻👨‍💻🚀🌟❤️‍🔥
=======
Comando para ejecutar gráficas:

```bash
streamlit run grafica.py
```
>>>>>>> 5170b7a6de6e07359999b09e85d7647325111eb2
