from django.shortcuts import render

from databank.models.genus import Genus
from databank.models.language import Language


def genus_page(request):
    cur_genus_name = request.GET.get("name")
    cur_genus_obj = Genus.objects.get(name=cur_genus_name)

    context = {
        "cur_genus": cur_genus_obj,
        "genus_list": Genus.objects.all(),
        "cur_genus_langs": Language.objects.filter(genus=cur_genus_obj.id),
    }
    return render(request, "genus.html", context)
