from rest_framework import generics
from invoices.models import Invoice
from rest_framework.parsers import FileUploadParser
from invoices.models import File
from invoices.serializers import InvoiceSerializer
from invoices.serializers import FileSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework import status
from django.http import JsonResponse
from liftit_demo.tasks import async_process_csv
from django.core.files.storage import default_storage

def index(request):
    return render(request, 'index.html', {})

class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name = 'invoice-list'

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name = 'invoice-detail'


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    name = 'file-list'

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    name = 'file-detail'


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


        default_storage.save('tmp/'+upload.name, upload)
        path = default_storage.path('tmp/'+upload.name)

        #Queue task using celery.
        async_task = async_process_csv.delay(path, upload.name, request.data['session_name'])

        return JsonResponse({'message': 'File in process', 'task_id': async_task.id}, status=status.HTTP_201_CREATED)



