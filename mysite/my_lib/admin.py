from django.contrib import admin

from .models import Document, Writer, Publisher

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Document info', {'fields' : ['name', 'document_type', 'document_genre', 'pub_date']}),
        ('Writer', {'fields' : ['writer']}),
        ('Publisher', {'fields' : ['publisher']}),
        ]
    list_display = ('name', 'writer', 'pub_date')

class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date')

admin.site.register(Document, DocumentAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Publisher, PublisherAdmin)
