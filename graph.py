# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np
import datetime as dt

# おまじない あとで調べる
plt.style.use('ggplot') 
#font = {'family' : 'meiryo'}
#matplotlib.rc('font', **font)

# csv読み込み。indexとして使う列を指定。header=0はデフォルトなので指定していない
df = pd.read_csv('Weight Data.csv',header=None, skiprows=2,index_col=0,names=['datetime', 'weight'])
df.index = pd.to_datetime(df.index)

# 可視化
plt.plot(df.index, df['weight'])

# 表示設定
plt.xticks(rotation=70)
plt.ylim([65,75])
plt.legend() # 凡例を表示
plt.title("Weight")
plt.xlabel("Datetime")
plt.ylabel("Weight(kg)")
plt.show()
#plt.savefig("weight.png")
