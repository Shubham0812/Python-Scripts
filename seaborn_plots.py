import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

df = pd.read_csv('PokeTest.csv', index_col=0)

stats_df = df.drop(['Total','Stage','Legendary'],axis = 1)
# print(df)

# sns.lmplot(x='Attack', y='Defense', data=df,hue='Stage',fit_reg=False)

sns.set_style('darkgrid')
# sns.boxplot(data=stats_df)

melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat")

print(melted_df)
# sns.violinplot(x='Type 1',y = 'Defense',data= df,palette=pkmn_type_colors)

sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1',palette=pkmn_type_colors)

plt.legend(bbox_to_anchor=(1, 1), loc=3)


plt.legend()
plt.show()
