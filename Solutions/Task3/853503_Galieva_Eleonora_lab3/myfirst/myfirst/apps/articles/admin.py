from django.contrib import admin
from .models import Article, Comment, Author, Account, Ad

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Account)
admin.site.register(Ad)