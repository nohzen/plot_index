import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import japanize_matplotlib

fig, ax = plt.subplots()

kawase_file_name = "datas/USDJPY.csv" # kawase
TOPIX_file_name = "datas/topix_manth.csv" # TOPIX


df_TOPIX = pd.read_csv(TOPIX_file_name, header=0, index_col=0)
df_TOPIX = df_TOPIX.iloc[:, 3] # 2016/02 - 2024/05, 終値
df_TOPIX = df_TOPIX / df_TOPIX[0] *100 # 2016/02で規格化
year_list = pd.to_datetime(df_TOPIX.index)
TOPIX_list = df_TOPIX.to_numpy()
ax.plot(year_list, TOPIX_list, label="株価 (TOPIX * const.)")


df_kawase = pd.read_csv(kawase_file_name, header=0, index_col=0)
df_kawase = df_kawase.iloc[:, 3] # 2016/02 - 2024/05, 終値
kawase_list = df_kawase.to_numpy()
ax.plot(year_list, kawase_list, label="ドル/円")


ratio_list = TOPIX_list / kawase_list * 100
ax.plot(year_list, ratio_list, label="ドル建てTOPIX (TOPIX*円/ドル)")


fig.autofmt_xdate()
plt.xticks(rotation=60)
locator = mdates.AutoDateLocator(minticks=5, maxticks=20)
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%Y/%m")
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid()
plt.xlabel("year/month")
plt.ylabel("ドル/円 or Index")
plt.title("月ごとの指数の変動")
plt.legend()
plt.tight_layout()
plt.savefig("images/TOPIX_kawase.png")
plt.show()


