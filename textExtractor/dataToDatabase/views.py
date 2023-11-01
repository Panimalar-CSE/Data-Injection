from django.shortcuts import render
import pandas
import pymongo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

# Database
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["TextToDb"]
my_collection = db["TextToDb"]
# file_path = 'C:\CTS Project\\textExtractor\\files\\records.xlsx'


class ExcelFileUpload(APIView):
    @staticmethod
    def post(request, format="xlsx"):
        excel_file = request.FILES['file_to_extract']
        excel_data_df = pandas.read_excel(excel_file)
        json_str = excel_data_df.to_dict(orient='records')
        # my_collection.insert_many(json_str)
        return Response(json_str)


class CsvFileUpload(APIView):
    @staticmethod
    def post(request, format="csv"):
        csv_file = request.FILES['file_to_extract']
        csv_data_df = pandas.read_csv(csv_file)
        json_str = csv_data_df.to_dict(orient='records')
        # my_collection.insert_many(json_str)
        return Response(json_str)
