from django.conf.urls import patterns, include, url
from products.views import FrontView, CategoryDetail, TraderDetail, ProductDetail
from vyazma import settings
from shop import urls as shop_urls
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', FrontView.as_view(), name='front'),
                       url(r'^category/(?P<slug>[0-9A-Za-z-_.//]+)/$', CategoryDetail.as_view(), name='category'),
                       url(r'^traders/(?P<slug>[0-9A-Za-z-_.//]+)/$', TraderDetail.as_view(), name='trader'),
                       url(r'^products/(?P<slug>[0-9A-Za-z-_.//]+)/$', ProductDetail.as_view(), name='product_details'),
                       # url(r'^catalog/$', CatalogView.as_view(), name='catalog'),
                       # url(r'^catalog/(?P<slug>[0-9A-Za-z-_.//]+)/$', CatalogCategory.as_view(), name='catalog_detail'),
                       # url(r'^painters/(?P<slug>[0-9A-Za-z-_.//]+)/$', CategoryDetail.as_view(), name='painters_detail'),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^shop/', include(shop_urls)),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
