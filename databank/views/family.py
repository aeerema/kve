from django.shortcuts import render

from databank.models.family import Family
from databank.models.language import Language


def family_page(request):
    cur_family_name = request.GET.get("name")
    cur_family_obj = Family.objects.get(name=cur_family_name)

    context = {
        "cur_family": cur_family_obj,
        "family_list": Family.objects.all(),
        "cur_family_langs": Language.objects.filter(family=cur_family_obj.id),
    }
    return render(request, "family.html", context)