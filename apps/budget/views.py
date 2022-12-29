from datetime import date, datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .forms import ItemForm
from .models import Bank, Item, ItemType
from .utilities import get_month

class InputView(LoginRequiredMixin, View):

    item_types = ItemType.objects.all()
    banks = Bank.objects.all()

    context = {
        'item_types': item_types,
        'banks': banks,
    }

    def get(self, request):

        context = {
            'item_types': self.item_types,
            'banks': self.banks,
        }
        return render(request, 'budget/index.html', self.context)

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            new_item = form.save()
            print(new_item)
            return render(request, 'budget/index.html', self.context)

class MonthDetail(LoginRequiredMixin, View):

    def get(self, request, year_month=None):

        month_list = list(reversed(range(1,13)))
        month_history = Item.objects.dates('transaction_date', 'month', order='DESC')
        year_list = list(reversed(range(month_history.last().year, date.today().year+1)))

        if not year_month:
            current_year_month = date.today()
        else:
            current_year_month = datetime.strptime(year_month, '%Y-%m')

        context = {
            'month_data': get_month(current_year_month),
            'year_list': year_list,
            'month_list': month_list,
            'current_year_month': current_year_month
        }

    
        return render(request, 'budget/month.html', context)

class EditItemView(LoginRequiredMixin, View):
    item_types = ItemType.objects.all()
    banks = Bank.objects.all()

    context = {
        'item_types': item_types,
        'banks': banks
    }

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        self.context['item'] = item
        return render(request, 'budget/edit-item.html', self.context)

    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            print(form.cleaned_data)

            item = form.save()
            print(item)
            self.context['item'] = item

            return render(request, 'budget/edit-item.html', self.context)


class ChartView(LoginRequiredMixin, View):

    def get(self, request):


        context = {
        }

    
        return render(request, 'budget/chart.html', context)