import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터  로드 및 병합

train=pd.read_csv('./data/train_2016_v2.csv')
train.head()

prop = pd.read_csv('./data/properties_2016.csv')
prop.head()

print(train.shape, prop.shape)

dataset = pd.merge(train,prop,on="parcelid",how="left")
dataset.head()

# 병합된 데이터는 계속되는 작업에서 불필요한 데이터로드를 피하기위해 'dataset.csv'로 저장하여 사용합니다.

dataset.to_csv('./data/dataset.csv',index = False)