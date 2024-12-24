from django.shortcuts import render
from django.http import JsonResponse

from databank.models.language import Language


def main_comment(request):
    print("\n\n\n", request.GET, request.POST, sep="\n\n\n")
    cur_lang_code = request.GET.get("code")
    cur_lang_obj = Language.objects.get(code=cur_lang_code)
    return JsonResponse({'status': 'ok'})