import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = ((df['weight']/((df['height']/100)**2)) > 25).astype(int)

# 3
df.replace(
    {"cholesterol": {1: 0, 2: 1, 3: 1}, "gluc": {1: 0, 2: 1, 3: 1}},
    inplace=True
)

# 4
def draw_cat_plot():
    # Convertendo o DataFrame para o formato longo
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Criando o gráfico
    fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')

    # Ajustando o rótulo do eixo y
    for ax in fig.axes.flat:
        ax.set_ylabel('total')

    # Salvando o gráfico
    fig.savefig('catplot.png')
    return fig.fig


# 10
def draw_heat_map():
    # 11
    q1 = (df['ap_lo'] <= df['ap_hi'])
    q2 = (df['height'] >= df['height'].quantile(0.025))
    q3 = (df['height'] <= df['height'].quantile(0.975))
    q4 = (df['weight'] >= df['weight'].quantile(0.025))
    q5 = (df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df.loc[(q1 & q2 & q3 & q4 & q5)]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=0.5)

    # 15



    # 16
    plt.savefig('heatmap.png')
    return plt.gcf()
