from textsummarizer.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.step2_data_validation import DataValidationTrainingPipeline
from textsummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")   


except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")   


except Exception as e:
    logger.exception(e)
    raise e