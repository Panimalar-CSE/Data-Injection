from django.urls import path
from . import views

urlpatterns = [
    path('upload-excel/', views.ExcelFileUpload.as_view(), name='excel-file-upload'),
    path('upload-csv/', views.CsvFileUpload.as_view(), name='ecsv-file-upload'),
    path('get-nppes/', views.Nppes.as_view(), name="nppes-api"),
]
