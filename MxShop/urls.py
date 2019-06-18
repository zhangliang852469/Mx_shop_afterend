from rest_framework import routers
from django.conf.urls import url, include
import xadmin

from MxShop.settings import MEDIA_ROOT  #导 入配置文件中的配置
from django.views.static import serve
from goods.views import GoodsListDetailViewSet, CategoryViewSet

# 配置路由
router = routers.DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListDetailViewSet, base_name='goods')  # 商品列表和详细

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')  # 商品分类列表

urlpatterns = [

    url(r'', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls')), # api 登录
]

# urlpatterns = router.urls