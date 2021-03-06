from django.contrib import admin
from .forms import KsForm
from .assets import RADIO_FIELDS
from .models import *


@admin.register(Ks_pnuh)
@admin.register(Ks_snuh)
class KsAdmin(admin.ModelAdmin):
    form = KsForm

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

