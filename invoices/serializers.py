from rest_framework import serializers
from invoices.models import Invoice
from invoices.models import File


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = (
            'id',
            'invoice_number',
            'client_name',
            'client_lastname',
            'client_id',
            'item_code',
            'item_description',
            'item_amount',
            'item_price',
            'item_discount_rate',
            'file',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
        )


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'filename',
            'total_items_price',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
        )


class ListFileSerializer(serializers.ModelSerializer):
    invoices = InvoiceSerializer(many=True)

    class Meta:
        model = File
        fields = (
            'id',
            'filename',
            'total_items_price',
            'created_at',
            'updated_at',
            'invoices'
        )
        read_only_fields = (
            'id',
        )