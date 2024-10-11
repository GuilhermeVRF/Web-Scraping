from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils import CSVReader

# Tornando o navegador um objeto
browser = webdriver.Chrome()
browser.get('https://www.mercadolivre.com.br/')

# Lendo a planilha contendo os produtos
productsCSV = CSVReader.read()

# Procurando um elemento na barra de pesquisa
searchInput = browser.find_element(By.CLASS_NAME, 'nav-search-input')
searchInput.send_keys('Monitor')
searchInput.submit()

input("Pressione Enter para fechar o navegador...")


