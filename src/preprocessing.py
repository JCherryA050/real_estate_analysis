import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
'''
    Functions used for preprocessing data for model integration.
'''
def log_scaled(data=None,features=None):
    '''
        Log transforms and scales continuous variables.
    '''
    data_preprocessed = data[features]
    for col in features:
        log_label = 'log_'+col

        log_var = np.log(data_preprocessed[col])
        log_var_normal = (log_var - np.mean(log_var))/np.std(log_var)

        data_preprocessed[log_label] = log_var_normal
        data_preprocessed.drop(col,axis=1,inplace=True)
    return data_preprocessed

def ohe_categoricals(data=None,features=None):
    '''
    Implements OHE operator on categorical variables.
    '''
    data_preprocessed = data[features]
    for col in features:
        data_preprocessed[col] = data_preprocessed[col].astype('str')
        var_train = data_preprocessed[[col]]

        # (2) Instantiate a OneHotEncoder with categories="auto",
        # sparse=False, and handle_unknown="ignore"
        ohe = OneHotEncoder(categories='auto',sparse=False,drop='first')
        # (3) Fit the encoder on fireplace_qu_train
        ohe.fit(var_train)
        var_encoded_train = ohe.transform(var_train)
        # Visually inspect fireplace_qu_encoded_train
        var_encoded_train = pd.DataFrame(
        # Pass in NumPy array
        var_encoded_train,
        # Set the column names to the categories found by OHE
        columns=col+'_'+ohe.categories_[0][:len(data_preprocessed[col].value_counts())-1],
        # Set the index to match X_train's index
        index=data_preprocessed.index
        )
        data_preprocessed = pd.concat([data_preprocessed, var_encoded_train], axis=1)
        data_preprocessed.drop(col,axis=1,inplace=True)
    return data_preprocessed