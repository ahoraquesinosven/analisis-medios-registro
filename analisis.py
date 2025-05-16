import tldextract
from urllib.parse import urlparse, urlunparse, quote, unquote, parse_qs
import pandas as pd


# # TESTING  
# source = pd.read_csv('./cases/20250513_2023_2024_2025_casos.csv')
# fechas_casos = source['Fecha_del_Caso']
# print(fechas_casos)



# # TESTING  
# url = "https://otrasvocesmdz.com.ar/brutal-intento-de-femicidio-en-el-palomar-apunalo-a-su-ex-pareja-y-huyo/"
# parsed_url = urlparse(url)
# print("Netloc:", parsed_url.netloc)

# extracted_info = tldextract.extract(parsed_url.netloc)
# print("Extracted info: ",extracted_info)

#Obtener domain 
def get_url_domain(url):
    #print("URL: ",url)
    parsed_url = urlparse(url)
    extracted_info = tldextract.extract(parsed_url.netloc)
    return extracted_info.domain

#obtener los campos que quiero analizar mes y año,  provincia, category y domain
def get_fields_for_analysis(csv):
    df = pd.read_csv(csv)
    return df.loc[:, ["Fecha_del_Caso","Provincia","Clasificacion","link1"]]

cases_2023_to_2025 = get_fields_for_analysis('./cases/20250513_2023_2024_2025_casos.csv')
# medio = get_url_domain(cases_2023_to_2025['link1'])
# print("MEDIO = ", medio)
cases_2023_to_2025["medio"] = cases_2023_to_2025.apply(lambda row: get_url_domain(row.link1), axis='columns')
cases_2023_to_2025.to_csv('fullMedios_2023_2025.csv')
print(cases_2023_to_2025.head())
# TODO https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html 
 

#  group by domain y provincia
byprov = cases_2023_to_2025[["Provincia","medio"]].groupby("medio").count()
print(byprov.head())

# group by domain y categoria
cat = cases_2023_to_2025[["Clasificacion","medio"]].groupby("medio").count()
print(cat.head())

 