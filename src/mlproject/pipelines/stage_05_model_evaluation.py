from mlproject import logger
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject.config.configuration import ConfigurationManager

STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n===============X")
    except Exception as e:
        logger.exception(e)