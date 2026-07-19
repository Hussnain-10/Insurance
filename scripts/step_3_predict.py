import pickle
with open('../model/Random_forest_i.pkl', 'rb') as file:
    model = pickle.load(file)
with open('../model/scaler_i.pkl', 'rb') as file:
    scaler = pickle.load(file)

customer=[[
    	19,                             # age
        0,                              # sex (female:0)(male:1)
        27.900,                         # bmi
        0,                              #children
        0,                              #smoker(yes:0)(no:1)
        0,                              #region_northwest
        0,                              #region_southeast
        1                               #region_southwest
     
]]
customer_scaled=scaler.transform(customer)
prediction=model.predict(customer)
print(prediction)