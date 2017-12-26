import pandas as pd
import numpy as np
from sklearn import model_selection, linear_model, svm
import httplib2

def get_data_saham(saham_label):
    #using period daily, indonesia stock exchange, and 1 year data
    resp, content = httplib2.Http().request("http://localhost:3000/saham/" + saham_label)
    df = pd.read_json(content)
    df.rename(columns={0:"Close"}, inplace=True)
    #return
    return df

def preprocessing(df):
    idx = len(df['Close']) - 1

    df['Close'] = df['Close'].astype(np.float64)

    for i in range(idx, 0, -1):
        selisih = df['Close'][i] - df['Close'][i-1]
        if selisih != 0:
           df['Close'][i] = selisih*100/df['Close'][i-1]
        else:
           df['Close'][i] = 0
    
    return df

def include_shift(stockdf, days = 8):
    #buat harga close beberapa hari menjadi fitur
    for i in range(1,days+1):
        length_forecast=i
        stockdf["shifted_close_" + str(i)]=stockdf["Close"].shift(-1*length_forecast)
        stockdf.fillna(value=stockdf["Close"][len(stockdf)-1],inplace=True)
    drop_row = days-1
    stockdf = stockdf[:-drop_row]
    return stockdf

def predict_tomorrow_price(saham_label, days = 8):
    maindf = get_data_saham(saham_label)
    maindf = include_shift(maindf, days)
    # maindf = include_shift(preprocessing(maindf), days)
    regressor = linear_model.Ridge(alpha=1.0)
    
    x_df = maindf.drop('shifted_close_' + str(days),1)
    y_df = maindf['shifted_close_' + str(days)]

    x = np.array(x_df)
    y = np.array(y_df)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.1)
    regressor.fit(x_train, y_train)
    
    #prepare test case for result
    x_result = []
    for i in range(1, days+1):
        column = 'shifted_close_' + str(i)
        x_result.append(maindf[column][len(maindf[column]) - 1])
    
    return regressor.predict(np.array(x_result).reshape(1, -1))


    
def predict_tomorrow_price_preprocessed(saham_label, days = 8):
    maindf = get_data_saham(saham_label)
    resultdf = maindf.copy()
    maindf = preprocessing(maindf)
    maindf = include_shift(maindf, days)

    regressor = svm.SVR()

    x_df = maindf.drop('shifted_close_' + str(days), 1)
    y_df = maindf['shifted_close_' + str(days)]
    
    x = np.array(x_df)
    y = np.array(y_df)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.1)
    regressor.fit(x_train, y_train)

    hasil = regressor.score(x_test, y_test)

    #prepare data for prediction
    x_result = []
    for i in range(1, days+1):
        column = 'shifted_close_' + str(i)
        x_result.append(maindf[column][len(maindf[column])-1])

    result = np.array(resultdf)
    return regressor.predict(np.array(x_result).reshape(1, -1))*result[len(result)-1]+result[len(result)-1]


