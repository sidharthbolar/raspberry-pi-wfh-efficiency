from itertools import groupby

import pandas as pd
from constants import SRC_PATH_OUTPUT_RB,curr_date_str,derived_col_names,col_names

class ResultProcessor:
    default_file_name='result.csv'

    def __init__(self, date, input=SRC_PATH_OUTPUT_RB, file_name=default_file_name):
        self.date = date
        self.input=input
        self.df=pd.read_csv(self.input+file_name,header=None,names=col_names,
                         parse_dates=[0])

    def result_processor_total_detections(self, file_name=default_file_name):
        df=self.df.copy()
        df[derived_col_names[0]] = df['ts'].dt.date.astype(str)
        df.drop(columns=[col_names[0]], inplace=True)
        final_output=df[(df.ts_dateformat == curr_date_str)] \
            .groupby([derived_col_names[0]]) \
            .sum(col_names[1]) \
            .rename(columns={col_names[1]: derived_col_names[1]}) \
            .reset_index() \
            .loc[:, derived_col_names[1]][0]
        return(final_output)

    def result_processor_consecutive_detections(self):
        df = self.df.copy()
        df[derived_col_names[0]] = df['ts'].dt.date.astype(str)
        df=df[(df[derived_col_names[0]] == curr_date_str)]
        return(max([sum(1 for i in g)
                    for k, g in groupby(df[col_names[1]].tolist())
                    if k ==1]))