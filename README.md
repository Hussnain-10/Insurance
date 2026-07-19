# Insurance charges Prediction
Predicting the insurance charges using the machine algorithum 
## Project Overview
The project is the analyze the insurance feature and build a model that can predict the charges of a insurance
## Dataset Features
The dataset contain the following features:
- age
- sex
- bmi
- children
- smoker
- region
 Target Variable :
- charges
## Data Preprocessing
The following preprocessing steps were performed:
- Loaded the dataset
- checked missing values
- Encode the datasets 
- see the data correlation 
- prepared data for machine learning models
## Machine learning Models
The following regression models were trained and compared
1. Linear Regression 
2. K-Nearest Neighbors Regreesor
3. Decision Tree Regressor 
4. Random Forest Regressor
## Model Evaluation 
Model are evaluated using:
- R2 score 
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
Example Comparison :
| Model               | R2    | MAE      | MSE          |
|----------------------|-------|----------|--------------|
| Linear Regression    | 0.745 | 4312.49  | 36776416.91  |
| KNeighborsRegressor  | 0.632 | 4470.15  | 53029344.31  |
| Decision Tree        | 0.695 | 3446.48  | 43898083.41  |
| Random Forest        | 0.824 | 2913.04  | 25312027.07  |

## Best Model 
Random Forest Regressor was selected as the final model because it provide the best performance on the datasets

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/Hussnain-10/Insurance.git
   cd Insurance
   ```

2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model
   ```bash
   cd scripts
   python step_2_train.py
   ```

4. Run a prediction on a new customer
   ```bash
   python step_3_predict.py
   ```