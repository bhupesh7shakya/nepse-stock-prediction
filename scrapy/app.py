import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st




st.title=('Nepse Trend Prediction')

# user_input=st.text_input('Enter The Stock Picker','NABIL')
selected_option = st.selectbox("Select an option", ["NABIL", "NTC", "HDL","UNL","GBIME"])



df =pd.read_excel(f'price_history/{selected_option}.xlsx')
df=df.dropna()
if selected_option is not "GBIME":
  closing_price=df.close.str.replace(',', '').astype(float)
else:
  closing_price=df.close
  
st.write(df.head())
# date=df.dates
# df.head()
data_training = pd.DataFrame(closing_price[0:int(len(df)*0.70)])
data_testing = pd.DataFrame(closing_price[int(len(df)*0.70):int(len(df))])

st.subheader('Data from 2012') 
st.write(df.describe())

st.subheader('Closing Price vs Time chart')

fig=plt.figure(figsize=(12,6))

plt.plot(closing_price)
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA')


ma100=closing_price.rolling(100).mean()

fig=plt.figure(figsize=(12,6))
plt.plot(closing_price,'b')
# read about moving average
plt.plot(ma100,'r')
plt.plot(closing_price)
st.pyplot(fig)


st.subheader('Closing Price vs Time chart with 100MA & 200MA')

ma100=closing_price.rolling(100).mean()
ma200=closing_price.rolling(200).mean()

fig=plt.figure(figsize=(12,6))
plt.plot(closing_price,'b')
# read about moving average
plt.plot(ma100,'g')
plt.plot(ma200,'r')
plt.plot(closing_price)
st.pyplot(fig)

st.subheader('Orignal vs Prediction')

# scaling dta
from sklearn.preprocessing import MinMaxScaler

scaler= MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)

x_train=[]
y_train=[]

for i in range(100, data_training_array.shape[0]):
    x_train.append(data_training_array[i-100:i])
    y_train.append(data_training_array[i,0])

x_train, y_train =np.array(x_train) ,np.array(y_train)

model = load_model(F'./{selected_option}.h5')

past_100_days=data_training.tail(100)
past_100_days_forcasting=data_testing.tail(100)

final_df=past_100_days._append(data_testing,ignore_index=True)
final_df_forcasting=past_100_days._append(data_testing,ignore_index=True)

final_df.head()
final_df_forcasting.head()

input_data=scaler.fit_transform(final_df)
input_data_forcasting=scaler.fit_transform(final_df_forcasting)

x_test =[]
y_test=[]
x_test_forcasting =[]
y_test_forcasting=[]

for i in range(100,input_data.shape[0]):
  x_test.append(input_data[i-100:i])
  y_test.append(input_data[i,0])

for i in range(100,input_data_forcasting.shape[0]):
  x_test_forcasting.append(input_data_forcasting[i-100:i])
  y_test_forcasting.append(input_data_forcasting[i,0])

x_test,y_test =np.array(x_test),np.array(y_test )
print(x_test.shape)
print(y_test.shape)

x_test_forcasting,y_test_forcasting =np.array(x_test_forcasting),np.array(y_test_forcasting )




y_predicted = model.predict(x_test)
y_predicted_forcasting = model.predict(x_test_forcasting)


# scale_factor = 1/0.02099517
scale_factor=1
y_predicted= y_predicted * scale_factor
y_test=y_test*scale_factor


fig =plt.figure(figsize=(12,6))
plt.plot(y_test,'b',label='Orignal Price')
plt.plot(y_predicted[:len(y_predicted)],'r',label='predicted')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig)
# y_predicted = scaler.inverse_transform(y_predicted)


st.subheader('Future Prediction')

fig = plt.figure(figsize=(12, 6))

# Reverse scaling for y_train
y_train_orig = scaler.inverse_transform(y_train.reshape(-1, 1))
y_test_orig = scaler.inverse_transform(y_test.reshape(-1, 1))

# Find out how many values you can append from y_test_orig to y_train_orig
values_to_append = min(100 - len(y_train_orig), len(y_test_orig))

# Slice the y_test_orig array to get the values you want to append
values_to_append_from_y_test = y_test_orig[:values_to_append]

# Append the selected values from y_test_orig to y_train_orig
y_train_orig = np.concatenate((y_train_orig, values_to_append_from_y_test), axis=0)



# Reverse scaling for y_predicted
y_predicted_orig = scaler.inverse_transform(y_predicted.reshape(-1, 1))

# Plotting the training data
plt.plot(range(len(y_train_orig)), y_train_orig, 'g', label='Training Data')

midpoint = len(y_predicted_orig) // 2


test_predicted_data=y_predicted_orig[:midpoint]
test_forcasted_data=y_predicted_orig[midpoint:]

# Plotting the predicted data
plt.plot(range(len(y_train_orig), len(y_train_orig) + len(y_test_orig)), y_test_orig, 'b', label='Test and actual Data')
plt.plot(range(len(y_train_orig), len(y_train_orig) + len(test_predicted_data)), test_predicted_data, 'r', label='Predicted')

# plotting forcasting
# plt.plot(range(len(y_train_orig)+len(y_train_orig), len(y_train_orig) + len(test_forcasted_data)), y_predicted_orig, 'y', label='Forcasting')
plt.plot(range(len(y_train_orig)+ len(y_test_orig[midpoint:]), len(y_train_orig[midpoint:]) + len(y_test_orig) + len(test_forcasted_data)), test_forcasted_data, 'y', label='Forecasting')


st.subheader(test_forcasted_data[len(test_forcasted_data)-1])

plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig)
st.subheader('News')
st.subheader("Not foud")


