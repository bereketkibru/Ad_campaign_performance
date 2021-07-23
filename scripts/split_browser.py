import pandas as pd
import numpy as np
from urllib.parse import urlparse
import mlflow
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
     #read the data
    data=pd.read_csv(data_url,sep=",")

    data = data.query("not (yes == 0 & no == 0)")
    datab = data.drop('browser', axis=1)
    print(datab.head(2))
    # saving file
    datab.to_csv('data/AdSmartABdata.csv',index=False)