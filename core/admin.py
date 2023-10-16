from django.contrib import admin
from .models import Client, Site, FilterWords, Notification, Article

admin.site.register(Client)
admin.site.register(Site)
admin.site.register(FilterWords)
admin.site.register(Notification)
admin.site.register(Article)

