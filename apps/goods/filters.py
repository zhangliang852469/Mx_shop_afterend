# -*- coding: utf-8 -*-
#!/usr/bin/env python3


from django_filters import rest_framework
from .models import Goods


class GoodsFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(name="shop_price", lookup_expr='gte', help_text="最低价格")
    max_price = rest_framework.NumberFilter(name="shop_price", lookup_expr='lte', help_text="最高价格")

    class Meta:
        model = Goods
        fields = ['name', 'goods_sn', 'min_price', 'max_price']
