pip install yfinance 
symbols = ["GOLD","CL=F","USDCAD=X"]
import yfinance as yf 
import pandas as pd 
import numpy as np 
df = pd.DataFrame()
for i in symbols:
    data = yf.download(symbols,start='2021-01-01',end='2023-01-01')
    data = data.fillna('null')
print(data)