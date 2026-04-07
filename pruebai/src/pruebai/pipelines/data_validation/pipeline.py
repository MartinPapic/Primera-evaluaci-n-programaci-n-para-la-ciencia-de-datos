from kedro.pipeline import Pipeline, node, pipeline
from .nodes import validate_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=validate_data,
                inputs="dataset_integrado",
                outputs="validation_report",
                name="validate_data_node",
            )
        ]
    )
