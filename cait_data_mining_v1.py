# name: compare sectorial data with gas-specific data
# function : 
# date: 2021/07/09
# writer : yejin kwon

# https://www.epa.gov/ghgemissions/overview-greenhouse-gases -> ref

#-----

# 모듈 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams

#-----


df_sector= pd.read_csv('df_sector.csv')
df_gas= pd.read_csv('df_gas.csv')
df_merge = pd.merge(df_sector, df_gas, on=["Country","Year"], how="outer")
df_merge.to_csv('df_merge.csv',index=False,encoding='cp949')
print(df_merge)


#----

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(1,1,1)
ax.plot(df_merge['Total excluding LUCF'],df_merge['ghg'], color='b', linewidth=1, label='sectorial-gas_specific')
ax.legend(loc='upper left', fontsize=6)
#ax.set_ylabel('sectorial emission(Mt CO2eq)',size=8)       check here !!
#ax.set_xlabel('gas-specific emission(Mt CO2eq)',size=8)
ax.set_xlabel('Sectorial GHG emission [Mt CO2eq]',size=8)
ax.set_ylabel('Gas-specific GHG emission [Mt CO2eq]',size=8)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.rcParams['axes.unicode_minus']=False
plt.subplots_adjust(left=0.05, bottom=0.13, right=0.95, top=0.88, wspace=0.05, hspace=0.05)
plt.title('Compare sectorial data with gas-specific data', size=12, pad=10)
plt.show()