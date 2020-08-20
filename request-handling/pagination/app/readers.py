import csv


def read_csv(file):
    with open(file, encoding='windows-1251') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data
