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

        items = Item.objects.filter(
            item_type=item_type,
            transaction_date__year=month.strftime('%Y'),
            transaction_date__month=month.strftime('%m')
        )

        item_list = []
        for  i in items:
            item_list.append(i.amount)

        item_type_data['items'] = item_list
        item_type_data['sum'] = sum(item_list)
        month_data['month_total'] += item_type_data['sum']
        month_data['item_types'].append(item_type_data)

    return month_data