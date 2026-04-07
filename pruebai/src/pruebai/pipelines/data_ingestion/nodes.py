import pandas as pd

def initialize_data(*datasets: pd.DataFrame) -> str:
    """Genera un diagnostico inicial de los datos ingresados."""
    report_lines = ["--- DATA INGESTION REPORT ---"]
    for i, df in enumerate(datasets):
        report_lines.append(f"\nDataset {i + 1}")
        report_lines.append(f"Shape: {df.shape}")
        report_lines.append(f"Duplicated rows: {df.duplicated().sum()}")
        nulls = df.isnull().sum()
        report_lines.append(f"Nulls:\n{nulls[nulls > 0].to_string() if nulls.sum() > 0 else '0'}")
    
    return "\n".join(report_lines)
