from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView,CreateView,UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trip,Leg
from .forms import TripForm, LegCreate, LegForm
from django.db.models import Count, Min

def edit_trip(request):
    return render(request, 'mileage/trip-edit.html')

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'mileage/index.html'
    context_object_name = 'trips_list'

    def get_queryset(self):
        return Trip.objects.annotate(start_min=Min('leg__start_date')).order_by('-start_min')

class CreateTripView(LoginRequiredMixin, CreateView):
    form_class = TripForm
    template_name = 'mileage/trip-edit.html'
    success_url = '/mileage/'


class TripDetailView(LoginRequiredMixin, View):
    template_name = "mileage/trip-detail.html"
    def get(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        legs = trip.leg_set.order_by('start_date')
        legForm = LegCreate
        return render(request, 'mileage/trip-detail.html', {'trip': trip, 'form':legForm, 'legs':legs})

    def post(self, request, pk):
        trip = Trip.objects.get(pk=pk)

        form = LegCreate(request.POST)
        if form.is_valid():
            newLeg = Leg(trip=trip, start_date=form.cleaned_data['start_date'], start_miles=form.cleaned_data['start_miles'] )
            newLeg.save()
            return HttpResponseRedirect(reverse('trip-detail', kwargs={'pk': pk}))
        else:
            return render(request, 'mileage/trip-detail.html', {'trip': trip, 'form':form})

class LegEditView(LoginRequiredMixin, UpdateView):
    model = Leg
    form_class = LegForm
    template_name = 'mileage/leg-edit.html'

    def get_success_url(self):
        return reverse('trip-detail', args=[self.object.trip.id])