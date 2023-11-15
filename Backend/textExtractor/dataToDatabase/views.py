from django.shortcuts import render
import pandas
import pymongo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import requests
import json

# Database
mongo_client = pymongo.MongoClient("mongodb+srv://myAtlasDBUser:root@myatlasclusteredu.u3lj8ji.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client["TextToDb"]
my_collection = db["TextToDb"]
# file_path = 'C:\CTS Project\\textExtractor\\files\\records.xlsx'

api_url = "https://npiregistry.cms.hhs.gov/api/v2/npiregistry/search"


class Nppes(APIView):
    @staticmethod
    def post(request):
        api_key = request.data.get("api_key", None)
        npi_number = request.data.get("npi_number", None)

        headers = {"apikey": api_key}
        params = {"number": npi_number}

        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()
        return Response(data)


class ExcelFileUpload(APIView):
    @staticmethod
    def post(request, format="xlsx"):
        excel_file = request.FILES['file_to_extract']
        excel_data_df = pandas.read_excel(excel_file)
        json_str = excel_data_df.to_dict(orient='records')
        my_collection.insert_many(json_str)
        return Response(json_str)


class CsvFileUpload(APIView):
    @staticmethod
    def post(request, format="csv"):
        csv_file = request.FILES['file_to_extract']
        csv_data_df = pandas.read_csv(csv_file)
        json_str = csv_data_df.to_dict(orient='records')
        my_collection.insert_many(json_str)
        return Response(json_str)
