"""
接入 -

Date: 2022/12/11

"""
import pandas as pd
import tushare as ts
ts.set_token('8d731504ede2a4d0a7924989c1cd6ab986ddea49d22cd3bc7b8ff31a')
pro = ts.pro_api()

# 查询公司基本信息
df = pro.stock_company(
    exchange='SZSE',
    fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')

df = pro.query('daily', ts_code='000003.SZ', start_date='20180701', end_date='20221208')
# 查询当前所有正常上市交易的股票列表
data = pro.stock_basic(
    exchange='',
    list_status='L',
    fields='ts_code,symbol,name,area,industry,list_date')

# Save the data to an Excel file
df.to_excel('000002.xlsx', index=False)

