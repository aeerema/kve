from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from databank.models.language import Language
from databank.models.comment import Comment
# from databank.models.comment_image import CommentImage
from databank.forms.tense_marker_form import FutForm, PstForm
from databank.forms.tense_system_form import TenseSystemForm
from databank.forms.combinations_form import MMForm, MAForm, AMForm, AAForm
from databank.forms.main_comment_form import MainCommentForm
from databank.forms.comment_form import CommentForm
# from databank.forms.comment_image_form import CommentImageForm


def lang_page(request):
    cur_lang_code = request.GET.get("code")
    cur_lang_obj = Language.objects.get(code=cur_lang_code)

    comments = Comment.objects.filter(lang=cur_lang_obj)
    new_comment_form = None

    if request.method == 'POST':
        if request.POST.get("pst") is not None:
            pst_form = PstForm(request.POST, instance=cur_lang_obj)
            pst_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("fut") is not None:
            fut_form = FutForm(request.POST, instance=cur_lang_obj)
            fut_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("tense_system") is not None:
            tense_system_form = TenseSystemForm(request.POST, instance=cur_lang_obj)
            tense_system_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("mm") is not None:
            mm_form = MMForm(request.POST, instance=cur_lang_obj)
            mm_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("ma") is not None:
            ma_form = MAForm(request.POST, instance=cur_lang_obj)
            ma_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("am") is not None:
            am_form = AMForm(request.POST, instance=cur_lang_obj)
            am_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("aa") is not None:
            aa_form = AAForm(request.POST, instance=cur_lang_obj)
            aa_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("main_comment") is not None:
            main_comment_form = MainCommentForm(request.POST, instance=cur_lang_obj)
            main_comment_form.save()
            return HttpResponse(status=200)
        elif request.POST.get("add_comment") is not None:
            new_comment = Comment.objects.create(lang=cur_lang_obj)
            new_comment_form = CommentForm(instance=new_comment, prefix=str(new_comment.id))
            # new_image = CommentImage.objects.create(comment=new_comment)
            # new_image_form = CommentImageForm(instance=new_image)
            return  HttpResponse(new_comment_form, status=200)
        else:
            comment_forms = []
            for c in Comment.objects.filter(lang=cur_lang_obj):
                form = CommentForm(request.POST, prefix=str(c.id), instance=c)
                if form.is_valid():
                    form.save()
                    comment_forms.append(form)
                else:
                    c.delete()
            return HttpResponse(status=200)
            
    
    context = {
        "cur_lang": cur_lang_obj,
        "lang_list": Language.objects.all(),
        "forms":{
            "ts": TenseSystemForm(instance=cur_lang_obj),
            "fut": FutForm(instance=cur_lang_obj),
            "pst": PstForm(instance=cur_lang_obj),
            "mm": MMForm(instance=cur_lang_obj),
            "ma": MAForm(instance=cur_lang_obj),
            "am": AMForm(instance=cur_lang_obj),
            "aa": AAForm(instance=cur_lang_obj),
            "main_comment": MainCommentForm(instance=cur_lang_obj),
            "comments": [CommentForm(instance=c, prefix=str(c.id)) for c in comments],
            "new_comment": new_comment_form,
        },
    }
    return render(request, "lang.html", context)
