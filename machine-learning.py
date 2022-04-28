# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:36:28 2022

@author: invitado
"""

import pandas as pd
import numpy as np

url = 'titanic.csv'
data = pd.read_csv(url)

#Tratamiento de la data

data.Sex.replace(['female', 'male'], [0, 1], inplace = True)
data['Embarked'].replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)
data.Age.replace(np.nan, 30)
