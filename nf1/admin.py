from django.contrib import admin

from .models import *
from .forms import CrfsForm
from .assets import DISPLAY_FIELDS, RADIO_FIELDS


class CrfOperationsInline(admin.TabularInline):
    model = CrfOperations
    fields = (
        'crf','no','date','age','status','reason','method'
    )
    readonly_fields = (
        'age',
    )
    extra = 1


@admin.register(Crf)
class CrfAdmin(admin.ModelAdmin):
    form = CrfsForm

    inlines = (CrfOperationsInline, )

    list_display = DISPLAY_FIELDS['crf']
    readonly_fields = (
        'age',
        'age_at_dx',
        'age_at_evaluation',
        'age_at_brain_mr',
        'age_at_spine_mr',
        'age_at_whole_body_mr',
        'age_at_breast_usg',
        'last_fu_age',
        'updated_at',
        'created_at',
    )
    fields = DISPLAY_FIELDS['crf']
    list_display_links = list_display
    list_filter = list_display
  
    # choice field: display radio
    radio_fields = { 
        radio_field: admin.HORIZONTAL for radio_field in RADIO_FIELDS['crf']
    }

    class Media:
        js = [
            '//ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
            'js/calculateAge.js'
        ]
