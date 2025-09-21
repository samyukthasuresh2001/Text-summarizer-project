from textsummarizer.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
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