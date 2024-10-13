import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from src.utils import CSVWriter
from collections import Counter

def currency_format(value):
    # Remove os separadores de milhar (pontos)
    value = value.replace('.', '')
    # Substitui a vírgula pelo ponto
    value = value.replace(',', '.')
    return value

# Definindo opção para o navegador rodar em 2° plano
options = Options()
# options.add_argument('--headless')

# Tornando o navegador um objeto
browser = webdriver.Chrome(options=options)

# Lendo a planilha contendo os produtos
with open('C:\\Users\\guilh\\Documentos\\Sites\\Web Scraping\\Sheet.csv', 'r') as file:
    productsCSV = csv.reader(file, delimiter=';')
    
    # Ignorando o cabeçalho
    next(productsCSV, None)

    for row in productsCSV:
        productCode = row[0]
        productName = row[1]
        productLength = row[2]
        productWidth = row[3]
        productHeight = row[4]

        # Pegando as dimensões do produto
        productsDimensions = row[2] + 'cm x ' + row[3] + 'cm x ' + row[4] + 'cm'

        browser.get('https://www.google.com/search?q=Decoração ' + productName + ' ' +productsDimensions)

        # Clicando na aba 'Shopping'
        try:
            shopping_tab = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Shopping'))
            )
            shopping_tab.click()
        except Exception as e:
            print(f'Erro ao clicar na aba Shopping: {str(e)}')


        # Pegando os preços dos produtos listados
        productPrices = []
        try:
            divPrices = WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(text(), 'R$')]"))
             )

            # Percorrendo cada preço encontrado
            for divPrice in divPrices[:10]:
                price = divPrice.text
                price = price.replace('R$ ', '')
                price = currency_format(price)

                # Formatando as informações deproço obtida para decimal
                if re.match(r'^[0-9.]+$', price):
                    productPrices.append(float(price))
        except Exception as e:
            print(f'Não foi possível pegar o preço do produto! {e}')

        # Armazenando o produto com as informações do preço
        CSVWriter.write([productCode, productName, productPrices])

        continue
