from django.contrib import admin
from tweet.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Section', {'fields': ('user',)}),
        ('Tweet Section', {'fields': ('tweet',)})
    ]

admin.site.register(Tweet, TweetAdmin)