# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:59:03 2020

@author: abishek.kandiyil
"""

import pandas as pd
from datetime import datetime

alert_name='abc'
feedback='Useful'
date=str(datetime.now())

df=pd.DataFrame()
df['Alert']=''
df['Date']=''
df['Feedback']=''

df['Alert']=alert_name
df['Date']=date
df['Feedback']=feedback

ls={'Alert':[alert_name],'Feedback':[feedback],'Date':[date]}

df=pd.DataFrame.from_dict(ls)


df.to_csv('D:\\Employers\\feedback.csv',index=False)
