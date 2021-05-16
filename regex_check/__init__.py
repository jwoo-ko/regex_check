import pandas as pd
import numpy as np
import os
import re


class Checklist:
    def __init__(self, checklist_path):
        self.checklist_df = pd.read_csv(os.path.join(checklist_path, 'checklist.txt'), sep='\t', encoding='utf-8', na_filter='')
        self.checklist_df['regex_yn'] = 0
        self.checklist_df['cond_yn'] = 0
        self.regex_dict = {}
        for key in self.checklist_df['regex']:
            if key not in self.regex_dict.keys():
                self.regex_dict[key] = 0

        for key in self.checklist_df['cond']:
            if key not in self.regex_dict.keys():
                self.regex_dict[key] = 0

    def reset(self):
        self.checklist_df['regex_yn'] = 0
        self.checklist_df['cond_yn'] = 0
        self.regex_dict = {key: 0 for key in self.regex_dict.keys()}

    def check(self, search_line):
        for key, value in self.regex_dict.items():
            regex_check = re.compile(key)
            if regex_check.search(search_line):
                self.regex_dict[key] = 1

    def update(self):
        self.checklist_df['regex_yn'] = self.checklist_df.apply(lambda x: self.regex_dict[x['regex']], axis=1)
        self.checklist_df['cond_yn'] = self.checklist_df.apply(
            lambda x: self.regex_dict[x['cond']] if x['cond'] is not np.nan else 1,
            axis=1
        )

    def error_log(self):
        result = '----RESULT----\n'
        for index, row in self.checklist_df.iterrows():
            if row['check'] == 'delete' and row['regex_yn'] == 1 and row['cond_yn'] == 1:
                result += \
                    'No.{}, ({}) "{}" if exists ({}): Failed.\n'.\
                    format(row['no'], row['check'], row['regex'], row['cond'])

        for index, row in self.checklist_df.iterrows():
            if row['check'] == 'insert' and row['regex_yn'] == 0 and row['cond_yn'] == 1:
                result += \
                    'No.{}, ({}) "{}" if exists ({}): Failed.\n'.\
                    format(row['no'], row['check'], row['regex'], row['cond'])

        result += '----------------\n\n'

        return result
