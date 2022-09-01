from django.contrib import admin

# Register your models here.
from .models import Nick,Comment
admin.site.register(Comment)
@admin.register(Nick)
class NickAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Nick
