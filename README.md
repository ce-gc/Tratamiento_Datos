# Sistema de Gestión de Temperaturas de A Coruña

Este proyecto es un sistema para la obtención, almacenamiento y visualización de datos meteorológicos de la ciudad de A Coruña, utilizando la API oficial de la AEMET.

## Componentes del Proyecto

1. **aemet.py**: Script para descargar los datos de temperaturas máximas diarias del último mes desde la API de AEMET y almacenarlos en una base de datos local SQLite (`aemet_coruña.db`).
2. **graficas.py**: Aplicación con Streamlit para visualizar la evolución de la temperatura máxima diaria.

## Instalación de Dependencias

Para la gestión de dependencias y ejecución del proyecto, se utiliza `uv`, un gestor rápido de proyectos y paquetes en Python.

Crea un entorno virtual e instala las dependencias necesarias:

```bash
uv venv
uv pip install requests python-dotenv streamlit pandas plotly
```

(En Windows, puedes activar el entorno virtual creado usando `.venv\Scripts\activate`).

## Configuración y Ejecución

1. Solicita una API KEY en AEMET OpenData.
2. Crea un archivo `.env` en la raíz del proyecto y añade tu clíve de la siguiente manera:
   ```
   API_KEY=tu_token_aqui
   ```
3. Obtén los datos de la AEMET y guárdalos en la base de datos:
   ```bash
   uv run aemet.py
   ```
4. Lanza el dashboard interactivo para ver las gráficas:
   ```bash
   uv run streamlit run graficas.py
   ```
