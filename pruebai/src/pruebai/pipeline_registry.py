"""Project pipelines."""
from __future__ import annotations

from kedro.pipeline import Pipeline
from pruebai.pipelines import data_ingestion, data_cleaning, data_transformation, data_validation

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    ingestion_pipe = data_ingestion.create_pipeline()
    cleaning_pipe = data_cleaning.create_pipeline()
    transformation_pipe = data_transformation.create_pipeline()
    validation_pipe = data_validation.create_pipeline()
    
    pipelines = {
        "data_ingestion": ingestion_pipe,
        "data_cleaning": cleaning_pipe,
        "data_transformation": transformation_pipe,
        "data_validation": validation_pipe,
        "__default__": ingestion_pipe + cleaning_pipe + transformation_pipe + validation_pipe
    }
    return pipelines
