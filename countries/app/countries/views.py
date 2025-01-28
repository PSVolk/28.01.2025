from django.http import HttpResponse
from django.template import loader

from .reg import countries_all, countries_name, regions_api


def view_all(request):
    c = countries_all()
    template = loader.get_template("all.html")
    context = {'countries': c}
    return HttpResponse(template.render(context, request))


def country_info(request, country):
    c = countries_name(str(country))
    template = loader.get_template("c_name.html")
    context = {'country': c}
    return HttpResponse(template.render(context, request))

def regions(request):
    c = regions_api()
    template = loader.get_template("regions.html")
    context = {'regions': c}
    return HttpResponse(template.render(context, request))
