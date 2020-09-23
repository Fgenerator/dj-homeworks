from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=30)
    width = models.IntegerField()
    serial_number = models.IntegerField(unique=True)


class Data(models.Model):
    file_path = models.CharField(max_length=100)

    @classmethod
    def get_path(cls):
        path = cls.objects.all()[0].file_path
        return path

    @classmethod
    def set_path(cls, path):
        from pathlib import Path
        cls.objects.all().delete()
        cls.objects.create(file_path=Path(path))

