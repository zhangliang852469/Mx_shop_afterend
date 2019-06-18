from rest_framework.pagination import PageNumberPagination  # 自定义分页
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend # 过滤
from rest_framework import filters   # 模糊查询
from rest_framework import mixins

from .models import Goods, GoodsCategory
from .serliazer import GoodsSerializer, GoodsCategorySerializer
from .filters import GoodsFilter

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """自定义分页"""
    page_size = 10  # 默认分页
    page_size_query_param = 'page_size' # 自定义分页数量
    page_query_param = 'p'  # 指定分页参数为p
    max_page_size = 100  # 单页最大数量


class GoodsListDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """商品列表页, 详细页"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤配置
    filter_class = GoodsFilter  # 导入fitlters.py 中的类实现
    search_fields = ('name', 'goods_brief', 'goods_desc')  # 模糊搜索
    ordering_fields = ('add_time', 'update_time')  # 排序


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer








