from products.models import Category, Region


def categories(request):
    return {'categories': Category.objects.filter(level=0)}


def regions(request):
    return {'regions': Region.objects.filter(active=True)}