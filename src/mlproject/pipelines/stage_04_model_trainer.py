from mlproject.config.configuration import ConfigurationManager
from mlproject import logger
from mlproject.components.model_trainer import ModelTrainer

STAGE_NAME="Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n===============X")
    except Exception as e:
        logger.exception(e)