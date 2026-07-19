import pandas as pd
def clean_data(path):
    df=pd.read_csv(path)
    df=pd.get_dummies(df,columns=['region'],dtype=int,drop_first=True )
    df['sex']=df['sex'].map({'female':0,'male':1})
    df['smoker']=df['smoker'].map({'yes':0,'no':1})
    return df