from datetime import date, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import QueryDict

from .models import Show

class MainView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        return render(request, 'episodetracker/index.html', context)


class ShowView(LoginRequiredMixin, View):

    def get(self, request):
        shows =  list(Show.objects.order_by('name').values())
        response = JsonResponse(shows, safe=False)
        return response

    def post(self, request):
        if request.POST['name']: 
            print(request.POST['name'])
            show = Show(name=request.POST['name'])
            show.save()

        response = JsonResponse({'msg':'ok'})
        return response


class ShowUpdateView(LoginRequiredMixin, View):

    def post(self, request, id):
        show = Show.objects.get(pk=id)
        if request.POST['action'] == 'update':
            show.episode = request.POST['episode']
            show.save()
        elif request.POST['action'] == 'delete':
            show.delete()

        response = JsonResponse({'msg':'ok'})
        return response