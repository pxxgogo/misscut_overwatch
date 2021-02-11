from django.contrib import admin
from text.models import TextFile

# Register your models here.
class TextFileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('create_time', {'fields': ['create_time']}),
        ('content_file', {'fields': ['file']}),
        ('ret_file', {'fields': ['ret_file']}),
        ('finish_flag', {'fields': ['finish_flag']}),

    ]
    list_display = ('id', 'create_time', 'finish_flag')

admin.site.register(TextFile, TextFileAdmin)
