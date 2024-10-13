import csv

def read():
    with open('C:\\Users\\guilh\\Documentos\\Sites\\Web Scraping\\Sheet.csv', 'r') as file:
        reader = csv.reader(file)
        
        # Ignorando o cabeçalho
        next(reader, None)