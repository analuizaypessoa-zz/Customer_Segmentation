
import pandas as pd
import numpy as np

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

## load data and build the plots
#EXAMPLE PLOT
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
df2 = pd.read_csv("../Outputs/modelv1.csv")


def table_Cat(col1,col2):
    NM = df[[col1,col2]]
    table = pd.pivot_table(NM, index = [col1],
                          columns = [col2], aggfunc = len, fill_value = 0)
    table_sort = table.sort_values([0,1], ascending = False)
    return table_sort

cols = ['GENDER', 'AGE', 'EMPLOYMENT', 'INCOME', 'FREQUENCY_VISIT',
       'HOW_DO_YOU_ENJOY_STARBUCKS', 'TIME_PER_VISIT',
       'DISTANCE_TO_NEAREST_STORE', 'MEMBER', 'SPEND_PER_VISIT', 'QUALITY_EV',
       'PRICE_EV', 'PROMOTIONS_EV', 'AMBIANCE_EV', 'WIFI_EV', 'SERVICE_EV',
       'BUSINESS_OR_FRIENDS', 'POTENTIAL_CLIENT', 'FG_cake', 'FG_coffee',
       'FG_colddrinks', 'FG_jawschip', 'FG_juices', 'FG_never', 'FG_pastries',
       'FG_sandwiches', 'FG_DIGITAL_MEDIA', 'FG_STARBUCKS_WEBSITE', 'FG_EMAIL',
       'FG_FRIENDS', 'FG_FISIC']

def df_col_table_Cat(df, cols):
    df_list = []
    a = df[cols]
    for col in a.columns:
        out = table_Cat(col,'Labels')
        out.reset_index(inplace = True)
        df_list.append(out)
    return df_list


df_l = df_col_table_Cat(df2, cols)
print(df_l[0])