from django.contrib import admin
from .models import *


class VideoInLine(admin.StackedInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInLine]


admin.site.register(Video)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Comments)
