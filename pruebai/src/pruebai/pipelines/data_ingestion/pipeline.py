from kedro.pipeline import Pipeline, node, pipeline
from .nodes import initialize_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=initialize_data,
                inputs=[
                    "asistencia_raw",
                    "calificaciones_raw",
                    "estudiantes_raw",
                    "inscripciones_raw"
                ],
                outputs="ingestion_report",
                name="diagnostico_inicial_node",
            )
        ]
    )
