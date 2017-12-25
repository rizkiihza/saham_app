import httplib2
import pandas as pd
import saham
import numpy as np
import random

saham_label = input("masukan simbol saham: ")
data_df = saham.get_data_saham(saham_label)
print(data_df["Close"][-30:].to_string(index=False))
hasil = saham.predict_tomorrow_price(saham_label, 100)
print(hasil)