from kedro.pipeline import Pipeline, node, pipeline
from .nodes import transform_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=transform_data,
                inputs=["asistencia_inter", "calificaciones_inter", "estudiantes_inter", "inscripciones_inter"],
                outputs="dataset_integrado",
                name="transform_data_node",
            )
        ]
    )
