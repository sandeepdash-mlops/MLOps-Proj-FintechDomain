import sys
from src.entity.config_entity import FintechPredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging
from pandas import DataFrame


class FintechData:
    def __init__(self,
                Gender,
                Age,
                KYC_Verified,
                Region_Code,
                Previously_Onboarded,
                Avg_Txn_Amt,
                Payment_Channel,
                Vintage,
                Account_Tenure_lt_1_Year,
                Account_Tenure_gt_2_Years,
                Chargeback_History_Yes
                ):
        """
        Fintech Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.Gender = Gender
            self.Age = Age
            self.KYC_Verified = KYC_Verified
            self.Region_Code = Region_Code
            self.Previously_Onboarded = Previously_Onboarded
            self.Avg_Txn_Amt = Avg_Txn_Amt
            self.Payment_Channel = Payment_Channel
            self.Vintage = Vintage
            self.Account_Tenure_lt_1_Year = Account_Tenure_lt_1_Year
            self.Account_Tenure_gt_2_Years = Account_Tenure_gt_2_Years
            self.Chargeback_History_Yes = Chargeback_History_Yes

        except Exception as e:
            raise MyException(e, sys) from e

    def get_fintech_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            fintech_input_dict = self.get_fintech_data_as_dict()
            return DataFrame(fintech_input_dict)
        
        except Exception as e:
            raise MyException(e, sys) from e


    def get_fintech_data_as_dict(self):
        """
        This function returns a dictionary from FintechData class input
        """
        logging.info("Entered get_payment_data_as_dict method as FintechData class")

        try:
            input_data = {
                "Gender": [self.Gender],
                "Age": [self.Age],
                "KYC_Verified": [self.KYC_Verified],
                "Region_Code": [self.Region_Code],
                "Previously_Onboarded": [self.Previously_Onboarded],
                "Avg_Txn_Amt": [self.Avg_Txn_Amt],
                "Payment_Channel": [self.Payment_Channel],
                "Vintage": [self.Vintage],
                "Account_Tenure_lt_1_Year": [self.Account_Tenure_lt_1_Year],
                "Account_Tenure_gt_2_Years": [self.Account_Tenure_gt_2_Years],
                "Chargeback_History_Yes": [self.Chargeback_History_Yes]
            }

            logging.info("Created fintech data dict")
            logging.info("Exited get_fintech_data_as_dict method as FintecheData class")
            return input_data

        except Exception as e:
            raise MyException(e, sys) from e

class FintechDataClassifier:
    def __init__(self,prediction_pipeline_config: FintechPredictorConfig = FintechPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of FintechDataClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of FintechDataClassifier class")
            model = Proj1Estimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise MyException(e, sys)