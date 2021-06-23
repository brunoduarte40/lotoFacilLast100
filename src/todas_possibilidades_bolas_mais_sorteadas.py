import pandas as pd
import itertools

df = pd.read_csv(r'C:\lotoFacilLast100\dados\bolas_mais_sorteadas.csv', sep=';')

df_tds_possib = pd.DataFrame([e for e in itertools.product(df.B1,df.B2,df.B3,df.B4,df.B5,
                                                           df.B6,df.B7,df.B8,df.B9,df.B10,
                                                           df.B11,df.B12,df.B13,df.B14,df.B15)],
                             columns=df.columns)
df_tds_possib.to_csv(r'C:\lotoFacilLast100\dados\todas_possibilidades_bolas_mais_sorteadas.csv', sep=';', index = False)