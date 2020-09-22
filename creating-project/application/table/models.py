from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=30)
    width = models.IntegerField()
    serial_number = models.IntegerField()


class Data(models.Model):
    file_path = models.FilePathField()

    @classmethod
    def get_path(cls):
        path = cls.objects.all()[0]
        return path

    @classmethod
    def set_path(cls, path):
        cls.objects.all().delete()
        cls.objects.create(file_path=path)

