"""liftit_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view
from invoices.views import InvoiceList
from invoices.views import InvoiceDetail
from invoices.views import FileList
from invoices.views import FileDetail
from invoices.views import index
from invoices.views import UploadFileView

schema_view = get_swagger_view(title='Liftit DEMO API')


urlpatterns = [
    path('', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/', schema_view),

    path(
        'upload-file/',
        UploadFileView.as_view(),
        name='upload file'
    ),


    # Invoice Endpoint's
    path(
        'invoice/',
        InvoiceList.as_view(),
        name='invoice list'
    ),
    re_path(
        '^invoice/(?P<pk>[0-9a-f-]+)/$',
        InvoiceDetail.as_view(),
        name='invoice detail'
    ),


    # File Endpoint's
    path(
        'file/',
        FileList.as_view(),
        name='file list'
    ),
    re_path(
        '^file/(?P<pk>[0-9a-f-]+)/$',
        FileDetail.as_view(),
        name='file detail'
    ),
]