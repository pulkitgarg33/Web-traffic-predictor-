# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:00:53 2018

@author: pulki
"""
import numpy as np 
import pandas as pd

dataset = pd.read_csv('train_2.csv').fillna(0)
page = dataset['Page']
dataset = dataset.drop( 'Page' , axis =1)

dataset = dataset.transpose()
dataset['date']  = dataset.index

pd.to_datetime( dataset['date'] ,format='%Y-%m-%d', errors='ignore')


import datetime
start = datetime.datetime.strptime("2017-09-13", "%Y-%m-%d")
end = datetime.datetime.strptime("2017-11-14", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
date_gen = np.array(date_generated)
i = 0
for x in date_gen:
    date_gen[i] = str(x).split(' ')[0]
    i = i+1

key_gen_1 = pd.read_csv('key_2.csv')


pd.to_datetime( date_gen ,format='%Y-%m-%d', errors='ignore')

from statsmodels.tsa.arima_model import ARIMA
id = []
predictions = []
exp = str()
for i in range (0 , 145064):
    train = []
    train = [ x for x in dataset.iloc[: , i].values]
    for t in range(len(date_gen)):
        model = ARIMA(train, order=(5,1,0))
        model_fit = model.fit(disp=0 , trend = 'c', solver = 'lbfgs')
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        history.append(yhat)
        exp = str(page[i]) + '_' + str(date_gen[t])
        id.append(key_gen_1[key_gen_1['Page'] == exp]['Id'].values)
    print ('page '+str(i+1) + 'trained')
        
id = np.array(id)
predictions = np.array(predictions)

prediction_results = pd.DataFrame( id , columns = ['id'])
predictions = predictions.astype(int)
prediction_results['Visits'] = predictions


    