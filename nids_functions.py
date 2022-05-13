############################################################################################
####################### i m p o r t i n g      l i b r a r i e s  ##########################
############################################################################################

from scipy import sparse
import pandas as pd
import numpy as np
import pickle as pk
from sklearn.metrics import roc_auc_score, f1_score


############################################################################################
####################### L o a d i n g    p i c k l e    f i l e s ##########################
############################################################################################

with open('scaler.pkl', 'rb') as f:
    scaler = pk.load(f)
with open('def_xgb_model.pkl', 'rb') as f:
    estimator = pk.load(f)
with open('feature_eng.pkl', 'rb') as f:
    eng_features_list = pk.load(f)
with open('unique_categories.pkl', 'rb') as f:
    cat_list = pk.load(f)

############################################################################################
##################### p r e p r o c e s s i n g    f u n c t i o n #########################
############################################################################################

def categorical_to_numerical(df):
    '''
    this function will return numerical value of categories in categorical features
    
    df: pandas dataframe which contains, proto, state and service as features
    '''
    ## uniques list for categories in proto features
    unique_proto = np.array(cat_list[0])
    ### uniques list for categories in service feature
    unique_service = np.array(cat_list[1])
    ### uniques list for categories in state feature
    unique_state = np.array(cat_list[2])
    
    def to_lower(x):
        return str(x.lower())
    def numerical_proto(x):
        '''this function will return index of a category present in the list'''
        return np.where(unique_proto == x)[0]
    def numerical_state(x):
        '''this function will return index of a category present in the list'''
        return np.where(unique_state == x)[0]
    def numerical_service(x):
        '''this function will return index of a category present in the list'''
        return np.where(unique_service == x)[0]
    
    ### converting categories into lower case
    df['proto'] = df['proto'].apply(to_lower)
    df['state'] = df['state'].apply(to_lower)
    df['service'] = df['service'].apply(to_lower)
    ### converting categorical features and with the index of their respective category in unique list
    df['proto'] = df['proto'].apply(numerical_proto)
    df['state'] = df['state'].apply(numerical_state)
    df['service'] = df['service'].apply(numerical_service)

    return df



############################################################################################
######################## F e a t u r e   e n g i n e e r i n g #############################
############################################################################################

def feature_engineering(df):
    '''
    this function will return the dataframe after performing some feature engineering on given dataframe
    
    df: pandas dataframe
    '''
    for feat in eng_features_list:
        ## adding an extra features by adding two features
        df[feat[0]+feat[1]] = np.array(df[feat[0]]) + np.array(df[feat[1]])
    return df


############################################################################################
############################# s c a l e r     f u n c t i o n ##############################
############################################################################################

def scale_features(df):
    '''
    this function will return the scaled array
    
    df: pandas dataframe
    '''
    scaled_data = scaler.transform(df.drop(['proto', 'state', 'service'], axis=1))
    return scaled_data

############################################################################################
##################### t o       s p a r s e        f u n c t i o n #########################
############################################################################################

def to_sparse(df, scaled_data):
    '''
    this function will return the sparse matrix of scaled data and the categorical features after stacking
    
    df: pandas dataframe
    scaled_data: array after transformation using scaler
    '''
    data = sparse.csr_matrix(np.array(np.hstack((np.array(df[['proto', 'state', 'service']]), scaled_data)), dtype=np.float32))
    return data
   

############################################################################################
##################  C a l c u l a t e   m e t r i c   s c o r e   ##########################
############################################################################################


def calculate_metric_score(y_true, y_pred):
    '''this function will return auc and f1 score'''
    ### calculat auc
    auc = roc_auc_score(y_true, y_pred)
    ### calculate f1-score
    f1score = f1_score(y_true, y_pred)
    return auc, f1score


############################################################################################
######################### p r e d i c t i o n    f u n c t i o n ###########################
############################################################################################

def predict(preprocessed_data):
    '''
    this function will return the predicted class label of input array of 1*d shape
    
    preprocessed_data: preprocessed data will be input in this features after preprocessing and feature engineering as done on train data
    '''
    output = estimator.predict(preprocessed_data)
    return output


############################################################################################
#######################                    E N D                  ##########################
############################################################################################

