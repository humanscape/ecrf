from django.contrib import admin
from .models import *

@admin.register(Ird)
class IrdAdmin(admin.ModelAdmin):
    list_display = (
        'case_no',
        'name',
        'birth_year_and_month',
    )
    list_display_links = list_display
    list_filter = list_display

