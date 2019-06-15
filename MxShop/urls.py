from rest_framework import routers
from django.conf.urls import url, include
import xadmin

from MxShop.settings import MEDIA_ROOT  #导 入配置文件中的配置
from django.views.static import serve
from goods.views import GoodsListDetailViewSet

# 配置路由
router = routers.DefaultRouter()

router.register(r'goods', GoodsListDetailViewSet,)  # 商品列表和详细

urlpatterns = [

    url(r'', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls')), # api 登录
]

# urlpatterns = router.urls