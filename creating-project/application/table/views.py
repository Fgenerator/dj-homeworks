import csv

from django.shortcuts import render

from table.models import Column, Data

from pathlib import Path


CSV_FILENAME = Path(Data.get_path()).name

COLUMNS = Column.objects.all().order_by('serial_number')


def table_view(request):
    template = 'table.html'
    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS,
            'table': table,
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
