import secrets
from django.utils.html import format_html

# generate key for encrypt
def generate_key():
    key = secrets.token_hex(32)
    print(key)

# link for viewing csv file
def generate_link(obj):
    csv_link = format_html(
        '<a target="_blank" href="/csv/%s/%s/%s">%s</a>' % (
            obj._meta.app_label, obj._meta.model_name, obj.pk, obj.csv))
    csv_link.allow_tags = True
    return csv_link
