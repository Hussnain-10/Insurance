import pickle
with open('Random_forest_i.pkl','rb') as file:
    model=pickle.load(file)

customer=[[
    	18,                             # age
        1,                              # sex (female:0)(male:1)
        37.900,                         # bmi
        2,                              #children
        1,                              #smoker(yes:0)(no:1)
        0,                              #region_northwest
        0,                              #region_southeast
        1                               #region_southwest
     
]]
prediction=model.predict(customer)
print(prediction)