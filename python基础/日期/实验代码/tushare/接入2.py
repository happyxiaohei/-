"""
接入2 - 

Date: 2022/12/18

"""
import pandas as pd
import tushare as ts
ts.set_token('8d731504ede2a4d0a7924989c1cd6ab986ddea49d22cd3bc7b8ff31a')
pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20221218')

print(df)