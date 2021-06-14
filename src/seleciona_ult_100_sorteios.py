import pandas as pd

lotofacil = pd.read_csv(r'C:\lotoFacilLast100\dados\LOTOFACIL.csv', sep=';')
lotofacil_100 = lotofacil.head(100)
lotofacil_100.to_csv(r'C:\lotoFacilLast100\dados\100_ultimos_jogos.csv', sep=';', index = False)

