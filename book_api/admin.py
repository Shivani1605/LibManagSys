from django.contrib import admin

from .models import Books

# Register your models here.
@admin.register(Books)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','book_quantity','book_gener','status']