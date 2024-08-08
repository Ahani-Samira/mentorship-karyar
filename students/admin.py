from django.contrib import admin
from .models import Student

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'grade', 'last_name')
    search_fields = ('first_name',)
    

