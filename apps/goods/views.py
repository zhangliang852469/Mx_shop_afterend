from rest_framework.pagination import PageNumberPagination  # 自定义分页
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend # 过滤

from .models import Goods
from .serliazer import GoodsSerializer
from .filters import GoodsFilter

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """自定义分页"""
    page_size = 10  # 默认分页
    page_size_query_param = 'page_size' # 自定义分页数量
    page_query_param = 'p'  # 指定分页参数为p
    max_page_size = 100 # 单页最大数量


class GoodsListDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """商品列表页, 详细页"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)  # 过滤配置
    filter_class = GoodsFilter  # 导入fitlters.py 中的类实现










