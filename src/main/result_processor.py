import pandas as pd
from constants import SRC_PATH_OUTPUT_RB

class ResultProcessor:
    default_file_name='result.csv'

    def __init__(self,input=SRC_PATH_OUTPUT_RB):
        self.input=input

    def result_processor(self, file_name=default_file_name):
        results_df=pd.read_csv(self.input+file_name,header=None)

        return(len(results_df))