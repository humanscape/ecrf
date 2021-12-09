from django.contrib import admin

from .models import *
from .forms import IrdForm, IrdHistoryForm
from .assets import RADIO_FIELDS


@admin.register(Ird)
class IrdAdmin(admin.ModelAdmin):
    form = IrdForm

    list_display = (
        'case_no',
        'name',
        'birth_year_and_month',
    )
    list_display_links = list_display
    list_filter = list_display

    # choice field: display radio
    radio_fields = {
        radio_field: admin.HORIZONTAL for radio_field in RADIO_FIELDS['ird']
    }


@admin.register(IrdHistory)
class IrdHistoryAdmin(admin.ModelAdmin):
    form =IrdHistoryForm

    list_display = (
        'id',
        'name',
        'birthdate',
    )
    list_display_links = list_display
    list_filter = list_display

    # choice field: display radio
    radio_fields = { 
        radio_field: admin.HORIZONTAL for radio_field in RADIO_FIELDS['ird_history']
    }
