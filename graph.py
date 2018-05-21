import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

plt.style.use('ggplot') 

dfw = pd.read_csv('Weight Data.csv',header=None, skiprows=2,index_col=0,names=['datetime', 'weight'])
dfw.index = pd.to_datetime(dfw.index)

plt.plot(dfw.index, dfw['weight'])
plt.xticks(rotation=70)
plt.ylim([65,75])
plt.title("Weight")
plt.xlabel("Datetime")
plt.ylabel("Weight(kg)")
plt.savefig("weight.png")

dfw = pd.read_csv('Body Fat Percentage Data.csv',header=None, skiprows=2,index_col=0,names=['datetime', 'fat'])
dfw.index = pd.to_datetime(dfw.index)

plt.plot(dfw.index, dfw['fat'])
plt.ylim([0.1,0.3])
plt.title("Body Fat")
plt.ylabel("Body Fat")
plt.savefig("fat.png")

