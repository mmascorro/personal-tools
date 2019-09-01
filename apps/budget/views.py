from datetime import date, datetime

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

        month_history = Item.objects.dates('transaction_date', 'month', order='DESC')

        if not year_month:
            current_month = date.today()
        else:
            current_month = datetime.strptime(year_month, '%Y-%m')


        context = {
            'month_data': get_month(current_month),
            'year_month': year_month,
            'months': month_history
        }

    
        return render(request, 'budget/month.html', context)