from django.contrib import admin

from .models import *
from .forms import IrdForm, IrdHistoryForm
from .assets import RADIO_FIELDS
from common.utils import generate_link

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

    readonly_fields = (
        'mutation_file_link', 
    )

    fields = [field.name for field in IrdHistory._meta.get_fields() if field.name != 'id']
    fields.append('mutation_file_link')

    # choice field: display radio
    radio_fields = { 
        radio_field: admin.HORIZONTAL for radio_field in RADIO_FIELDS['ird_history']
    }

    # link for viewing csv file
    def mutation_file_link(self, obj):
        return generate_link(obj)
    mutation_file_link.short_description = '파일 조회 링크'