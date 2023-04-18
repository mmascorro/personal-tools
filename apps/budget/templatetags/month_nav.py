from django import template
from datetime import datetime
from dateutil.relativedelta import relativedelta

register = template.Library()

@register.simple_tag
def prev_month(year_month):
    prev_month = year_month - relativedelta(months=1)
    return prev_month.strftime('%Y-%m')

@register.simple_tag
def next_month(year_month):
    prev_month = year_month + relativedelta(months=1)
    return prev_month.strftime('%Y-%m')
