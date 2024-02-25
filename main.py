from mlproject import logger
from mlproject.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipelines.stage_03_data_transformation import DataTransformationPipeline
from mlproject.pipelines.stage_04_model_trainer import ModelTrainingPipeline
from mlproject.pipelines.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=================X")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=================X")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n===============X")
except Exception as e:
    logger.exception(e)

STAGE_NAME="Model Training Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:
    logger.exception(e)


STAGE_NAME="Model Evaluation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:
    logger.exception(e)
