from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def base(request):
    return render(request, "base.html")

def home(request, c_slug=None):
    c_page = None
    pro = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        pro = product.objects.filter(category=c_page, available=True)
    else:
        pro = product.objects.filter(available=True)
    cat = categ.objects.all()

    paginator = Paginator(pro, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except:
        products = paginator.page(paginator.num_pages)

    return render(request, "index.html", {'res': products, 'ca': cat})


def prod(request, c_slug, p_slug):
    try:
        pr = product.objects.get(category__slug=c_slug, slug=p_slug)
    except 'exception ' as e:
        raise e
    return render(request, "product.html", {'ob': pr})


def searching(request):
    query = None
    pro = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        pro = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, "search.html", {'qr': query, 'res': pro})

