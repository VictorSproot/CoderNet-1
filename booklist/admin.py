from django.contrib import admin
from .models import Book, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Book)
admin.site.register(Category)
