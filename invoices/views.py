from rest_framework import generics
from invoices.models import Invoice
from invoices.models import File
from invoices.serializers import InvoiceSerializer
from invoices.serializers import FileSerializer
from django.shortcuts import render

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