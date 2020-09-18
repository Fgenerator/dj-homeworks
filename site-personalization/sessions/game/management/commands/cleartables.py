from django.core.management.base import BaseCommand

from game.models import Player, Game


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Player.objects.all().delete()
        Game.objects.all().delete()
