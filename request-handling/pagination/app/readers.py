import csv


def read_csv(file):
    data = []
    with open(file, encoding='windows-1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
