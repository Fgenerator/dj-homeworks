from django.contrib import admin

from .models import Player, Game, PlayerGameInfo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id',)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'is_finished', 'final_attempts')


class PlayerGameInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'game', 'is_author', 'attempts')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)