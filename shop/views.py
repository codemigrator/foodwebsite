from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify as _slugify
from django.db.models import Q
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
import datetime

def home(request, c_slug=None):
    c_page = None
    prodt = None
    date = datetime.date.today
    data = product.objects.filter(is_featured=True).order_by('-id')
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = product.objects.filter(category=c_page, available=True)
    else:
        prodt = product.objects.all().filter(available=True)
    ca = categ.objects.all()
    paginator = Paginator(prodt,6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'pt':prodt,'ct': ca,'pg':pro,'data':data,'date':date})
def productDetails(request,c_slug,product_slug):
    try:
        category=categ.objects.get(slug=c_slug)
        print(c_slug)
        print(product_slug)
        prod = product.objects.get(category=category, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'item.html', {'pt': prod})
def searching(request):
    query = None
    prod = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod =product.objects.all().filter(Q(name__contains= query)|Q(desc__contains= query))
    return render(request,'search.html',{'qr': query,'pt': prod})


# Create your views here.
