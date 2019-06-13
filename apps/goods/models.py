from django.db import models
from DjangoUeditor.models import UEditorField

from db_models.base_models import BaseModels



# Create your models here.


class GoodsCategory(BaseModels, models.Model):
    """ 商品类别"""
    CHOICES_CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(max_length=30, default='', verbose_name='类别名', help_text='类别名')
    code = models.CharField(max_length=30, default='', verbose_name='类别编码', help_text='类别编码')
    desc = models.TextField(default='', verbose_name='类别描述', help_text='类别描述')
    category_type = models.SmallIntegerField(choices=CHOICES_CATEGORY_TYPE, verbose_name='类目级别',
                                             help_text='类目级别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父目录级别',
                                        help_text='父目录级别', related_name='sub_cat')
    is_table = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(BaseModels, models.Model):
    """品牌名"""
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类目', null=True, blank=True,
                                 related_name='brands')
    name = models.CharField(default='', verbose_name='品牌名', max_length=30, help_text='品牌名')
    desc = models.CharField(default='', max_length=300, verbose_name='品牌描述', help_text='品牌描述')
    image = models.ImageField(max_length=200, upload_to='brands/images/')

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(BaseModels, models.Model):
    """商品"""
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类目')
    goods_sn = models.CharField(max_length=50, default='', verbose_name='商品货号')
    name = models.CharField(max_length=100, verbose_name='商品名称')
    click_num = models.IntegerField(verbose_name='点击数', default=0)
    sold_num = models.IntegerField(verbose_name='销售数量', default=0)
    fav_num = models.IntegerField(verbose_name='收藏数量', default=0)
    goods_num = models.IntegerField(default=0, verbose_name='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name="内容", imagePath="goods/images/",
                              width=1000, height=300, filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=False, verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(BaseModels, models.Model):
    """首页商品类别广告"""
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="商品类目")
    goods = models.ForeignKey(Goods, related_name='goods')

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(BaseModels, models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="goods/images", verbose_name="图片", null=True, blank=True)

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(BaseModels, models.Model):
    """轮播的商品"""
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='brands/', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(BaseModels, models.Model):
    """热搜词"""
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords




