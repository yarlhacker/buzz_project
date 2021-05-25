from django.shortcuts import get_object_or_404, render
from . import models
from service import models as models_service


def index(request):
    banners = models.Banner.objects.filter(status=True)
    imagebanner = models.ImageBanner.objects.filter(status=True)
    siteweb = models.SiteWeb.objects.filter(status=True)
    categorieservices = models_service.CategorieService.objects.filter(status=True)
    services= models_service.Service.objects.filter(status=True)
    return render(request, 'index.html',locals())

def about(request):
    infoabout = models.AboutInfo.objects.filter(status = True)
    return render(request, 'about.html',locals())


def contact(request):
    siteweb = models.SiteWeb.objects.filter(status=True)
    return render(request, 'contact.html',locals())

def pricing(request):
    siteweb = models.SiteWeb.objects.filter(status=True)
    return render(request, 'pricing.html',locals())

def work(request):
    siteweb = models.SiteWeb.objects.filter(status=True)
    return render(request, 'work.html',locals())

def work_pricing(request,id):
    work = get_object_or_404(models_service.Work, id=id)
    siteweb = models.SiteWeb.objects.filter(status=True)
    return render(request, 'work-single.html',locals())


# Create your views here.
