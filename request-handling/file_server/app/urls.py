import datetime

from django.urls import path, register_converter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app import converters
from app.views import file_list, file_content

register_converter(converters.DateConverter, 'dt')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dt:date>', file_list, name='file_list'),
    path('file_content/<name>/', file_content, name='file_content')
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    # path(..., name='file_list'),
    # path(..., name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    # path(..., name='file_content'),
]
