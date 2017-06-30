import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('./data/dataset.csv')
dataset.head()


# 데이터 프레임과 변수이름 넣으면 describe와 distplot 보여줌 
def value(df, value_name):
    print(df[[value_name]].describe())
    sns.distplot(df[value_name], kde=True, bins=1000)
    plt.show()
    
# qqplot 출력     
def qq(df, value_name):
    sp.stats.probplot(df[value_name], plot=plt)
    plt.title(value_name + " qqplot")
    plt.show()


# transaction_date / month별로 막대그래프 
from datetime import datetime
def transaciton_month(df):
    month = [datetime.strptime(x, '%Y-%m-%d').month for x in df["transactiondate"]]
    month = pd.Series(month)
    month_cnt = month.value_counts()
    sns.barplot(month_cnt.index, month_cnt.values, alpha=0.7)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Number of transactions", fontsize=12)
    plt.show()


# missing pct 그래프 출력 및 마지막 row에 missing pct 추가해서 리턴 
def missing(df):
    missing_pct = df.isnull().sum() / df.isnull().count()
    df.loc["missing_pct"] = missing_pct.round(3)
    plt.figure(figsize=(12,18))
    missing_pct = missing_pct.sort_values(ascending=False)
    sns.barplot(y=missing_pct.index, x=missing_pct.values, 
            alpha=1., color="r")
    plt.xlabel("Missing_pct", fontsize=12)
    plt.title("Number of missing values in each column", fontsize=15)
    return df

  
# missing_pct가 30% 미만인 변수만 살려본다 
def missing30(df):
    df2 = df.loc[:, df.loc["missing_pct"] < 0.3]
    print(df2.shape)
    return df2

  
# filling missing values 
# 연속형 변수는 평균으로 대체 
def toMean(df):
    missing_feature1 = ["calculatedbathnbr", "calculatedfinishedsquarefeet", "finishedsquarefeet12",
                  "fullbathcnt", "lotsizesquarefeet", "structuretaxvaluedollarcnt", "taxvaluedollarcnt",
                   "landtaxvaluedollarcnt", "taxamount"]
    for x in missing_feature1:
        df[x].fillna(df[x].mean(), inplace=True)
    return df

  
# filling missing values 
# 카테고리 변수는 최빈값으로 
def toMode(df):
    missing_feature2 = ["regionidcity", "censustractandblock", "regionidzip", "propertycountylandusecode"]
    for x in missing_feature2:
        df[x].fillna(df.mode()[0], inplace=True)
    return df

#df_train2.isnull().sum()


# yearbuilt 삭제 
# 남은 데이터에서 결측값이 있는 row는 날려보자 
def delete_missing(df):
    df2 = df.dropna()
    print(df2.shape)
    return df2


# 회귀 분석을 위해 id 칼럼 삭제 
#df_train3 = df_train3.drop("missing_pct")
#df_train3 = df_train3.drop("parcelid", axis=1)
#df_train3.tail(10)


# 대부분 float로 되어 있지만 실제로는 카테고리 데이터가 많이 존재한다. 타입을 변환시켜줘야함 
#df_dtype = df.dtypes.reset_index()
#df_dtype.columns = ["name", "type"]
#df_dtype


# 일단 리스트에 numeric과 category 변수를 각각 넣어둠 
# target = logerror
numeric = ["bathroomcnt", "bedroomcnt", "calculatedbathnbr", "calculatedfinishedsquarefeet",
          "finishedsquarefeet12", "fullbathcnt", "latitude", "longitude",
          "lotsizesquarefeet", "roomcnt", , "yearbuilt", "structuretaxvaluedollarcnt",
          "taxvaluedollarcnt", "landtaxvaluedollarcnt","taxamount"]
category = ["transactiondate", "fips", "propertycountylandusecode", 
           "propertylandusetypeid", "rawcensustractandblock",
           "regionidcity", "regionidcounty", "regionidzip",
           "assessmentyear", "censustractandblock"]


# 카테고리 변수로 만들기 위해 str로 타입 변환
def toCat(df):
    for x in category:
        df[x] = df[x].astype(str)
    return df
    
#df_dtype = df_train3.dtypes.reset_index()
#df_dtype.columns = ["name", "type"]
#df_dtype
