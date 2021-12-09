from django.shortcuts import render
from django.apps import apps

def ViewCsv(request, app, model, pk):
    obj = apps.get_model(app, model).objects.get(pk=int(pk))
    file_field = [field for field in obj._meta.fields if field.get_internal_type() == 'FileField']
    context = { 
        'url': getattr(obj, file_field[0].name).url
    }
    return render(request, 'common/csv_parse.html', context)