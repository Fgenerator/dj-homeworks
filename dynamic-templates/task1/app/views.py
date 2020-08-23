from django.shortcuts import render

from app.readers import read_csv

DATA = read_csv('inflation_russia.csv')


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {
        'data': DATA
    }

    return render(request, template_name,
                  context)