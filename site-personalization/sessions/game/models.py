from django.db import models


class Player(models.Model):
    pass


class Game(models.Model):
    number = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    final_attempts = models.IntegerField(default=0)
    players = models.ManyToManyField(
        Player,
        through='PlayerGameInfo',
        default=None,
    )


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
