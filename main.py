import matplotlib
import matplotlib.pyplot as plt 

import pandas as pd
import numpy as np 

df = pd.read_csv("datos.csv")

type_count = df['Type1'].value_counts(ascending=True)

type2_count = df['Type2'].value_counts(ascending=True)

legendary_count = df['Legendary'].value_counts()

colors = ["blue", "orange"]

height = df["Height"].mean()

weight = df["Weight"].mean()

figure, axes = plt.subplots(2,2)
figure.suptitle("pokemon mas raro", fontsize=16)

axes[0, 0].barh(type_count.index, type_count.values )

axes[0, 0].set_title('Pokemon tipo 1 distribucion')

axes[0,1].barh(type2_count.index, type2_count.values,)

axes[0, 1].set_title('Pokemon tipo 2 distribucion')


axes[1, 0].scatter(df["Height"], df["Weight"], 
                     color='black',  
                     alpha=0.5,
                     s= 3)

axes[1, 0].set_title("Relación entre peso y altura")
axes[1, 0].set_xlabel("Altura (m)")
axes[1, 0].set_ylabel("Peso (kg)")

plt.tight_layout()


axes[1, 1].pie(legendary_count.values,
                
                  autopct='%1.1f%%',
                  colors = colors,
                  labels = ["", "Legendary"],
                  explode = [0, 0.2],
                  shadow = True,)

axes[1, 1].set_title("Legendario vs No Legendario",
                      fontsize=14)

plt.tight_layout()

plt.show()