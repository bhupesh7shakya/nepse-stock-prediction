# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import load_model

# # Load the saved model
# model = load_model('E:/scraper/nabil.h5')

# # Assuming you have the test data in the variable 'x_test'
# df= pd.read_excel('./price_history/NABIL.xlsx')
# df=df.dropna()
# closing_price=df.close.str.replace(',', '').astype(float)

# date=df.date
# data_training=pd.DataFrame(closing_price[0:int(len(df)*0.70)])
# data_testing=pd.DataFrame(closing_price[int(len(df)*0.70):int(len(df))])



# # scaling dta
# from sklearn.preprocessing import MinMaxScaler

# scaler= MinMaxScaler(feature_range=(0,1))
# past_100_days=data_training.tail(100)
# final_df=past_100_days._append(data_testing,ignore_index=True)
# input_data=scaler.fit_transform(final_df)



# x_test =[]
# y_test=[]

# for i in range(100,input_data.shape[0],3):
#   x_test.append(input_data[i-100:i])
#   y_test.append(input_data[i,0])

# x_test,y_test =np.array(x_test),np.array(y_test )

# y_predicted = model.predict(x_test)

# y_predicted = scaler.inverse_transform(y_predicted)


# print(y_predicted.shape[0])

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
# from matplotlib import 
# Load the saved model
model = load_model('E:/scraper/nabil.h5')

# Assuming you have the test data in the variable 'x_test'
df = pd.read_excel('./price_history/NABIL.xlsx')
df = df.dropna()
closing_price = df.close.str.replace(',', '').astype(float)

date = df.date
data_training = pd.DataFrame(closing_price[0:int(len(df)*0.70)])
data_testing = pd.DataFrame(closing_price[int(len(df)*0.70):int(len(df))])

# Scaling data
scaler = MinMaxScaler(feature_range=(0,1))
past_100_days = data_training.tail(100)
final_df = past_100_days._append(data_testing, ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0], 3):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i:i+3, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

y_predicted = model.predict(x_test)
y_predicted = scaler.inverse_transform(y_predicted)

num_predictions = y_predicted.shape[0]

print("Number of predictions:", num_predictions)
print(y_predicted)
