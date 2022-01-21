import secrets
from django.utils.html import format_html

# generate key for encrypt
def generate_key():
    key = secrets.token_hex(32)
    print(key)

# link for viewing csv file
def generate_link(obj):
    file_field = [field for field in obj._meta.fields 
                    if field.get_internal_type() == 'FileField' and len(field.validators) > 0 and 'csv' in field.validators[0].allowed_extensions]
    csv_link = format_html(
        '<a target="_blank" href="/csv/%s/%s/%s">%s</a>' % (
            obj._meta.app_label, obj._meta.model_name, obj.pk, getattr(obj, file_field[0].name)))
    return csv_link


def calculate_age(to_date, from_date):
    if to_date is None or from_date is None:
        return None
    return to_date.year - from_date.year - ((to_date.month, to_date.day) < (from_date.month, from_date.day))