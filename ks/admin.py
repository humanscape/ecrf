from django.contrib import admin
from .forms import KsForm
from .assets import RADIO_FIELDS
from .models import *


class Ks_pnuh_historyInline(admin.TabularInline):
    model = Ks_pnuh_history
    fields = (
        'history_1', 'history_2'
    )
    extra = 1


class Ks_pnuh_con_medInline(admin.TabularInline):
    model = Ks_pnuh_con_med
    fields = (
        'con_med_1', 'con_med_2'
    )
    extra = 1


@admin.register(Ks_pnuh)
class KsAdmin(admin.ModelAdmin):
    form = KsForm

    inlines = (Ks_pnuh_historyInline, Ks_pnuh_con_medInline)

    list_display = (
        'patient_number',
        'icf_date',
        'sex',
        'birthdate',
    )
    list_display_links = list_display
    list_filter = list_display

    # choice field: display radio
    radio_fields = {
        radio_field: admin.HORIZONTAL for radio_field in RADIO_FIELDS['ks']
    }


@admin.register(Ks_snuh)
class KsSnuhAdmin(admin.ModelAdmin):
    form = KsForm

    list_display = (
        'patient_number',
        'icf_date',
        'sex',
        'birthdate',
    )
    list_display_links = list_display
    list_filter = list_display

