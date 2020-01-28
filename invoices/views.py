from rest_framework import generics
from invoices.models import Invoice
from rest_framework.parsers import FileUploadParser
from invoices.models import File
from invoices.serializers import InvoiceSerializer
from invoices.serializers import FileSerializer
from invoices.serializers import ListFileSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework import status
from django.http import JsonResponse
from liftit_demo.tasks import async_process_csv
from django.core.files.storage import default_storage
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html', {})

class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    detail_serializer_class = ListFileSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return self.serializer_class

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    detail_serializer_class = ListFileSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return self.serializer_class

class UploadFileView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):

        if 'file' not in request.data:
            raise ParseError("Empty content")

        if 'session_name' not in request.data:
            raise ParseError("Not session information")

        upload = request.data['file']

        if not upload.name.endswith('.csv'):
            raise ParseError("Wrong format")


        default_storage.save(settings.BASE_DIR + '/tmp/' + upload.name, upload)
        path = settings.BASE_DIR + '/tmp/' + upload.name

        #Queue task using celery.
        async_task = async_process_csv.delay(path, upload.name, request.data['session_name'])

        return JsonResponse({'message': 'File in process', 'task_id': async_task.id}, status=status.HTTP_201_CREATED)



