import datetime
import os

from django.shortcuts import render
from django.conf import settings

from pathlib import Path


FILES_PATH = Path(settings.FILES_PATH)


def file_list(request, date=None):
    template_name = 'index.html'
    files = os.listdir(FILES_PATH)
    context = {
        'files': [],
        'date': ''
    }
    for file in files:
        file_to_open = FILES_PATH / file

        raw_ctime = os.path.getctime(file_to_open)
        converted_ctime = datetime.datetime.fromtimestamp(raw_ctime)
        raw_mtime = os.path.getmtime(file_to_open)
        converted_mtime = datetime.datetime.fromtimestamp(raw_mtime)


        # raw_ctime = os.stat(f'{file_to_open}').st_ctime
        # raw_mtime = os.stat(f'{file_to_open}').st_mtime
        #
        # converted_ctime = datetime.datetime.fromtimestamp(raw_ctime)
        # converted_mtime = datetime.datetime.fromtimestamp(raw_mtime)

        context['files'].append(
            {
               'name': file,
                'ctime': converted_ctime,
                'mtime': converted_mtime
            }
        )
    print(converted_ctime.date)
    print(converted_mtime.date)

    if date:
        context['date'] = date
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # context = {
    #     'files': [
    #         {'name': 'file_name_1.txt',
    #          'ctime': datetime.datetime(2018, 1, 1),
    #          'mtime': datetime.datetime(2018, 1, 2)}
    #     ],
    #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    # }

    return render(request, template_name, context)


def file_content(request, name):
    content = ''
    file_to_open = FILES_PATH / name

    with open(file_to_open, encoding='utf8') as file:
        for line in file:
            if content:
                content = f'{content}{line}'
            else:
                content = line
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

