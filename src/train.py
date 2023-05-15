import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from xgboost import XGBRegressor
import pickle

df = pd.read_csv(r'C:\Users\yeray\notebooks\repo-dsftf23\Rampup\proyecto ML\src2\data\processed\BGG_cleaned.csv')

X=df.drop('Rating Average',axis=1)
y=df['Rating Average']
X.dropna(inplace=True)
y=y.drop(y.drop(X.index).index)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42)

xgb_reg = XGBRegressor()
param_grid = {
    'learning_rate': [0.1, 0.05, 0.01],
    'max_depth': [3, 4, 5],
    'n_estimators': [50, 100, 200]
}

grid_search_xgb = GridSearchCV(estimator=xgb_reg, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search_xgb.fit(X_train, y_train)

xgb_reg = XGBRegressor(**grid_search_xgb.best_params_)

xgb_reg.fit(X_train, y_train)

with open('new_model.pkl', 'wb') as archivo:
    pickle.dump(xgb_reg, archivo)



