import pandas as pd
import os

train_data = 'data/train.csv'
test_data = 'data/test.csv'
valid_data = 'data/test.csv'

file = "multiclass_dataset.csv"

def save_load_df(file:str):
    if os.path.exists(file):
        df = pd.read_csv(file, index_col= 0)
    else:
        df = pd.concat(map(pd.read_csv, [train_data, test_data, valid_data]), axis= 0, ignore_index=True)
        df.to_csv(file, columns= ['id', 'text', 'label', 'sentiment'])
        df = pd.read_csv(file, index_col= 0)

    return df