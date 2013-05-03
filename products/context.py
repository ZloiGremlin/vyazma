from products.models import Category, Region


def categories(request):
    return {'categories': Category.tree.all()}


def regions(request):
    return {'regions': Region.objects.filter(active=True)}