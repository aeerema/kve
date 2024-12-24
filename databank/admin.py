from django.contrib import admin

from databank.models.language import Language
from databank.models.genus import Genus
from databank.models.family import Family
from databank.models.comment import Comment
# from databank.models.comment_image import CommentImage


admin.site.register(Language)
admin.site.register(Genus)
admin.site.register(Family)
admin.site.register(Comment)
# admin.site.register(CommentImage)