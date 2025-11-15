import pandas as pd
from data_preprocessing_project import *

data = pd.read_csv('nhldraft.csv')

remove_feature_substr(data, 'amateur_team', '()')
c, n, b=assess_data(data)
# check each of the numerical features
# for num in n:
#     assess_numeric_feature(data,num)

# If a numeric feature has outliers, use the following example to recode them or drop the rows
column_name = 'age'
data_no_nan = data[data[column_name].notna()].copy()

data_no_nan[column_name] = recode_numeric_outliers(data_no_nan, column_name)
data.loc[data[column_name].notna(), column_name] = data_no_nan[column_name]
assess_numeric_feature(data,column_name)