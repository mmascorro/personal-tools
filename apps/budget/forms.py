from django import forms
from .models import Bank, Item, ItemType

class InputForm(forms.Form):
    bank = forms.ModelChoiceField(queryset=Bank.objects.all())
    item_type = forms.ModelChoiceField(queryset=ItemType.objects.all())
    amount = forms.DecimalField()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['bank', 'item_type', 'amount']