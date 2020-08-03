from .models import Item, ItemType

def get_month(month):

    item_types = ItemType.objects.all()

    month_data = {
        'item_types': [],
        'month_total': 0
    }

    for item_type in item_types:

        item_type_data = {
            'name': item_type.name,
            'items': []
        }

        item_query = Item.objects.filter(
            item_type=item_type,
            transaction_date__year=month.strftime('%Y'),
            transaction_date__month=month.strftime('%m')
        ).order_by('transaction_date')

        item_amounts = []
        items = []
        for  i in item_query:
            item_amounts.append(i.amount)
            item = {
                'id': i.id,
                'amount': i.amount
            }
            items.append(item)

        item_type_data['items'] = items
        item_type_data['sum'] = sum(item_amounts)
        month_data['month_total'] += item_type_data['sum']
        month_data['item_types'].append(item_type_data)

    return month_data