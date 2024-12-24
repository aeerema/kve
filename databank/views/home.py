from django.shortcuts import render

from databank.models.language import Language


def home_page(request):
    context = {
        "lang_list": Language.objects.all(),
    }
    return render(request, "home.html", context)
