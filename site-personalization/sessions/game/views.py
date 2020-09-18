import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Player, Game, PlayerGameInfo
from .forms import GameForm


def show_home(request):
    return render(
        request,
        'home.html'
    )


def get_current_game_id():
    try:
        current_game_id = Game.objects.get(is_finished=False).id
    except ObjectDoesNotExist:
        return None
    except MultipleObjectsReturned:
        ...

    return current_game_id


class GameView(View):
    template = 'home.html'
    form = GameForm

    def get(self, request):
        player_id = request.session.get('player_id')
        game_id = request.session.get('game_id')

        if not player_id: # new player
            player_id = Player.objects.create().id
            request.session['player_id'] = player_id

        player = Player.objects.get(id=player_id)

        if not game_id and not get_current_game_id(): # no started games
            game_id = Game.objects.create(number=random.randint(1, 10)).id
            game = Game.objects.get(id=game_id)
            request.session['game_id'] = game_id
            Game.objects.get(id=game_id).players.add(player)

            info = PlayerGameInfo.objects.get(game=game)
            info.is_author = True
            info.save()

        elif not game_id and get_current_game_id(): # game started
            game_id = Game.objects.get(is_finished=False).id
            request.session['game_id'] = game_id
            Game.objects.get(id=game_id).players.add(player)

        if player_id and game_id: # player with game
            game = Game.objects.get(id=game_id)
            is_author = PlayerGameInfo.objects.get(player=player, game=game).is_author
            number = game.number

            context = {
                'number': number,
                'is_author': is_author,
                'form': self.form
            }

        if game.final_attempts:
            game.is_finished = True
            game.save()

            request.session['attempts'] = 0
            request.session['game_id'] = None

            if is_author:
                if game.final_attempts == 1:
                    context['message'] = 'Ваше число было угадано с 1 попытки'
                elif game.final_attempts > 1:
                    context['message'] = f'Ваше число было угадано с {game.final_attempts} попыток'
            else:
                context['brake'] = True
                context['message'] = 'Игра окончена'

        return render(request, self.template, context)

    def post(self, request):
        self.form = GameForm(request.POST)
        if self.form.is_valid():
            player_id = request.session.get('player_id')
            attempts = request.session.get('attempts', 0)
            number = self.form.cleaned_data['number']
            game_id = request.session['game_id']

            player = Player.objects.get(id=player_id)
            game = Game.objects.get(id=game_id)
            info = PlayerGameInfo.objects.get(game=game, player=player)

            info.attempts = attempts
            info.save()

            if number == game.number:
                info.attempts += 1
                info.save()
                game.final_attempts = info.attempts
                game.save()

                context = {
                    'form': self.form,
                    'message': 'Вы угадали число!'
                }

            elif number > game.number:
                info.attempts += 1
                info.save()
                request.session['attempts'] = info.attempts
                context = {
                    'form': self.form,
                    'message': f'Загаданное число меньше {number}'
                }

            elif number < game.number:
                info.attempts += 1
                info.save()
                request.session['attempts'] = info.attempts
                context = {
                    'form': self.form,
                    'message': f'Загаданное число больше {number}'
                }

        return render(request, self.template, context)
