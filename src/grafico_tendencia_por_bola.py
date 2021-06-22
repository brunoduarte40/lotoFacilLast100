import pandas as pd
import matplotlib.pyplot as plt
dataFrame_baixado = pd.read_csv(
        r'C:\lotoFacilLast100\dados\LOTOFACIL.csv', sep=';')
dataFrame_baixado_B1 = dataFrame_baixado[['B1']]
dataFrame_baixado_B2 = dataFrame_baixado[['B2']]
dataFrame_baixado_B3 = dataFrame_baixado[['B3']]
dataFrame_baixado_B4 = dataFrame_baixado[['B4']]
dataFrame_baixado_B5 = dataFrame_baixado[['B5']]
dataFrame_baixado_B6 = dataFrame_baixado[['B6']]
dataFrame_baixado_B7 = dataFrame_baixado[['B7']]
dataFrame_baixado_B8 = dataFrame_baixado[['B8']]
dataFrame_baixado_B9 = dataFrame_baixado[['B9']]
dataFrame_baixado_B10 = dataFrame_baixado[['B10']]
dataFrame_baixado_B11 = dataFrame_baixado[['B11']]
dataFrame_baixado_B12 = dataFrame_baixado[['B12']]
dataFrame_baixado_B13 = dataFrame_baixado[['B13']]
dataFrame_baixado_B14 = dataFrame_baixado[['B14']]
dataFrame_baixado_B15 = dataFrame_baixado[['B15']]
######################################################################################################################
tendenciaB1 = dataFrame_baixado_B1.hist()
plt.rc(tendenciaB1)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB1.png', format='png')

tendenciaB2 = dataFrame_baixado_B2.hist()
plt.rc(tendenciaB2)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB2.png', format='png')

tendenciaB3 = dataFrame_baixado_B3.hist()
plt.rc(tendenciaB3)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB3.png', format='png')

tendenciaB4 = dataFrame_baixado_B4.hist()
plt.rc(tendenciaB4)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB4.png', format='png')

tendenciaB5 = dataFrame_baixado_B5.hist()
plt.rc(tendenciaB5)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB5.png', format='png')

tendenciaB6 = dataFrame_baixado_B6.hist()
plt.rc(tendenciaB6)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB6.png', format='png')

tendenciaB7 = dataFrame_baixado_B7.hist()
plt.rc(tendenciaB7)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB7.png', format='png')

tendenciaB8 = dataFrame_baixado_B8.hist()
plt.rc(tendenciaB8)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB8.png', format='png')

tendenciaB9 = dataFrame_baixado_B9.hist()
plt.rc(tendenciaB9)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB9.png', format='png')

tendenciaB10 = dataFrame_baixado_B10.hist()
plt.rc(tendenciaB10)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB10.png', format='png')

tendenciaB11= dataFrame_baixado_B11.hist()
plt.rc(tendenciaB11)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB11.png', format='png')

tendenciaB12 = dataFrame_baixado_B12.hist()
plt.rc(tendenciaB12)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB12.png', format='png')

tendenciaB13 = dataFrame_baixado_B13.hist()
plt.rc(tendenciaB13)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB13.png', format='png')

tendenciaB14 = dataFrame_baixado_B14.hist()
plt.rc(tendenciaB14)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB14.png', format='png')

tendenciaB15 = dataFrame_baixado_B15.hist()
plt.rc(tendenciaB15)
plt.savefig(r'C:\lotoFacilLast100\dados\TendenciaB15.png', format='png')
