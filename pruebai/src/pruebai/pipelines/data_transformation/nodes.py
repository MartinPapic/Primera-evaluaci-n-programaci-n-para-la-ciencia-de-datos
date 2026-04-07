import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def transform_data(asistencia: pd.DataFrame, calificaciones: pd.DataFrame, estudiantes: pd.DataFrame, inscripciones: pd.DataFrame) -> pd.DataFrame:
    # 1. Agrupar calificaciones por id_inscripcion
    if 'id_inscripcion' in calificaciones.columns and 'nota' in calificaciones.columns:
        calificaciones_agg = calificaciones.groupby('id_inscripcion', as_index=False)['nota'].mean()
    else:
        calificaciones_agg = calificaciones

    # 2. Unir inscripciones con calificaciones
    if 'id_inscripcion' in inscripciones.columns and 'id_inscripcion' in calificaciones_agg.columns:
        insc_cal = pd.merge(inscripciones, calificaciones_agg, on='id_inscripcion', how='left')
    else:
        insc_cal = inscripciones

    # 3. Pivot table para la rubrica: convertir notas de asignaturas en columnas por estudiante
    if 'id_estudiante' in insc_cal.columns and 'nombre_asignatura' in insc_cal.columns and 'nota' in insc_cal.columns:
        pivot_notas = insc_cal.pivot_table(
            index='id_estudiante', 
            columns='nombre_asignatura', 
            values='nota', 
            aggfunc='mean'
        ).fillna(0).reset_index()
    else:
        pivot_notas = pd.DataFrame()

    # 4. Join final con Estudiantes
    merged = estudiantes
    if 'id_estudiante' in pivot_notas.columns:
        merged = pd.merge(merged, pivot_notas, on='id_estudiante', how='left')

    # Feature Engineering Avanzado: Indice de rendimiento (Promedio general)
    if 'id_estudiante' in insc_cal.columns and 'nota' in insc_cal.columns:
        promedio = insc_cal.groupby('id_estudiante', as_index=False)['nota'].mean().rename(columns={'nota': 'indice_rendimiento'})
        merged = pd.merge(merged, promedio, on='id_estudiante', how='left')

    # 5. Múltiples imputaciones y Rellenar nulos
    for col in merged.columns:
        if merged[col].dtype == 'object':
            mode_vals = merged[col].mode()
            merged[col] = merged[col].fillna(mode_vals[0] if not mode_vals.empty else 'Desconocido')
        else:
            merged[col] = merged[col].fillna(0)

    # 6. Codificacion de categoricas
    le = LabelEncoder()
    cat_columns = merged.select_dtypes(include=['object']).columns
    for col in cat_columns:
        merged[f"{col}_encoded"] = le.fit_transform(merged[col].astype(str))
        
    # 7. Normalizacion
    scaler = StandardScaler()
    num_columns = merged.select_dtypes(include=['float64', 'int64']).columns
    num_columns = [col for col in num_columns if col != 'id_estudiante']
    if len(num_columns) > 0:
        merged[num_columns] = scaler.fit_transform(merged[num_columns])
        
    return merged
