from django.db import models


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()

    def __str__(self):
        return f'{self.id}. {self.name} {self.price} {self.release_date}'