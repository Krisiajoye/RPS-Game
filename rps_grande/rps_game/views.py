from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from django.template import loader
from rps_game.models import UserSelection, Status
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    n = 1
    defaultSelection = UserSelection.objects.get(id=n)
    win_lose = Status.objects.get(id=n)
    context = {
        'userDef':defaultSelection,
        'state': win_lose,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))

def rock(request):
    user = UserSelection.objects.get(id=1)
    user.selection = "Rock"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def paper(request):
    user = UserSelection.objects.get(id=1)
    user.selection = "Paper"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def scissors(requet):
    user = UserSelection.objects.get(id=1)
    user.selection = "Scissors"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def play(request):
    choices = ['Rock', 'Paper', 'Scissors']
    randChoices = []
    for i in range(15):
        randChoices.append(choices[randint(0,2)])

    computer = randChoices[randint(0, len(randChoices))]

    user = UserSelection.objects.get(id=1)
    status = Status.objects.get(id=1)
    if user.selection == computer:
        status.stat = "You Win"
        status.score += 1
        status.save()
    else:
        status.stat = "You Lose"
        status.save()

    status.outoff += 1
    status.save()

    return(HttpResponseRedirect(reverse(index)))

def reset(request):
    default = UserSelection.objects.get(id=1)
    default.selection = "Select"
    default.save()

    default = Status.objects.get(id=1)
    default.stat = ""
    default.save()

    default = Status.objects.get(id=1)
    default.score = 0
    default.save()
    default.outoff = 0
    default.save()

    return HttpResponseRedirect(reverse(index))
