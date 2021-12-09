from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('<str:app>/<str:model>/<int:pk>', views.ViewCsv, name='csv_view'),
]