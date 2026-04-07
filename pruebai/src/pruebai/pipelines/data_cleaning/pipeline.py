from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_asistencia, clean_calificaciones, clean_estudiantes, clean_inscripciones

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_asistencia,
                inputs="asistencia_raw",
                outputs="asistencia_inter",
                name="clean_asistencia_node",
            ),
            node(
                func=clean_calificaciones,
                inputs="calificaciones_raw",
                outputs="calificaciones_inter",
                name="clean_calificaciones_node",
            ),
            node(
                func=clean_estudiantes,
                inputs="estudiantes_raw",
                outputs="estudiantes_inter",
                name="clean_estudiantes_node",
            ),
            node(
                func=clean_inscripciones,
                inputs="inscripciones_raw",
                outputs="inscripciones_inter",
                name="clean_inscripciones_node",
            ),
        ]
    )
