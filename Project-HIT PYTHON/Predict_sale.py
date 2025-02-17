import pandas as pd
import numpy as np
import sklearn


data = pd.read_csv(r'train.csv',index_col="Id")
data.head()
data.columns
features = {"LotArea","YearBuilt","1stFlsSF","2ndFlsSF","BedroomAbvGr","ToTRmsAbvGrd","TotRmsAbvGrd"}
x = data[features]
y = data["SalePrice"]
x.head()
y.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8,test_size = 0.2, random_state = 0)

from sklearn.tree import DecisionTreeRegressor
dt_model = DecisionTreeRegressor(random_state=1)
dt_model.fit(x_train, y_train)
y_preds =dt_model.predict(x_test)
y_preds
pd.DataFrame({'y' : y_test,'y_pred':y_preds}).head()

from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(random_state=1) # type: ignore
rf_model.fit(x_train, y_train)
y_preds_rf = rf_model.predict(x_test)
y_preds_rf[:5]
#predict with a new input
rf_model.predict([[]])