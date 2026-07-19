from step_1_preprocess import clean_data
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
df = clean_data(r'../dataset/insurance.csv')
X=df.drop('charges',axis=1)
y=df['charges']
scaling= MinMaxScaler()
X_scaled=scaling.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)
#i train the four model already ik the best model is the random forest
RF=RandomForestRegressor()
RF.fit(X_train,y_train)
y_pred_rf=RF.predict(X_test)
print("MAE: ",mean_absolute_error(y_test,y_pred_rf))
print("MSE: ",mean_squared_error(y_test,y_pred_rf))
print("R2: ",r2_score(y_test,y_pred_rf))
with open('../model/Random_forest_i.pkl', 'wb') as file:
    pickle.dump(RF, file)
with open('../model/scaler_i.pkl', 'wb') as file:
    pickle.dump(scaling, file)
print('Done')