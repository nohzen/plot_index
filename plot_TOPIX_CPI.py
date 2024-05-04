import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

CPI_file_name = "datas/CPI_year.xlsx" # 消費者物価指数
TOPIX_file_name = "datas/topix_year.csv" # TOPIX


df_CPI = pd.read_excel(CPI_file_name, header=9, index_col=1)
df_CPI = df_CPI.iloc[0:54, 13] # 1970年-2023年, 年平均
year_list = df_CPI.index.to_numpy(dtype=int)
CPI_list = df_CPI.to_numpy()
# df_CPI.plot()
plt.plot(year_list, CPI_list, label="物価 (CPI)")

df_TOPIX = pd.read_csv(TOPIX_file_name, header=0, index_col=0)
df_TOPIX = df_TOPIX.iloc[0:54, 3] # 1970年-2023年, 終値
df_TOPIX = df_TOPIX / df_TOPIX[-4] *100 # 2000年で規格化
TOPIX_list = df_TOPIX.to_numpy()
# df_TOPIX.plot()
plt.plot(year_list, TOPIX_list, label="株価 (TOPIX * const.)")

ratio_list = TOPIX_list / CPI_list * 100
plt.plot(year_list, ratio_list, label="株価/物価")


plt.grid()
plt.xlabel("year")
plt.ylabel("index")
plt.title("年ごとの指数の変動")
plt.legend()
plt.tight_layout()
plt.savefig("images/TOPIX_CPI.png")
plt.show()

