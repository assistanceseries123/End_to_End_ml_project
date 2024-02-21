from mlproject.constants import *
from mlproject.utils.common import read_yaml,create_directories
from src.mlproject.entity.config_entity import DataIngestionConfig
from mlproject.entity.config_entity import DataValidationConfig
from mlproject.entity.config_entity import DataTransformationConfig
class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params= read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])
    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_files=config.local_data_files,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config


    
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation_config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config= self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config= DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config