import pandas as pd
import itertools
import numpy as np
from random import randrange, uniform
df_tds_possib = pd.read_csv(r'C:\lotoFacilLast100\dados\todas_possibilidades_bolas_mais_sorteadas.csv', sep=';')

df_40_possibilidades_aleatorias = df_tds_possib.sample(40)
df_40_possibilidades_aleatorias.to_csv(r'C:\lotoFacilLast100\dados\40_possibilidades_sorteadas.csv', sep=';', index = False)