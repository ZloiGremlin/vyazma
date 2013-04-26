# vim:fileencoding=utf-8
from django.views.generic import TemplateView, DetailView
from products.models import Category, Trader, Product, Region


class FrontView(TemplateView):
    template_name = 'front.html'

    def get_context_data(self, **kwargs):
        ctx = super(FrontView, self).get_context_data(**kwargs)
        ctx['traders'] = Trader.objects.all()
        return ctx

class CategoryDetail(DetailView):
    slug_field = 'url'
    slug_url_kwarg = 'slug'
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


class TraderDetail(DetailView):
    slug_field = 'url'
    slug_url_kwarg = 'slug'
    model = Trader
    template_name = 'trader.html'
    context_object_name = 'trader'


class ProductDetail(DetailView):
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    model = Product
    template_name = 'product.html'


class RegionView(DetailView):
    template_name = 'traders.html'
    model = Region
    slug_field = 'url'
    slug_url_kwarg = 'url'

