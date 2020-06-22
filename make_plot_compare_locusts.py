import math

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
sns.set_style('whitegrid')
sns.set_palette('Set1')
plt.rcParams['figure.dpi'] = 250

T = 10
L = 3000
per = 100

csv_datas_locusts = []
csv_datas_birds = []
for i in range(T):
    data_locusts = pd.read_csv(f"locusts/result{i + 1}.csv")
    data_birds = pd.read_csv(f"birds/result{i + 1}.csv")
    csv_datas_locusts.append(data_locusts)
    csv_datas_birds.append(data_birds)

# -----------------------------------
# locusts figure

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
x = []
locusts_y = []
locusts_err = []

birds_y = []
birds_err = []

for i in range(0, 3000 + 1, per):

    if i == 3000:
        i -= 1
    x.append(i)

    # locusts
    sum_v = 0
    for j in range(T):
        sum_v += csv_datas_locusts[j].loc[i]['locusts']
    avg_v = sum_v / T

    sd_v = 0
    for j in range(T):
        sd_v += (csv_datas_locusts[j].loc[i]['locusts'] - avg_v) ** 2
    sd_v /= T
    sd_v = math.sqrt(sd_v)
    sd_v /= math.sqrt(T)

    locusts_err.append(sd_v)
    locusts_y.append(avg_v)

    # birds
    sum_v = 0
    for j in range(T):
        sum_v += csv_datas_birds[j].loc[i]['locusts']
    avg_v = sum_v / T
    sd_v = 0
    for j in range(T):
        sd_v += (csv_datas_birds[j].loc[i]['locusts'] - avg_v) ** 2
    sd_v /= T
    sd_v = math.sqrt(sd_v)
    sd_v /= math.sqrt(T)

    birds_err.append(sd_v)
    birds_y.append(avg_v)

ax.set_xlabel("ticks")
ax.set_ylabel("num of locusts")
ax.errorbar(x, locusts_y, locusts_err, label="without birds", marker='o', capthick=1, capsize=3, lw=1)
ax.errorbar(x, birds_y, birds_err, label="with birds", marker='o', capthick=1, capsize=3, lw=1)
ax.legend()

figure.savefig('images/compare_locusts.png')
