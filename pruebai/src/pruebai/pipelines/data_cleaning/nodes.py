import pandas as pd
import numpy as np

def clean_asistencia(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Manejo de nulos basico - forward fill u otro (aplica a series de tiempo o lógicas de negocio)
    # Por el caso base, podemos rellenar con la moda
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            mode_vals = df[col].mode()
            if len(mode_vals) > 0:
                df[col] = df[col].fillna(mode_vals[0])
            
    # Estandarizar alguna columna string si existe
    if 'estado_asistencia' in df.columns:
        df['estado_asistencia'] = df['estado_asistencia'].astype(str).str.lower().str.strip()
        
    return df

def clean_calificaciones(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    
    # Si hay columna 'nota', extraemos valor numérico
    if 'nota' in df.columns:
        df['nota'] = df['nota'].astype(str).str.extract(r'(\d+(?:\.\d+)?)', expand=False).astype(float)
        df['nota'] = df['nota'].fillna(df['nota'].median())
    
    for col in df.columns:
        if df[col].isnull().sum() > 0 and col != 'nota':
            mode_vals = df[col].mode()
            if len(mode_vals) > 0:
                df[col] = df[col].fillna(mode_vals[0])
            
    # Tratamiento de outliers usando IQR
    if 'nota' in df.columns:
        Q1 = df['nota'].quantile(0.25)
        Q3 = df['nota'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Cap outliers
        df.loc[df['nota'] < lower_bound, 'nota'] = lower_bound
        df.loc[df['nota'] > upper_bound, 'nota'] = upper_bound
        
    return df

def clean_estudiantes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    
    # Manejo de valores mixtos o inconsistentes, por ejemplo mayusculas en carreras o facultades
    if 'carrera' in df.columns:
        df['carrera'] = df['carrera'].astype(str).str.upper().str.strip()
        
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            # Imputar strings con modo, numeros con media
            if df[col].dtype == 'object':
                mode_vals = df[col].mode()
                if len(mode_vals) > 0:
                    df[col] = df[col].fillna(mode_vals[0])
            else:
                df[col] = df[col].fillna(df[col].median())
                
    return df

def clean_inscripciones(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    
    # Estandarizar posibles fechas si existen
    for col in df.columns:
        if 'fecha' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                mode_vals = df[col].mode()
                if len(mode_vals) > 0:
                    df[col] = df[col].fillna(mode_vals[0])
            else:
                df[col] = df[col].fillna(df[col].median())
                
    return df
