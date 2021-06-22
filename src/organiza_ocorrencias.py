import pandas as pd
dataFrame_baixado_B1 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB1.csv', sep=';')
dataFrame_baixado_B2 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB2.csv', sep=';')
dataFrame_baixado_B3 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB3.csv', sep=';')
dataFrame_baixado_B4 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB4.csv', sep=';')
dataFrame_baixado_B5 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB5.csv', sep=';')
dataFrame_baixado_B6 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB6.csv', sep=';')
dataFrame_baixado_B7 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB7.csv', sep=';')
dataFrame_baixado_B8 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB8.csv', sep=';')
dataFrame_baixado_B9 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB9.csv', sep=';')
dataFrame_baixado_B10 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB10.csv', sep=';')
dataFrame_baixado_B11 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB11.csv', sep=';')
dataFrame_baixado_B12 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB12.csv', sep=';')
dataFrame_baixado_B13 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB13.csv', sep=';')
dataFrame_baixado_B14 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB14.csv', sep=';')
dataFrame_baixado_B15 = pd.read_csv(r'C:\lotoFacilLast100\dados\OcorrenciaB15.csv', sep=';')
######################################################################################################################
B1_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B1.iloc[0:2,]
B2_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B2.iloc[0:2,]
B3_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B3.iloc[0:2,]
B4_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B4.iloc[0:2,]
B5_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B5.iloc[0:2,]
B6_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B6.iloc[0:2,]
B7_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B7.iloc[0:2,]
B8_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B8.iloc[0:2,]
B9_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B9.iloc[0:2,]
B10_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B10.iloc[0:2,]
B11_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B11.iloc[0:2,]
B12_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B12.iloc[0:2,]
B13_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B13.iloc[0:2,]
B14_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B14.iloc[0:2,]
B15_frame_primeira_e_segunda_bola_mais_sorteada = dataFrame_baixado_B15.iloc[0:2,]
######################################################################################################################
B1_primeira_e_segunda_bola_mais_sorteada = B1_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B2_primeira_e_segunda_bola_mais_sorteada = B2_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B3_primeira_e_segunda_bola_mais_sorteada = B3_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B4_primeira_e_segunda_bola_mais_sorteada = B4_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B5_primeira_e_segunda_bola_mais_sorteada = B5_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B6_primeira_e_segunda_bola_mais_sorteada = B6_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B7_primeira_e_segunda_bola_mais_sorteada = B7_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B8_primeira_e_segunda_bola_mais_sorteada = B8_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B9_primeira_e_segunda_bola_mais_sorteada = B9_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B10_primeira_e_segunda_bola_mais_sorteada = B10_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B11_primeira_e_segunda_bola_mais_sorteada = B11_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B12_primeira_e_segunda_bola_mais_sorteada = B12_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B13_primeira_e_segunda_bola_mais_sorteada = B13_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B14_primeira_e_segunda_bola_mais_sorteada = B14_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
B15_primeira_e_segunda_bola_mais_sorteada = B15_frame_primeira_e_segunda_bola_mais_sorteada['Unnamed: 0']
######################################################################################################################
concatenando_primeira_e_segunda_bola_mais_sorteada = pd.concat([B1_primeira_e_segunda_bola_mais_sorteada,
           B2_primeira_e_segunda_bola_mais_sorteada,
          B3_primeira_e_segunda_bola_mais_sorteada,
          B4_primeira_e_segunda_bola_mais_sorteada,
          B5_primeira_e_segunda_bola_mais_sorteada,
          B6_primeira_e_segunda_bola_mais_sorteada,
          B7_primeira_e_segunda_bola_mais_sorteada,
          B8_primeira_e_segunda_bola_mais_sorteada,
          B9_primeira_e_segunda_bola_mais_sorteada,
          B10_primeira_e_segunda_bola_mais_sorteada,
          B11_primeira_e_segunda_bola_mais_sorteada,
          B12_primeira_e_segunda_bola_mais_sorteada,
          B13_primeira_e_segunda_bola_mais_sorteada,
          B14_primeira_e_segunda_bola_mais_sorteada,
          B15_primeira_e_segunda_bola_mais_sorteada], axis=1, ignore_index=True)
######################################################################################################################
renomeando_cabecalho = concatenando_primeira_e_segunda_bola_mais_sorteada.rename(columns={0: 'B1',
                                                                                         1: 'B2',
                                                                                         2: 'B3',
                                                                                         3: 'B4',
                                                                                         4: 'B5',
                                                                                         5: 'B6',
                                                                                         6: 'B7',
                                                                                         7: 'B8',
                                                                                         8: 'B9',
                                                                                         9: 'B10',
                                                                                         10: 'B11',
                                                                                         11: 'B12',
                                                                                         12: 'B13',
                                                                                         13: 'B14',
                                                                                         14: 'B15'})
bolas_mais_sorteadas = renomeando_cabecalho
bolas_mais_sorteadas.to_csv(r'C:\lotoFacilLast100\dados\bolas_mais_sorteadas.csv',index=False, sep=';')