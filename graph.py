import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

plt.style.use('ggplot') 

df = pd.read_csv('Weight Data.csv',header=None, skiprows=2,index_col=0,names=['datetime', 'weight'])
df.index = pd.to_datetime(df.index)

plt.plot(df.index, df['weight'])
plt.xticks(rotation=70)
plt.ylim([65,75])
plt.title("Weight")
plt.xlabel("Datetime")
plt.ylabel("Weight(kg)")
plt.savefig("weight.png")
