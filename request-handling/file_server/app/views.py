import datetime
import os

from django.shortcuts import render
from django.conf import settings

from pathlib import Path


FILES_PATH = Path(settings.FILES_PATH)


def get_ctime(file):
    raw_ctime = file.stat().st_ctime
    converted_ctime = datetime.datetime.fromtimestamp(raw_ctime)
    return converted_ctime


def get_mtime(file):
    raw_mtime = file.stat().st_mtime
    converted_mtime = datetime.datetime.fromtimestamp(raw_mtime)
    return converted_mtime


def prepare_files(files, date=None):
    temp_context = {
        'files': []
    }
    for file in files:
        converted_ctime = get_ctime(file)

        converted_mtime = get_mtime(file)

        if not date or converted_ctime.date() == date.date():
            temp_context['files'].append(
                {
                    'name': file.name,
                    'ctime': converted_ctime,
                    'mtime': converted_mtime
                }
            )
    return temp_context


def file_list(request, date=None):
    template_name = 'index.html'
    files = Path.iterdir(FILES_PATH)
    context = {
        'files': [],
        'date': ''
    }
    if date:
        #context['date'] = date
        context['files'] = prepare_files(files, date)['files']

    else:
        context['files'] = prepare_files(files)['files']



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
    file_to_open = FILES_PATH.joinpath(name)

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

