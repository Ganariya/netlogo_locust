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

csv_datas_birds = []

for i in range(T):
    data_birds = pd.read_csv(f"birds/result{i + 1}.csv")
    csv_datas_birds.append(data_birds)

# -----------------------------------
# locusts figure

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
x = []
left_y = []
left_err = []

right_y = []
right_err = []

for i in range(0, 3000 + 1, per):

    if i == 3000:
        i -= 1
    x.append(i)

    # left
    sum_v = 0
    for j in range(T):
        sum_v += csv_datas_birds[j].loc[i]['left-grass']
    avg_v = sum_v / T

    sd_v = 0
    for j in range(T):
        sd_v += (csv_datas_birds[j].loc[i]['left-grass'] - avg_v) ** 2
    sd_v /= T
    sd_v = math.sqrt(sd_v)
    sd_v /= math.sqrt(T)

    left_err.append(sd_v)
    left_y.append(avg_v)

    # right
    sum_v = 0
    for j in range(T):
        sum_v += csv_datas_birds[j].loc[i]['right-grass']
    avg_v = sum_v / T
    sd_v = 0
    for j in range(T):
        sd_v += (csv_datas_birds[j].loc[i]['right-grass'] - avg_v) ** 2
    sd_v /= T
    sd_v = math.sqrt(sd_v)
    sd_v /= math.sqrt(T)

    right_err.append(sd_v)
    right_y.append(avg_v)

ax.set_xlabel("ticks")
ax.set_ylabel("num of grass")
ax.errorbar(x, left_y, left_err, label="left grass", marker='o', capthick=1, capsize=3, lw=1)
ax.errorbar(x, right_y, right_err, label="right grass", marker='o', capthick=1, capsize=3, lw=1)
ax.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=12)

plt.show()
figure.savefig('images/compare_with_bird_grass.png')
