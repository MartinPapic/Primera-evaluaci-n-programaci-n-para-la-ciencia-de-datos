import pandas as pd

def validate_data(df_integrado: pd.DataFrame) -> str:
    report_lines = ["--- DATA VALIDATION REPORT ---"]
    report_lines.append(f"Shape of integrated dataset: {df_integrado.shape}")
    
    # Validar que no hay nulos (o documentar si quedaron)
    nulls = df_integrado.isnull().sum()
    total_nulls = nulls.sum()
    report_lines.append(f"Total null values in integrated dataset: {total_nulls}")
    
    if total_nulls > 0:
        report_lines.append(f"Columns with nulls:\n{nulls[nulls > 0].to_string()}")
        
    # Verificar codificacion y escalado
    dtypes_counts = df_integrado.dtypes.value_counts()
    report_lines.append(f"\nData Types summary:\n{dtypes_counts.to_string()}")
    
    if 'indice_rendimiento' in df_integrado.columns:
        report_lines.append(f"\nIndice de rendimiento derivation succeeded. Mean: {df_integrado['indice_rendimiento'].mean():.2f}")
        
    return "\n".join(report_lines)
