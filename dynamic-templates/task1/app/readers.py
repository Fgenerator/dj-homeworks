import csv


def read_csv(file):
    with open(file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        data = list(reader)
    return data
