# importing libraries
from numpy.lib.function_base import median
import pandas as pd
import numpy as np
# from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
# import mlflow.sklearn

# Get url from Dvc
import dvc.api
path = 'data/AdSmartABdata.csv'
repo = 'G:/10_academy/Week_2/solutions/Ad_campaign_performance'
version = 'v1'

data_url = dvc.api.get_url(
    path= path,
    repo=repo,
    rev= version
)
mlflow.set_experiment('demo')



if __name__=="__main__":
    # warnings.filterwarnings('ignore')
    np.random.seed(40)

    #read the data
    data=pd.read_csv(data_url,sep=",")

    #log data params
    mlflow.log_param('data_url',data_url)
    mlflow.log_param('data_version',version)
    mlflow.log_param('input_rows',data.shape[0])
    mlflow.log_param('input_cols',data.shape[1])

    print(data.head(1))
    
