# --------------------------------------------------------------
# Define library for handling the preprocessing of data.
#
# Currently, only log transforms, scaling and one hot encoding are implemented.
#
# --------------------------------------------------------------

# Standard Library imports.
import warnings

# Numpy imports
import numpy as np

# Pandas Imports
import pandas as pd

# skylearn preprocessing imports
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer, MissingIndicator

def log_scaled(data=None,features=None):
    '''Log transforms and scales continuous variables.

    This function handles Log transforms of selected continuous features, 
    standardizes the Log transformed data and generates new column names
    for the transformed features.

    Parameters
    ----------
    data: pd.DataFrame
        Pandas DataFrame containing the data to be processed.
    features: list_type
        List containing Pandas DataFrame columns associated with the 
        features to be processed.
    '''
    # Suppress the slice warnings associated with copying DataFrame
    warnings.filterwarnings('ignore')

    # Copy the DataFrame parameter with only the selected features
    data_preprocessed = data[features]

    # Loop through the list of features 
    for col in features:
        # Create new column name for processed feature
        log_label = 'log_'+col

        # Take the log of the feature
        log_var = np.log(data_preprocessed[col])

        # Standardize the distribution of the feature
        log_var_normal = (log_var - np.mean(log_var))/np.std(log_var)

        # Set new column in the copied DataFrame and drop the old feature
        data_preprocessed[log_label] = log_var_normal
        data_preprocessed.drop(col,axis=1,inplace=True)


    return data_preprocessed

def ohe_categoricals(data=None,features=None):
    '''OneHot Encoding of categorical variables.

    This function handles OneHotEncoding of selected categorical features.

    Parameters
    ----------
    data: pd.DataFrame
        Pandas DataFrame containing the data to be processed.
    features: list_type
        List containing Pandas DataFrame columns associated with the 
        features to be processed.
    '''
    # Suppress the slice warnings associated with copying DataFrame
    warnings.filterwarnings('ignore')

    # Copy the DataFrame parameter with only the selected features
    data_preprocessed = data[features]

    # Loop through the list of features 
    for col in features:

        # Convert the feature categories into string_type (this is for
        # categories that are of int64 or float type)
        data_preprocessed[col] = data_preprocessed[col].astype('str')

        # Create a variable var_trian
        # extracted from data parameter
        # (double brackets due to shape expected by OHE)
        var_train = data_preprocessed[[col]]

        # Instantiate a OneHotEncoder with categories="auto",
        # sparse=False, and drop="first"
        ohe = OneHotEncoder(categories='auto',sparse=False,drop='first')

        # Fit the encoder on var_train
        ohe.fit(var_train)
        var_encoded_train = ohe.transform(var_train)

        # Convert the encoded variable to Pandas DataFrame
        var_encoded_train = pd.DataFrame(
        # Pass in NumPy array
        var_encoded_train,
        # Set the column names to the categories found by OHE
        columns=col+'_'+ohe.categories_[0][:len(data_preprocessed[col].value_counts())-1],
        # Set the index to match X_train's index
        index=data_preprocessed.index
        )

        # Set new column in the copied DataFrame and drop the old feature
        data_preprocessed = pd.concat([data_preprocessed, var_encoded_train], axis=1)
        data_preprocessed.drop(col,axis=1,inplace=True)
        
    return data_preprocessed