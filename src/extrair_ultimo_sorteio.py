import pandas as pd
from pandas import DataFrame
from lxml import html
import requests
import requests
import urllib
import bs4

########################################__Site_da_cotacao#########################
page = 'https://noticias.uol.com.br/loterias/lotofacil/'
page = requests.get("https://noticias.uol.com.br/loterias/lotofacil/")
tree = html.fromstring(page.content)
soup = bs4.BeautifulSoup(page.content, 'html.parser')
soup.get
soup = bs4.BeautifulSoup(page.content, 'html.parser')
soup.get_text()
all_text = soup.find_all(class_="quote")
all_text
quotes_raw = [comment.find_all(class_='text') for comment in all_text]
########################################__FIM_Site_da_cotacao#########################
tabela = tree.xpath('//*[@class="lt-number  loto-facil-colors border color"]/text()')
df_bolas = DataFrame (tabela)
df_bolas_horizontal = df_bolas.T
#########################################__codigo_a_cima_seleciona_as_bolas###########
infos = tree.xpath('//*[@class="lottery-info"]/span/text()')
string_list = ''.join(infos)
string_separada = string_list.split(" ")
string_concurso = string_separada[1]
#string_concurso
int_concurso_web = int(string_concurso)
print(int_concurso_web)
#################################pegando_ultimo_concurso##############################
dataFrame_baixado = pd.read_csv(r'C:\lotoFacilLast100\dados\LOTOFACIL.csv', sep=';')
######################################################################################
ultimo_concurso_registrado = dataFrame_baixado.loc[0, 'concurso']
int_ultimo_concurso_registrado = int(ultimo_concurso_registrado)

#########################_ultimo_concurso_como_inteiro###############################
int_concurso_web
int_ultimo_concurso_registrado
if int_concurso_web > int_ultimo_concurso_registrado: # End of condition
    print("concurso web eh maior que o ultimo concurso registrado")

    ###################################data_formato_2021#################################
    string_data = string_separada[4]
    string_data_com_barra = string_data.replace(".", "/")
    string_data_com_barra = string_data_com_barra.replace("21", "2021")
    string_data_com_barra

    ################organizando_bolas###################################################

    df_bolas_horizontal.rename(columns={0: 'B1', 1: 'B2', 2: 'B3', 3: 'B4', 4: 'B5', 5: 'B6',
                                        6: 'B7', 7: 'B8', 8: 'B9', 9: 'B10', 10: 'B11', 11: 'B12',
                                        12: 'B13', 13: 'B14', 14: 'B15'}, inplace=True)
    ##################################################################################
    data_frame_adicioando_novas_colunas = df_bolas_horizontal.assign(data=string_data_com_barra,
                                                                     concurso=string_concurso)
    data_frame_organizado = data_frame_adicioando_novas_colunas[
        ['concurso', 'data', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14',
         'B15']]
    data_frame_organizado.to_csv(r'C:\lotoFacilLast100\dados\ultimo_jogo.csv', sep=';', index=False)
    ###################################################################################
    ###################################################################################
    dataFrame_baixado = pd.read_csv(
        r'C:\lotoFacilLast100\dados\LOTOFACIL.csv', sep=';')
    ##############################concatenar_ultimo_jogo_com_resto#####################
    planilha_concatenada = pd.concat([data_frame_organizado, dataFrame_baixado])
    planilha_concatenada.to_csv(r'C:\lotoFacilLast100\dados\LOTOFACIL.csv', sep=';', index=False)
    ###################################################################################
    ###############################pegar_ultimo_concurso###############################
else:
    print("concurso web eh menor que o ultimo concurso registrado")
########################condição_para_gravar_nova_linha##############################






#####################################################################################