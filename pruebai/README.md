# Guía de Implementación Kedro - Caso 5: Educación Universitaria

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

Este repositorio contiene la solución completa para el **Caso 5: Educación Universitaria**. Utilizando el framework de **Kedro**, hemos construido una serie de _pipelines_ (flujos de datos) modulares encargados de ingerir, limpiar, transformar matemáticamente y validar datos provenientes de cuatro fuentes: *Estudiantes, Asistencias, Calificaciones e Inscripciones*.

Este documento `README.md` funciona como una guía paso a paso para que cualquier usuario o docente pueda implementar, reproducir y evaluar este proyecto en su propio equipo sin inconvenientes.

---

## 1. Requisitos y Preparación del Entorno

Es muy recomendable ejecutar este proyecto dentro de un entorno virtual aislado para evitar conflictos con las librerías globales de tu computadora. Debes contar con **Python 3.9 o superior**.

### Crear y Activar el Entorno Virtual
Primero, abre tu terminal (PowerShell recomendado en Windows) en la carpeta raíz del proyecto (`pruebai/`) y ejecuta:

```bash
# Crear el entorno virtual
python -m venv entorno-prueba

# Activar el entorno virtual
.\entorno-prueba\Scripts\activate
```

### Instalación de Dependencias
Con el entorno activado, instala todas las librerías necesarias. Hemos configurado el archivo de requerimientos para que incluya dependencias clave como `scikit-learn` y el plugin de pandas para el catálogo de Kedro:

```bash
pip install -r requirements.txt
```

---

## 2. Ejecución del Proyecto: Consideración Crítica para Windows

Los datos originales contienen caracteres especiales y tildes en español. Para asegurar que Pandas y Kedro lean y guarden estos archivos correctamente sin arrojar errores de codificación (como el temido `UnicodeDecodeError`), configuramos el catálogo para leer en formato `latin1` y guardar el resultado final en formato estándar `utf-8`.

**🔴 IMPORTANTE:** Si usas Windows, el sistema operativo por defecto intentará usar su propia codificación (`cp1252`) ignorando nuestras reglas y provocando una caída durante el guardado de los datos limpios. Para prevenir esto, **antes de ejecutar Kedro**, debes configurar temporalmente la codificación de tu terminal al estándar internacional.

En **PowerShell** (Recomendado), ejecuta este comando una vez:
```powershell
$env:PYTHONUTF8=1
```
*(Si usas la consola CMD tradicional, utiliza en su lugar: `set PYTHONUTF8=1`)*

---

## 3. Ejecutar los Pipelines de Datos

Con las dependencias instaladas y la variable `PYTHONUTF8` configurada, estás listo para correr el flujo completo. Este comando ejecutará secuencialmente la Ingesta, Limpieza, Transformación y Validación de los datos:

```bash
kedro run
```

### Resultados de la Ejecución
Al finalizar exitosamente, verás un mensaje indicando `Exit code 0`. Podrás comprobar los resultados revisando las siguientes carpetas dentro de `/data`:
* **`02_intermediate/`**: Contiene las cuatro tablas originales, ahora completamente limpias, sin valores nulos ni ruido en las notas.
* **`03_primary/`**: Contiene nuestro gran entregable: `dataset_integrado.csv`. Un dataset robusto de formato Machine Learning, unificado a partir de las bases previas, con variables escaladas (StandardScaler) numéricamente.
* **`08_reporting/`**: Contiene reportes de texto (`.txt`) generados automáticamente resumiendo diagnósticos de duplicados, datos faltantes y validación de columnas.

---

## 4. Exploración Visual (Notebook EDA)

Si además de correr el código en la terminal deseas visualizar de manera gráfica los problemas que tenían los datos originales y cómo cada función del pipeline los fue resolviendo, hemos dejado preparado un cuaderno interactivo provisto de gráficos (utilizando Matplotlib y Seaborn).

Levanta el entorno de cuadernos ejecutando:

```bash
kedro jupyter lab
```

Una vez en el navegador, abre el archivo `notebooks/01_eda_exploratorio.ipynb` y ejecuta sus celdas paso a paso para recorrer interactivamente todo nuestro Análisis Exploratorio de Datos (EDA).
