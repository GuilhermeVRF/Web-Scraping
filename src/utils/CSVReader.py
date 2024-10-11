import csv

def read():
    with open('C:\\Users\\guilh\\Documentos\\Sites\\Web Scraping\\Sheet.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)