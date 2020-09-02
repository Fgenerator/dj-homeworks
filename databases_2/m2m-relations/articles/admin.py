from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_check = False
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print(form.cleaned_data)
            if is_main_check and form.cleaned_data.get('is_main'):
                raise ValidationError('Основным может быть только один раздел')
            if form.cleaned_data.get('is_main'):
                is_main_check = True
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
        if not is_main_check:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInLine(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInLine,
    ]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInLine,
    ]