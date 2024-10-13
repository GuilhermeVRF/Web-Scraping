import csv

def write(rowData):
    with open('C:\\Users\\guilh\\Documentos\\Sites\\Web Scraping\\src\\content\\PricesSheet.csv',mode ='a', newline='',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        writer.writerow(rowData)
