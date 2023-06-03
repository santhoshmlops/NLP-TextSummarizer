from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_ingestion import DataIngestion
from textsummarizer.components.data_validation import DataValiadtion
from textsummarizer.components.data_transformation import DataTransformation
from textsummarizer.components.model_trainer import ModelTrainer
from textsummarizer.components.model_evaluation import ModelEvaluation



from textsummarizer.logger import logger


class DataTrainingPipeline:
    def __init__(self):
        pass

    def dataingestiontrainingpipeline(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


    def datavalidationtrainingpipeline(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()


    def datatransformationtrainingpipeline(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()

    def modeltrainertrainingpipeline(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

    def modelevlauationtrainingpipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()